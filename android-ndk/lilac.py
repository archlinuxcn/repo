#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
  # delete old source files as they have same names each version
  run_cmd(["rm", "-f", "android-ndk_x86_64.bin", "android-ndk_i686.bin"])
  aur_pre_build()

  remove_lines = ["chmod +x ${pkgname}_$CARCH.bin",
                  "./${pkgname}_$CARCH.bin"]
  first_time = True
  for line in edit_file('PKGBUILD'):
      if line.strip() in remove_lines:
          if first_time:
            print("7z x -y ${pkgname}_$CARCH.bin")
            first_time = False
      else:
          print(line)
          if line.startswith("arch="):
              print("makedepends=('p7zip')")


if __name__ == '__main__':
  single_main(build_prefix)
