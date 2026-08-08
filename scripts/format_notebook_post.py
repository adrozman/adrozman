#!/usr/bin/env python3
"""
Utility script to convert a jupyter nbconvert markdown output into a formatted Jekyll post.

Example Usage:
    ./scripts/format_notebook_post.py \\
      /path/to/my_new_notebook.ipynb \\
      /path/to/my_new_notebook.md \\
      --date 2026-10-15 \\
      --title "My Awesome Post Title" \\
      --description "A brief summary of my post" \\
      --thumbnail "/images/posts/my_new_notebook_files/plot_1_1.png"
"""
import os
import re
import json
import shutil
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Convert jupyter nbconvert markdown into a formatted Jekyll post.")
    parser.add_argument("notebook_path", help="Path to the original .ipynb file")
    parser.add_argument("markdown_path", help="Path to the nbconvert generated .md file")
    parser.add_argument("--date", help="Date for the post (YYYY-MM-DD)", required=True)
    parser.add_argument("--title", help="Title of the post", required=True)
    parser.add_argument("--description", help="Description for the post", required=True)
    parser.add_argument("--thumbnail", help="Path to the thumbnail image (relative to /images/posts/)", required=True)
    
    args = parser.parse_args()

    # Paths setup
    scripts_dir = Path(__file__).resolve().parent
    repo_root = scripts_dir.parent

    nb_src = Path(args.notebook_path).resolve()
    md_src = Path(args.markdown_path).resolve()
    basename = md_src.stem
    
    md_dst = repo_root / "_posts" / f"{args.date}-{basename.replace('_', '-')}.md"
    nb_dst = repo_root / "notebooks" / f"{basename}.ipynb"
    
    img_src = md_src.parent / f"{basename}_files"
    img_dst = repo_root / "images" / "posts" / f"{basename}_files"
    permalink = f"/blog/{basename.replace('_', '-')}/"
    
    print(f"Generating post for '{args.title}'...")

    # 1. Modify the notebook and copy
    with open(nb_src, 'r') as f:
        nb = json.load(f)

    # Insert the Author/Contact block into the first markdown cell
    header = f"**Author:** Adam Rozman  \n**Contact:** arozman@bu.edu  \n**Writeup:** [adrozman.github.io{permalink}](https://adrozman.github.io{permalink})  \n\n"
    nb['cells'][0]['source'].insert(0, header)

    with open(nb_dst, 'w') as f:
        json.dump(nb, f, indent=1)

    # 2. Copy the image folder
    if img_src.exists():
        if img_dst.exists():
            shutil.rmtree(img_dst)
        shutil.copytree(img_src, img_dst)

    # 3. Format the markdown file
    with open(md_src, 'r') as f:
        lines = f.readlines()

    frontmatter = f"""---
layout: post
title: "{args.title}"
date: {args.date}
description: "{args.description}"
author: Adam Rozman
permalink: {permalink}
thumbnail: "{args.thumbnail}"
---

"""

    colab_link = f"""
Open this Jupyter notebook in Colab to follow along and modify, or save for future use:
<a href="https://colab.research.google.com/github/adrozman/adrozman.github.io/blob/gh-pages/notebooks/{basename}.ipynb" target="_blank" rel="noopener noreferrer">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" width="200">
</a>

"""

    out_lines = [frontmatter]
    in_code_block = False
    in_plotting = False
    first_cell = True

    for line in lines:
        if line.startswith("    Text(") and "Text(" in line:
            continue
            
        if f"![png]({basename}_files/" in line:
            line = line.replace(f"![png]({basename}_files/", f"![png](/images/posts/{basename}_files/")

        if line.startswith("```python"):
            in_code_block = True
            in_plotting = False
            out_lines.append(line)
            continue

        if in_code_block and line.startswith("```") and not line.startswith("```python"):
            if in_plotting:
                while out_lines and out_lines[-1].strip() == "":
                    out_lines.pop()
                out_lines.append("\n{% endhighlight %}\n</details>\n\n")
                in_plotting = False
                in_code_block = False
            else:
                while out_lines and out_lines[-1].strip() == "":
                    out_lines.pop()
                out_lines.append("\n" + line)
                in_code_block = False
            
            if first_cell:
                first_cell = False
            continue

        if in_code_block:
            if first_cell and line.startswith("# Set plotting convention"):
                out_lines.append("```\n")
                in_code_block = False 
                first_cell = False
                continue
                
            if not in_plotting and "plt.figure(" in line:
                while out_lines and out_lines[-1].strip() == "":
                    out_lines.pop()
                out_lines.append("\n```\n\n")
                out_lines.append('<details markdown="0">\n<summary>View plotting code</summary>\n{% highlight python %}\n')
                in_plotting = True
            
            out_lines.append(line)
            continue

        if not in_code_block:
            if line.startswith("*For a refresher on the fundamentals"):
                out_lines.append(line)
                out_lines.append(colab_link)
                continue
            out_lines.append(line)

    # Clean up empty code blocks
    clean_lines = []
    skip = False
    for i in range(len(out_lines)):
        if skip:
            skip = False
            continue
        if out_lines[i].strip() == "```python" and i+1 < len(out_lines) and out_lines[i+1].strip() == "```":
            skip = True
            continue
        clean_lines.append(out_lines[i])

    with open(md_dst, 'w') as f:
        f.writelines(clean_lines)

    print(f"Formatting successful! Saved post to {md_dst}")

if __name__ == "__main__":
    main()
