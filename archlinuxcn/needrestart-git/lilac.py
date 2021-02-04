#!/usr/bin/env python3

from lilaclib import *
from pathlib import Path

def pre_build():
    aur_pre_build()
    Path('.gitignore').unlink(missing_ok=True)
