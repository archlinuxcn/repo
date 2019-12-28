from lilaclib import aur_pre_build, edit_file

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'provides=' in line:
            print(line.replace("'nextcloud'", '"nextcloud=$pkgver"'))
        else:
            print(line)
