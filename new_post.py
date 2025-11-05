#!/usr/bin/env python3
"""
Create a new blog post for LittleMonkeyBlog

Usage:
    python new_post.py "My Post Title"
    python new_post.py "My Post Title" --slug "custom-slug"
    python new_post.py "My Post Title" --categories "Data Science,Tutorial"
"""

import argparse
import os
import re
from datetime import datetime
from pathlib import Path


def slugify(text):
    """Convert text to a URL-friendly slug"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text


def create_post(title, slug=None, categories=None, description=None, image=None):
    """Create a new blog post directory and file"""
    
    # Use provided slug or generate from title
    if slug is None:
        slug = slugify(title)
    
    # Create post directory
    posts_dir = Path("posts")
    post_dir = posts_dir / slug
    post_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if post already exists
    post_file = post_dir / "index.qmd"
    if post_file.exists():
        print(f"⚠️  Post already exists at {post_file}")
        response = input("Do you want to overwrite it? (y/N): ")
        if response.lower() != 'y':
            print("Cancelled.")
            return
    
    # Get today's date
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Default categories
    if categories is None:
        categories = ["News", "Methods", "Research"]
    elif isinstance(categories, str):
        categories = [c.strip() for c in categories.split(",")]
    
    # Create post template
    template = f"""---
title: "{title}"
date: "{today}"
categories: {categories}
description: "{description or 'A new blog post'}"
{f'image: {image}' if image else ''}
---

## Introduction

Write your introduction here. This is where you hook your readers and introduce the main topic.

## Main Content

Add your main content here. You can include:

- Lists
- **Bold text**
- *Italic text*
- Code blocks
- And more!

### Subsections

You can organize your content with subsections like this.

```python
# Example code block
def example():
    print("Hello, world!")
```

## Conclusion

Wrap up your post with a conclusion that summarizes key points and provides next steps or takeaways.

<!--------------- appendices go here ----------------->
## Last Updated {{.appendix}}
```{{r}}
#| echo: false
today <- Sys.Date()
format(today, format="%d %B %Y")
```

## Acknowledgments {{.appendix}}

Thank you for reading!
"""
    
    # Write post file
    post_file.write_text(template)
    
    print(f"✅ Created new blog post: {post_file}")
    print(f"📝 Edit it at: {post_file.absolute()}")
    print(f"🔗 Post URL will be: /posts/{slug}/")
    print(f"\n💡 Next steps:")
    print(f"   1. Edit {post_file}")
    print(f"   2. Preview with: quarto preview")
    print(f"   3. Commit and push to publish")


def main():
    parser = argparse.ArgumentParser(
        description="Create a new blog post for LittleMonkeyBlog",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python new_post.py "My New Post"
  python new_post.py "Advanced Analysis" --slug "advanced-analysis"
  python new_post.py "Data Science Tips" --categories "Data Science,Tutorial"
  python new_post.py "Quick Guide" --description "A quick guide to..."
        """
    )
    
    parser.add_argument(
        "title",
        help="Title of the blog post"
    )
    
    parser.add_argument(
        "--slug",
        help="URL slug (default: auto-generated from title)"
    )
    
    parser.add_argument(
        "--categories",
        help="Comma-separated list of categories (default: News, Methods, Research)"
    )
    
    parser.add_argument(
        "--description",
        help="Post description/meta description"
    )
    
    parser.add_argument(
        "--image",
        help="Image filename (e.g., RMIPHEX.png)"
    )
    
    args = parser.parse_args()
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    create_post(
        title=args.title,
        slug=args.slug,
        categories=args.categories,
        description=args.description,
        image=args.image
    )


if __name__ == "__main__":
    main()

