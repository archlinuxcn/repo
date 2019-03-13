from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'package(' in line:
            print(line)
            print('	echo "blacklist r8169" | \\')
            print('		install -Dm644 /dev/stdin "$pkgdir/usr/lib/modprobe.d/r8168.conf"')
        else:
            print(line)
