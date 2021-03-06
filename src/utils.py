import subprocess
import shutil
import datetime
from dateutil.parser import parse

def dic2arg_list(x):
    if x:
        args = []

        for arg, val in x.items():
            args.append("--" + arg)
            if val:
                args.append(val)
        return args
    else:
        return []

def run_pandoc(input, output, args=None):
    prog_w_args = ["pandoc", str(input)] + dic2arg_list(args) + ["-o", str(output)]
    p = subprocess.run(prog_w_args)
    p.check_returncode()

def list_categories(posts):
    categories = {}
    for p in posts:
        for c in p['categories']:
            if c not in categories.keys():
                categories[c] = []
            categories[c].append(p)
    return categories

def format_time(time, in_format="%Y-%m-%d %H:M:%S %z", out_format="%d %b %Y"):
    # date = datetime.datetime.strptime(time, in_format)
    date = parse(time)
    return date.strftime(out_format)

def copytree(src, dst):
    """Recursively copy  contents of one src folder to dst with no errors if
    files or directories exists"""
    dst.mkdir(exist_ok=True)
    for f in src.iterdir():
        if f.is_dir():
            newdst = (dst/f.name)
            copytree(f, newdst)
        else:
            shutil.copy2(f, dst)
