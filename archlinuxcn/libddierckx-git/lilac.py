# Trimmed lilac.py
from lilaclib import *

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
