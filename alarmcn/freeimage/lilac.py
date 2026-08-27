from lilaclib import *


def pre_build():
  aur_pre_build(maintainers=['andreas_baumann'])
  add_arch(['aarch64'])

  in_build = False
  has_pic_flags = False
  for line in edit_file('PKGBUILD'):
    if line == 'build() {':
      in_build = True
    elif in_build and line == "  CFLAGS+=' -fPIC'":
      has_pic_flags = True
    elif in_build and line == '  cd FreeImage':
      if not has_pic_flags:
        print("  CFLAGS+=' -fPIC'")
        print("  CXXFLAGS+=' -fPIC'")
        print()
      in_build = False
    print(line)
