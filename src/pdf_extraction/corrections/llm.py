"""
Extract OCR errors that preclude mathematical understanding from a PDF extraction.

Focus: Errors where the OCR output is mathematically wrong or unreadable.
Skip: Spacing, capitalization, punctuation, hyphenation, LaTeX formatting.
"""

import os
import tiktoken
import time
from openai import OpenAI

# Configuration
CHUNK_SIZE = 100_000  # tokens per chunk
MAX_RETRIES = 5
RETRY_DELAY = 45  # seconds (Gemini free tier rate limit reset)
MODEL = 'gemini-2.5-flash'

PROMPT = """Find OCR errors where extracted text is MATHEMATICALLY WRONG or UNREADABLE.

REPORT:
- Wrong symbols: E for summation, E for element-of, 0 for O (orthogonal group), ! for T (transpose)
- Garbled formulas where the math is broken
- Missing critical symbols that change meaning
- Subscripts/superscripts wrong so variables are unidentifiable
- Words so garbled the sentence is incomprehensible

DO NOT REPORT (these don't break understanding):
- Spacing: "$p$ -adic" vs "$p$-adic" - SKIP
- Capitalization: "From" vs "from" - SKIP
- Punctuation: missing periods, commas - SKIP
- Hyphenation: "MordellWeil" vs "Mordell-Weil" - SKIP
- LaTeX formatting: extra braces, spacing in math mode - SKIP

Format: LINE_NUM: "wrong" -> "right"
LINE_NUM is approximately {start_line} + offset within this chunk.

Text:
{chunk_text}

Errors:"""


def extract_errors(input_file: str, output_file: str):
    """Extract OCR errors and write to output file."""
    
    # Load and tokenize input
    with open(input_file) as f:
        content = f.read()
    
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(content)
    print(f"Input: {len(tokens):,} tokens ({len(content):,} chars)")
    
    gemini_api_key = os.environ.get('GEMINI_API_KEY', 'AIzaSyA_ty8ZeH-JSM4gHM_Fyr6IdCg3vYcmCQ8')

    # Initialize client
    client = OpenAI(
        api_key=gemini_api_key,
        base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
    )
    
    all_errors = []
    chunk_num = 0
    
    for i in range(0, len(tokens), CHUNK_SIZE):
        chunk_tokens = tokens[i:i+CHUNK_SIZE]
        chunk_text = enc.decode(chunk_tokens)
        start_line = content[:enc.decode(tokens[:i]).rfind('\n')].count('\n') + 1
        chunk_num += 1
        
        print(f"Chunk {chunk_num} (lines ~{start_line})...", end=" ", flush=True)
        
        prompt = PROMPT.format(start_line=start_line, chunk_text=chunk_text)
        
        for attempt in range(MAX_RETRIES):
            try:
                resp = client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=12000,
                    timeout=180
                )
                
                text = resp.choices[0].message.content
                errors = [l.strip() for l in text.split('\n') 
                         if l.strip() and '->' in l and l.strip()[0].isdigit()]
                
                print(f"{len(errors)} errors")
                all_errors.extend(errors)
                break
                
            except Exception as e:
                if '429' in str(e) and attempt < MAX_RETRIES - 1:
                    print(f"rate limited, waiting {RETRY_DELAY}s...")
                    time.sleep(RETRY_DELAY)
                else:
                    print(f"FAILED: {e}")
                    break
    
    # Write output
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(f"# Mathematical Corrections\n")
        f.write(f"**Source**: {os.path.basename(input_file)}\n")
        f.write(f"**Total**: {len(all_errors)} errors\n\n")
        for e in all_errors:
            f.write(e + '\n')
    
    print(f"\nOutput: {len(all_errors)} errors → {output_file}")
    return all_errors
