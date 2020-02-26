#!/usr/bin/env python3
import sys
import subprocess
import pathlib
import shutil
import frontmatter
import yaml

from src.utils import run_pandoc, copytree, list_categories, format_time
from src.sitemap_generator import Sitemap
from src.args import DefaultArguments

path_root = pathlib.Path('.')
path_site = pathlib.Path('public')
path_posts = pathlib.Path('_posts')
path_tmp = pathlib.Path('tmp')

# DO NOT REMOVE ANYTHING ON ./public recursively
path_site.mkdir(exist_ok=True)
path_tmp.mkdir(exist_ok=True)

copytree(path_root/'_assets', path_site/'assets')
shutil.copy(path_root/'template/style.css', path_site/'assets/style.css')

pandoc_args = {
    "template": "template/index.html",
    "mathjax": "",
    "metadata-file": "tmp/config.yml",
    "highlight-style": "breezeDark"
}

with open("config.yml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

args_parser = DefaultArguments()
args = args_parser.parse_args(sys.argv[1:])
if args.site_root is not None:
    config['site-root'] = args.site_root
if args.serve:
    config['site-root'] = 'http://localhost:8000'

def build_posts(post_files):
    """Returns a list of dicts with metadata from each post"""
    posts = []
    for p in post_files:
        with open(p, encoding='utf_8') as f:
            metadata, content = frontmatter.parse(f.read())

        if not args.draft:
            if 'draft' in metadata.keys(): # Do not build drafts
                continue

        p_data = {
            'title' : metadata['title'],
            'categories' : metadata['categories'],
            'description' : metadata['description'],
            'date' : format_time(metadata['date']),
            'url' : "posts/" + metadata['slug'].replace(' ', '-') + ".html",
            'metadata' : metadata
        }
        posts.append(p_data)
        out = (path_site/p_data['url']).relative_to(path_root)
        run_pandoc(p.as_posix(), out, args=pandoc_args)
    return posts

def build_front_page(input_file, output_file, posts):
    with open(path_tmp/"post.yml", 'w', encoding='utf_8') as f:
        f.write(yaml.dump({'posts': posts[::-1]}))

    # build the list of posts
    # shutil.copy(path_root/'index.md', path_tmp/'index.md')
    # use index.md as a template to fill in the posts as metadata
    cost_arg = {
        'template': str(input_file),
        'metadata-file': str(path_tmp/'post.yml')
    }
    run_pandoc(input_file, path_tmp/'index.md', cost_arg)
    # Build the post page.
    run_pandoc(path_tmp/"index.md", output_file, pandoc_args)



pages = list(filter(lambda x: not x.name == 'index.md', path_root.glob('*.md')))

nav_pages = []
for p in pages:
    with open(p, encoding='utf-8') as f:
        metadata, content = frontmatter.parse(f.read())
        if metadata['nav']:
            nav_pages.append(p)

print("Nav pages: {}".format(nav_pages))

nav_items = [{'name' : p.stem.capitalize(),
              'url': p.with_suffix(".html").name } for p in nav_pages]

config['nav-items'] = nav_items
with open(pandoc_args['metadata-file'], 'w', encoding='utf-8') as f:
    f.write(yaml.dump(config))


post_files = path_posts.glob('*.md')
site_posts = path_site / "posts"
site_posts.mkdir(exist_ok=True)
posts = build_posts(post_files)
build_front_page(path_root/"index.md", path_site/"index.html", posts)
print("Build {} post".format(len(posts)))

categories = list_categories(posts)

for p in pages:
    with open(p, encoding='utf_8') as f:
        metadata, content = frontmatter.parse(f.read())
    out = path_site / p.with_suffix(".html").name
    run_pandoc(p.as_posix(), out.as_posix(), args=pandoc_args)

print("Build {} pages".format(len(pages)))

print("Site generated at {}".format(path_site))

sitemap = Sitemap(path_site, config['site-root'])
sitemap.make_sitemap(path_site/'sitemap.xml')
with open(path_site/'robots.txt', 'w') as f:
    f.write("Sitemap: {}/sitemap.xml\n".format(config['site-root']))

print("sitemap.xml and robots.txt generated")

if args.serve:
    print("Reminder this is not a secure http server use only for testing")
    import http.server
    import socketserver
    import os
    os.chdir(path_site)
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT, "\nPress CTRL-C to stop")
        httpd.serve_forever()