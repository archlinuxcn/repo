from lilaclib import aur_pre_build, edit_file


def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'groups=' in line:
            continue
        print(line)
