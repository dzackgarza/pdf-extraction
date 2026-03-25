# PDF Extraction Plan

## Goal

Extract all 615 PDFs from `/home/dzack/Dropbox/Library/` on `dzack@ssh-work.dzackgarza.com` to markdown using CPU-based MinerU extraction.

## Current Status

**Active Job:** Elmendorf - "Rings, Modules, and Algebras in Stable Homotopy Theory" (265 pages)

**Last Known State (03:45 UTC):**

- Layout Predict: 100% ✓
- MFD Predict: 100% ✓
- MFR Predict: 12% (1456/11774 formulas)
- Estimated time remaining: ~47 minutes for MFR stage alone

**Blocker:** SSH tunnel disconnected (cloudflared handshake error). Cannot monitor or submit new jobs.

## Workflow (from GAPS.md)

For each PDF in the checklist:

1. **Copy PDF to remote** → `~/pdf-inputs/<simplified-name>.pdf`
2. **Submit to tmux** → `tmux send-keys -t pdf-extraction 'cd /home/dzack/pdf-extraction && source .venv/bin/activate && mineru -p ~/pdf-inputs/<name>.pdf -o ~/pdf-outputs/ -b pipeline -m auto -l en -d cpu -f true -t false' Enter`
3. **Monitor loop** → `tmux capture-pane -pt pdf-extraction` every 300s until `"local output dir is"` appears
4. **Copy markdown back** → `scp dzack@ssh-work.dzackgarza.com:~/pdf-outputs/<name>/auto/<name>.md /home/dzack/pdf-extraction/extracted/`
5. **Clean up remote** → `ssh dzack@ssh-work.dzackgarza.com "cd ~/pdf-outputs/<name>/auto/ && gio trash images/ *_layout.pdf *_span.pdf *_origin.pdf *_middle.json *_model.json *_content_list.json"`
6. **Mark complete** → Update GAPS.md checklist with `[x]`

## Performance Estimates

- **Throughput:** ~3-4 pages/min on CPU (4 core, 32GB RAM)
- **Elmendorf (265 pages):** ~75-90 minutes total
- **Average book (300 pages):** ~75-100 minutes
- **Total library (615 PDFs, ~100k pages est.):** ~400-500 hours CPU time

## Queue Management

**Input staging:** `~/pdf-inputs/` on remote
**Output directory:** `~/pdf-outputs/<pdf-stem>/auto/<pdf-stem>.md`

Process one PDF at a time sequentially. No parallel jobs (RAM limited to 32GB).

## Files to Maintain

- `GAPS.md` - Master checklist with workflow instructions
- `PLAN.md` - This file (current status, queue, blockers)
- `EXTRACTION_LOG.md` - Timestamped log of completed extractions

## Next Actions

1. Restore SSH connectivity
2. Check status of Elmendorf extraction
3. If complete: copy markdown, clean up, mark complete in GAPS.md
4. Submit next PDF from GAPS.md checklist
5. Repeat for all 615 PDFs

## Error Handling

**If tmux session dies:** Job must restart from scratch (no checkpoint/resume)
**If SSH disconnects:** Wait for reconnection, check tmux session status
**If MinerU fails:** Check error output, may need to adjust parameters or skip corrupted PDF

## Metrics to Track

- PDFs completed: 0 / 615
- Total pages processed: 0
- Success rate: N/A
- Average extraction time: TBD
- Failures: 0
