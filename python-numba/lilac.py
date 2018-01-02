from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'
post_build = aur_post_build

depends = ['python-llvmlite']

def pre_build():
  aur_pre_build()
  for l in edit_file('PKGBUILD'):
    if l.lstrip().startswith('depends='):
      l = l.rstrip(' )')
      l += " 'python-numpy')"
    print(l)

if __name__ == '__main__':
  single_main(build_prefix)
