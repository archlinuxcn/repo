#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}]
build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'install -dm755 "$pkgdir/usr/share/locale"' in line:
        print('  install -dm755 -g games "$pkgdir/${instdir}/lang/mo"')
    elif 'LOCALE_DIR="$pkgdir/usr/share/locale" lang/compile_mo.sh' in line:
        print('  LOCALE_DIR="$pkgdir/${instdir}/lang/mo" lang/compile_mo.sh\n')
        print('  install -dm775 -g games "$pkgdir/${instdir}/memorial/"')
    else:
        print(line)

post_build = aur_post_build
if __name__ == '__main__':
    single_main(build_prefix)
