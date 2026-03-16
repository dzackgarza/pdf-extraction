import sys
import argparse
from pdf_extraction.corrections.llm import extract_errors

def main():
    parser = argparse.ArgumentParser(
        description="Extract OCR errors that preclude mathematical understanding from a PDF extraction."
    )
    parser.add_argument("input_file", help="Input markdown file")
    parser.add_argument("output_file", help="Output markdown file")
    
    args = parser.parse_args()
    extract_errors(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
