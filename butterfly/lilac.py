# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends = ['python-pyopenssl', 'python-tornado', 'tornado_systemd'],
    depends_setuptools = True,
    optdepends = ['python-libsass'],
    arch = ['any']
  )

def post_build():
  pypi_post_build()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
