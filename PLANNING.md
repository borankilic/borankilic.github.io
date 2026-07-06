# Personal Website — Planning Report

**Date:** 2026-07-05
**Decisions made:** Astro · minimal academic design · PDFs committed in-repo (compressed) · hosted at `<username>.github.io`

---

## 1. Goal

A plain but professional personal website hosted free on GitHub Pages, with:

| Section | Purpose |
|---|---|
| Home / About | Who you are, headshot, short bio, contact links |
| Projects | Showcase of software/hardware projects with links to code |
| Research | Current and past research, papers, posters |
| Blog | Occasional posts written in Markdown |
| Coursework | Notes and homework PDFs from previous classes, organized by course |
| Resume | Viewable/downloadable PDF + contact information |

## 2. Stack and hosting

- **Generator:** [Astro](https://astro.build). Pages and blog posts are written in Markdown; Astro compiles everything to plain static HTML/CSS — fast, no client-side framework needed for a site like this.
- **Hosting:** GitHub Pages, free. The repo must be named **`<your-github-username>.github.io`** and the site will be live at `https://<username>.github.io`.
- **Deployment:** A GitHub Actions workflow (Astro provides an official one, `withastro/action`) builds the site on every `git push` to `main` and publishes it. You never build locally unless you want to preview.
- **HTTPS:** automatic. **Custom domain:** can be added later in ~5 minutes (one CNAME file + DNS record), no restructuring.

### GitHub Pages limits you must know

| Limit | Value | Consequence for you |
|---|---|---|
| Max file size | 100 MB hard limit (warning at 50 MB) | No single PDF over ~50 MB should be committed |
| Repo size | ~1 GB soft limit (5 GB hard) | Total PDFs + images should stay well under ~500 MB |
| Bandwidth | 100 GB/month soft limit | Irrelevant for a personal site |
| Git LFS | **NOT served by GitHub Pages** | Do not use LFS for anything the site links to |

## 3. Hosting large files: the strategy

### PDFs (notes, homework, papers) — commit in-repo, compressed first

Most lecture notes and homework PDFs are 0.5–5 MB and fine as-is. **Scanned** documents are the problem (often 20–100 MB). Before committing any PDF over ~10 MB, compress it:

```bash
# ghostscript: usually 5–10x smaller for scans, still readable
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=out.pdf in.pdf
```

(`/ebook` = 150 dpi, good for screen reading; use `/printer` = 300 dpi if quality matters.)

**Escape hatch:** if some file is still >25 MB after compression (e.g. a full scanned textbook of notes), attach it to a **GitHub Release** in this repo (2 GB/file allowed) and link to the release asset from the site. Release assets get permanent URLs and don't count toward Pages limits.

### Images

- Headshot + project screenshots: export as **WebP or JPEG, ≤ 1600 px wide, target < 300 KB each**. `cwebp -q 80 in.png -o out.webp` or any export tool.
- Astro's built-in `<Image>` component will handle resizing/optimizing automatically at build time.

### Code

- **Don't host code on the website.** Each project lives in its own GitHub repository; the website links to it. Short illustrative snippets go inline in blog/project pages with syntax highlighting (Astro does this out of the box via Shiki).

## 4. Repository structure

### Now (staging — this is where YOU put files)

```
boran_website/
├── PLANNING.md              ← this file
├── .gitignore
├── .agents/skills/          ← frontend-design skill (drives the visual design work)
└── uploads/                 ← STAGING AREA: drop your raw materials here
    ├── resume/              ← resume PDF (and source .tex/.docx if you want it versioned)
    ├── images/              ← headshot, project screenshots, research figures
    ├── projects/            ← one .md or .txt per project (see checklist below)
    ├── research/            ← papers (PDF), posters, project descriptions
    ├── coursework/          ← one folder per course, e.g. coursework/PHYS-143a/ with PDFs
    └── blog-drafts/         ← any posts you already want up, as .md or plain text
```

Once you've dropped materials in `uploads/`, the site gets scaffolded and content is migrated into the Astro structure below; `uploads/` is then deleted.

### After scaffolding (target Astro layout)

```
boran_website/
├── astro.config.mjs
├── package.json
├── .github/workflows/deploy.yml    ← auto-deploy to Pages on push
├── public/                          ← served verbatim at site root
│   ├── resume.pdf                   → yoursite/resume.pdf
│   ├── pdfs/
│   │   ├── coursework/<course>/     → yoursite/pdfs/coursework/...
│   │   └── research/
│   └── favicon.svg
└── src/
    ├── assets/                      ← images (optimized at build)
    ├── components/                  ← header, footer, post list, etc.
    ├── layouts/                     ← base page + blog post layouts
    ├── content/                     ← Markdown content collections
    │   ├── blog/        one .md per post (frontmatter: title, date, tags)
    │   ├── projects/    one .md per project
    │   └── courses/     one .md per course (description + list of its PDFs)
    └── pages/
        ├── index.astro              ← home/about
        ├── projects.astro
        ├── research.astro
        ├── blog/                    ← index + [slug] route
        ├── coursework.astro
        └── resume.astro             ← embedded PDF viewer + download link
```

Adding a blog post later = create one Markdown file in `src/content/blog/`, `git push`. Same for projects and courses. No HTML editing, ever.

## 5. What you need to upload (checklist)

Drop these into `uploads/`:

**Identity & contact**
- [ ] Resume as PDF (`uploads/resume/`)
- [ ] Headshot photo (`uploads/images/`)
- [ ] Contact info: email to display, plus links — GitHub, LinkedIn, Google Scholar, ORCID, X/Bluesky (whatever applies). A plain text file is fine.
- [ ] Short bio (2–4 sentences) and a longer one if you want an About section. Your GitHub username (needed for the repo name).

**Projects** — for each: a few sentences on what/why/how, tech used, link to its GitHub repo, 1–2 screenshots or a figure, year.

**Research** — for each project: title, one-paragraph description, advisor/lab, status (ongoing/published), paper or poster PDF if public, arXiv/DOI links.

**Coursework** — one folder per course named like `PHYS-143a-quantum-mechanics/`. Inside: the notes/homework PDFs (compressed per §3), and optionally a line about the course (semester, instructor, what the materials cover). **Check you have the right to post them** — your own notes are yours; official solutions or instructor slides usually aren't postable.

**Blog** — any existing drafts as Markdown or plain text.

## 6. Design direction: minimal academic

Executed with the installed `frontend-design` skill. Guardrails:

- Typography-first: a well-chosen serif for body (e.g. Source Serif, Newsreader) with a clean sans or mono for metadata; generous line-height; measure ~65ch.
- Near-white background, near-black text, **one** restrained accent color for links.
- No cards, no hero banners, no animations. Navigation is a simple text header.
- Blog and coursework pages are essentially beautiful lists. Fast: no JS beyond what's needed (target: none).
- Reference points: academic personal pages, gwern.net's restraint, distill.pub's typography.

## 7. Roadmap

1. **Done:** git repo initialized, staging structure created, `frontend-design` skill installed, this plan.
2. **You:** answer the checklist in §5 — drop files into `uploads/`, create the GitHub repo named `<username>.github.io`.
3. Scaffold Astro, build layouts/pages per §6, migrate `uploads/` content in.
4. Set up the deploy workflow, push, enable Pages (Settings → Pages → Source: GitHub Actions).
5. Verify live site, iterate on design.
6. Later (optional): custom domain, RSS feed for the blog (Astro one-liner), analytics (e.g. GoatCounter, free + private).

## 8. Ongoing maintenance

- New blog post → add `.md` file, push.
- New course materials → compress PDFs, drop into `public/pdfs/coursework/<course>/`, add/update the course `.md`, push.
- Resume update → replace `public/resume.pdf`, push.
- Every push auto-deploys in ~1–2 minutes.
