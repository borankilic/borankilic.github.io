BLUEPRINT 1: Finalize content migration & retire the uploads/ staging folder
BUILDER: Claude Haiku, working alone, cold start, cannot ask questions.  (Pure file inventory + move/delete + one .gitignore edit; no design or code logic, so the cheapest model is right.)

GOAL
  The Astro repo at /Users/borankilic/Desktop/projects/boran_website no longer contains an `uploads/` folder in its working tree. Every original source file that was in `uploads/` is preserved in a new archive folder OUTSIDE the repo (`/Users/borankilic/Desktop/boran_website_uploads_archive/`), so nothing is lost. The `uploads/` line in `.gitignore` is updated to a comment explaining the folder was archived. `npm run build` still succeeds.

CONTEXT THE BUILDER NEEDS (it has no memory of the planning chat)
  - Files to read first:
    - /Users/borankilic/Desktop/projects/boran_website/.gitignore
    - /Users/borankilic/Desktop/projects/boran_website/PLANNING.md  (sections 3 and 4 explain that uploads/ is a STAGING area whose processed copies now live in public/ and src/assets/, and that uploads/ is meant to be removed after migration)
  - Real inputs, in full: `uploads/` currently contains these source files (originals, NOT all migrated verbatim — some are .pptx/.docx/.ipynb sources that were only partially processed into the site):
      uploads/images/bio_boran Background Removed.png
      uploads/resume/CV_one_pager.pdf
      uploads/research/phase_interferometer/Interferometry_Theory.pdf
      uploads/research/phase_interferometer/g12Inter_exp_setup.pdf
      uploads/projects/brain_criticality_AD/Final_presentation_EE492.pptx
      uploads/projects/brain_criticality_AD/EE492_Final_Project_Report (2).pdf
      uploads/projects/epileptic_seizure_detection/epileptic_seizure_detection_using_wavelet_transform (3).pdf
      uploads/projects/NV_center_magnetometry/hyperfine_ODMR_spectra.docx
      uploads/projects/NV_center_magnetometry/nv_data_preprocessing.ipynb
      uploads/projects/NV_center_magnetometry/alternatic_square_test_field_report.docx
      uploads/projects/NV_center_magnetometry/experiment_report_dynamic_range_exploration.docx
      uploads/projects/NV_center_magnetometry/experiment_report_time_difference_between_detectors.docx
      uploads/projects/NV_center_magnetometry/experiment_report_LIA_spectra_freq_sweep.docx
      uploads/projects/NV_center_magnetometry/experiment_report_senitivity_compared_with_varying_laser power.docx
      uploads/projects/NV_center_magnetometry/experiment_report_plotting_sensitivity_graph.docx
      uploads/projects/NV_center_magnetometry/NV Center-OrnekUrunler.pptx
      uploads/projects/NV_center_magnetometry/NV_center_machine_learning.ipynb
      uploads/projects/synthetic_MRI/Abstract 360-04-011.pdf
      uploads/projects/neural_inspired_molecular_comm_networks/MOLCOM26_Neural_Inspired_Multi_Agent_Molecular_Communication_Networks_for_Collective_Intelligence (1).pdf
      uploads/projects/neural_inspired_molecular_comm_networks/MOLCOM26_Poster.pdf
      uploads/projects/brats_tumor_segmentation/EE475_Final_Project_Report (3).pdf
      uploads/projects/brats_tumor_segmentation/EE475_final_presentation_.pptx
      (plus .gitkeep and .DS_Store files, which are disposable)
  - Data shapes / examples: none — this is a filesystem operation.
  - Gotchas (READ THESE, they are why a naive "rm -rf uploads" is WRONG):
    1. `uploads/` is listed in `.gitignore` (line 19). That means it was NEVER committed to git. There is NO git history to recover it from. Deleting it is PERMANENT. This is why you archive, not delete.
    2. The `.gitignore` comment literally says "originals kept on disk" — the user's intent is that these source files survive as a backup. Do not destroy them.
    3. Several files (the .pptx presentations, the .docx experiment reports) exist ONLY here — they were never copied into public/ or src/. Do not assume "it's on the site so the original is safe."
    4. Two files ARE confirmed duplicates of committed files and are safe: `uploads/resume/CV_one_pager.pdf` is byte-identical to `public/resume.pdf` (both 147276 bytes); the headshot at `uploads/images/bio_boran Background Removed.png` corresponds to the processed `src/assets/boran.png`. You still archive them (don't delete), but they are not the risk.
    5. Do a MOVE (mv), not a copy-then-delete, so you never end up with the folder half-gone.

CONSTRAINTS (the limits)
  - Must stay inside: the `uploads/` folder (source), the new archive folder `/Users/borankilic/Desktop/boran_website_uploads_archive/` (destination), and `.gitignore` (one-line edit). Nothing else.
  - Must not change: any file under `public/`, `src/`, `astro.config.mjs`, `package.json`, content collections, or any published PDF/image. The live site output must be byte-for-byte identical after this.
  - Stack / tools to respect: plain shell (`mv`, `mkdir`). No npm packages, no scripts committed.
  - Non-negotiables: zero data loss. If any single file cannot be moved, STOP moving, leave everything in place, and report which file failed — do not continue deleting.

STEP-BY-STEP PLAN (in build order)
  1. Create the archive destination outside the repo:
     `mkdir -p "/Users/borankilic/Desktop/boran_website_uploads_archive"`
  2. Move the entire staging tree there in one operation (preserves subfolder structure):
     `mv "/Users/borankilic/Desktop/projects/boran_website/uploads" "/Users/borankilic/Desktop/boran_website_uploads_archive/uploads"`
     (Depends on step 1. After this, `boran_website/uploads` no longer exists.)
  3. Verify the move succeeded and nothing remains in the repo:
     - `ls "/Users/borankilic/Desktop/projects/boran_website/uploads"` must return "No such file or directory".
     - `find "/Users/borankilic/Desktop/boran_website_uploads_archive/uploads" -type f ! -name ".DS_Store" | wc -l` must be at least 22 (the source files listed above).
  4. Edit `/Users/borankilic/Desktop/projects/boran_website/.gitignore`: replace the block that currently reads (lines ~17-19):
        # Staging area: raw source materials (originals kept on disk, processed copies
        # live in public/ and src/assets/). Keeps the repo lean and under Pages limits.
        uploads/
     with:
        # Staging area retired 2026-07: originals archived at
        # ~/Desktop/boran_website_uploads_archive/uploads/ . Processed copies live in
        # public/ and src/assets/. Left ignored in case the folder is ever recreated.
        uploads/
     (Keep the `uploads/` line so a recreated folder stays ignored.)
  5. Confirm the site still builds (depends on nothing above being wrong):
     `cd /Users/borankilic/Desktop/projects/boran_website && npm run build`
     Must exit 0.

EXACT INPUTS TO USE
  - Files to open or create, by name: `.gitignore` (edit); `/Users/borankilic/Desktop/boran_website_uploads_archive/` (create).
  - The one prompt to hand the builder to kick this off:
    "Open blueprints/01-finalize-and-remove-uploads.md in /Users/borankilic/Desktop/projects/boran_website and execute it exactly. This is a filesystem-safety task: MOVE the gitignored uploads/ folder to an archive outside the repo (never delete it — it was never committed and holds the only copies of some source files), update the .gitignore comment, and confirm npm run build still passes. Follow the DEFINITION OF DONE checklist before reporting."
  - Copy / values / snippets to use verbatim: the replacement `.gitignore` comment block in step 4.

DEFINITION OF DONE (checklist the builder ticks against its own output before calling it finished)
  [ ] `/Users/borankilic/Desktop/projects/boran_website/uploads` no longer exists (ls returns not-found).
  [ ] `/Users/borankilic/Desktop/boran_website_uploads_archive/uploads/` exists and contains >= 22 non-.DS_Store files, including the .pptx and .docx originals listed above.
  [ ] `.gitignore` still contains the `uploads/` line and its comment now points to the archive path.
  [ ] `npm run build` exits 0.
  [ ] No file under public/ or src/ was modified (git status shows only .gitignore changed).
  [ ] nothing in CONSTRAINTS was violated (zero files lost).

IF SOMETHING IS UNCLEAR (anti-stall)
  If the archive path already exists with content, do NOT overwrite it — append a timestamp suffix to the destination folder name (e.g. `uploads_archive_20260708`), note it as 'ASSUMPTION: ...' at the top of your output, and continue. If any file refuses to move (permissions, open handle), stop all further deletion, restore anything half-moved, and report the exact file. Never delete a source file to "make room."
