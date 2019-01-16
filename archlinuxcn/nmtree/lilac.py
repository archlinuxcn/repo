from lilaclib import aur_pre_build, edit_file


def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        print(line)
        if 'makedepends' in line:
            # https://bugs.square-r00t.net/index.php?do=details&task_id=47
            print("options+=('!makeflags')")
