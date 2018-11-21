from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends=['python-attrs', 'python-sortedcontainers', 'python-idna', 'python-async_generator', 'python-outcome', 'python-sniffio'],
    provides=['python-multio-provider'],
    depends_setuptools=False)

def post_build():
  git_pkgbuild_commit()
  update_aur_repo()
