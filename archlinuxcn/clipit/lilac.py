from lilaclib import aur_pre_build, edit_file

def pre_build():
    aur_pre_build('clipit')

    for line in edit_file('PKGBUILD'):
        if line.startswith('depends'):
            line = line.replace('gtk2', 'gtk3')
        print(line)
