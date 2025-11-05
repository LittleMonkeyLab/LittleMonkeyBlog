# Quick Start Guide

## 🚀 Create a New Post

```bash
python3 new_post.py "Your Post Title"
```

## 👀 Preview Your Blog

```bash
quarto preview
```

Then open http://localhost:4200 in your browser.

## 📤 Publish Your Blog

```bash
git add .
git commit -m "Add new post"
git push origin main
```

GitHub Actions will automatically deploy it!

## 🎯 Cursor Shortcuts

Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux), then:

- **"Create New Blog Post"** - Create a new post (prompts for title)
- **"Preview Blog (Local)"** - Start local preview server
- **"Render Blog"** - Build the site
- **"Quick Publish (Render + Push)"** - One-step publish

## 📝 Post Template

Each post lives in `posts/[slug]/index.qmd` with this structure:

```yaml
---
title: "Your Title"
date: "YYYY-MM-DD"
categories: [Category1, Category2]
description: "Brief description"
---
```

## 💡 Tips

- Use `new_post.py` to create posts with proper structure
- Preview before pushing to catch errors early
- Posts auto-deploy on push to `main`
- Check `.cursor/instructions.md` for detailed workflow

