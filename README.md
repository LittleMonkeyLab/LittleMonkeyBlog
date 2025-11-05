# LittleMonkeyBlog

Little Monkeys Blogging!

## Quick Start

### Creating a New Blog Post

**Option 1: Using the helper script (recommended)**
```bash
python3 new_post.py "My New Post Title"
```

With additional options:
```bash
python3 new_post.py "My Post" --categories "Data Science,Tutorial" --description "A great post about data"
```

**Option 2: Using Cursor Tasks**
1. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "Tasks: Run Task"
3. Select "Create New Blog Post"
4. Enter your post title

### Previewing Locally

```bash
quarto preview
```

Or use the Cursor task: "Preview Blog (Local)"

### Publishing

Simply push to the `main` branch:
```bash
git add .
git commit -m "Add new post"
git push origin main
```

The GitHub Actions workflow will automatically build and deploy to GitHub Pages.

Or use the Cursor task: "Quick Publish (Render + Push)" for a one-step publish.

## Project Structure

- `posts/` - Blog posts directory
  - Each post is in its own folder: `posts/[slug]/index.qmd`
- `_quarto.yml` - Quarto configuration
- `.github/workflows/publish.yml` - GitHub Actions workflow for auto-deployment
- `new_post.py` - Helper script to create new posts

## Recommended Cursor Extensions

Cursor will prompt you to install these if you open the workspace:
- Quarto (for `.qmd` file support)
- R (for R code chunks)
- Prettier (for code formatting)

## Workflow

1. **Create**: Use `new_post.py` or create manually in `posts/[slug]/index.qmd`
2. **Write**: Edit your post in Cursor
3. **Preview**: Run `quarto preview` to see your changes
4. **Publish**: Commit and push to `main` - GitHub Actions handles the rest!

For more detailed instructions, see `.cursor/instructions.md`.
