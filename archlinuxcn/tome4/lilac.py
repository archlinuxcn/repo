from lilaclib import aur_pre_build, edit_file


def pre_build():
    aur_pre_build('tome4')

    for line in edit_file('PKGBUILD'):
        if line.startswith('makedepends'):
            line = line.replace('glew-git', 'glew')
        print(line)
