from lilaclib import *

build_prefix = 'extra-x86_64'

def _get_new_version():
  web = s.get('https://www.giss.nasa.gov/tools/panoply/download/')
  return re.search(r'\d\.\d\.\d', web.text).group()

def pre_build():
  update_pkgver_and_pkgrel(_G.newver.lstrip('v'))

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
#  update_aur_repo()

if __name__ == '__main__':
  single_main()
