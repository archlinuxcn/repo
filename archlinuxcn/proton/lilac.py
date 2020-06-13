from lilaclib import *

def pre_build():
  update_pkgver_and_pkgrel(_G.newver.lstrip('proton-'))
  for line in edit_file('PKGBUILD'):
      if line.startwith('pkgver='):
          line = line.replace("-",".")
      
      print(line)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
