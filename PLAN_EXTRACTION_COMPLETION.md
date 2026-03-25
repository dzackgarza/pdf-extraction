# PDF Extraction Completion Plan

**Created:** 2026-03-19  
**Status:** Ready for execution  
**Goal:** Complete all pending PDF extractions using new remote-first architecture

---

## Current State

### Incomplete Extractions

| PDF                                          | Pages | Status            | Priority |
| -------------------------------------------- | ----- | ----------------- | -------- |
| Vakil - Foundations of Algebraic Geometry    | 838   | 6 failed attempts | HIGH     |
| Peters-Sterk - Symmetric and Quadratic Forms | ~491  | Not attempted     | HIGH     |
| Hartshorne - Algebraic Geometry              | ~300  | Not attempted     | LOW      |
| FOAG (Friberg)                               | ~600  | Not attempted     | LOW      |

### Previous Vakil Failures (all 6 attempts)

1. MinerU produced no output files (2x)
2. Notebook didn't produce extraction output after 153min
3. GPU session limit reached (max 2 parallel) (2x)
4. Dataset title conflict

### Architecture Status

- ✅ New remote-first CLI implemented
- ✅ State machine with 7 states
- ✅ All 42 tests passing
- ✅ All local job state cleared
- ✅ No remote kernels running

---

## Execution Plan

### Phase 1: Validation (30 min)

**Goal:** Verify new CLI workflow functions correctly

1. **Test with small PDF** (5-10 pages)
   - Use existing test PDF or create new small fixture
   - Run full workflow: prepare → submit → poll → download
   - Verify state transitions work correctly
   - Validate output quality

2. **Verify monitoring tools**
   - Test `just kaggle-status` with refresh
   - Test `just kaggle-poll` for monitoring
   - Confirm staleness detection works

### Phase 2: Peters-Sterk Extraction (2 hours)

**Goal:** Complete first successful large-book extraction

**Rationale:** Known good benchmark (23.68 pages/min on P100), ~21min total runtime

**Batching Strategy:**

- Batch size: 200 pages (4 batches total)
- Sequential execution (avoid GPU session limits)
- GPU enabled with formula extraction

**Steps:**

1. `just kaggle-prepare-pdf /home/dzack/pdfs/Peters-Sterk_2024_Symmetric-and-Quadratic-Forms/Peters-Sterk_2024_Symmetric-and-Quadratic-Forms.pdf dzackgarza --batch-size 200`
2. Submit batch 1, poll to completion
3. Submit batch 2, poll to completion
4. Submit batch 3, poll to completion
5. Submit batch 4, poll to completion
6. Download all batches
7. Merge outputs
8. Validate markdown quality

### Phase 3: Vakil Extraction (4 hours)

**Goal:** Complete Vakil extraction with lessons learned

**Batching Strategy (optimized from failures):**

- Batch size: 150 pages (6 batches total)
- **Sequential only** (no parallel - avoids GPU session limit)
- GPU enabled with formula extraction
- Extended timeout (30min per batch)

**Steps:**

1. Prepare 6 batches of 150 pages each
2. Submit and monitor each batch sequentially
3. Download all completed batches
4. Merge all outputs
5. Validate markdown quality

**Risk Mitigation:**

- If MinerU produces no output: try CPU fallback for that batch
- If GPU limit hit: wait and retry (sequential should prevent this)
- If timeout: increase batch timeout, reduce batch size

### Phase 4: Documentation (30 min)

**Goal:** Update all documentation with results

1. Update EXTRACTIONS.md with all results
2. Document batching strategy that worked
3. Add troubleshooting guide for common failures
4. Update README with new CLI commands

---

## Success Criteria

- [ ] Peters-Sterk: Complete markdown output with all formulas preserved
- [ ] Vakil: Complete markdown output with all formulas preserved
- [ ] No GPU session limit errors
- [ ] All state transitions logged correctly
- [ ] Documentation updated

---

## Timeline

| Phase                  | Duration | Cumulative |
| ---------------------- | -------- | ---------- |
| Phase 1: Validation    | 30 min   | 30 min     |
| Phase 2: Peters-Sterk  | 2 hours  | 2.5 hours  |
| Phase 3: Vakil         | 4 hours  | 6.5 hours  |
| Phase 4: Documentation | 30 min   | 7 hours    |

**Total estimated time:** 7 hours (can be split across sessions)

---

## Commands Reference

### Preparation

```bash
just kaggle-prepare-pdf <pdf_path> <owner> --batch-size 200
```

### Submission & Monitoring

```bash
just kaggle-submit <job_dir>
just kaggle-poll <job_dir> --interval 30 --timeout 1800
just kaggle-status <job_dir> --refresh
```

### Download & Merge

```bash
just kaggle-download <job_dir>
just kaggle-merge-single <job1> <job2> --output <merged.md>
```

### Batch Operations

```bash
just kaggle-batch-status --json <job1> <job2> <job3>
just kaggle-batch-download <job1> <job2> <job3>
```
