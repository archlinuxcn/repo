from lilaclib import aur_pre_build, edit_file


def pre_build():
    aur_pre_build('libblocksruntime',maintainers=['Zrax'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('depends'):
            line = line.replace('depends', 'makedepends')
        print(line)
