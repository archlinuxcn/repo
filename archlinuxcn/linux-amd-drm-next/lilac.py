from lilaclib import *

def pre_build():
  newver = _G.newver.removeprefix('amd-drm-fixes-')

  for line in edit_file('PKGBUILD'):
      if line.startswith('_tag'):
          line = "_tag='amd-drm-fixes-" + newver + "'"
      print(line)
  newver2 = newver.replace("-",".")
  update_pkgver_and_pkgrel(newver2)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
