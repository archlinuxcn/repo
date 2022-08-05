from lilaclib import aur_pre_build, edit_file

def pre_build():
    aur_pre_build('pcem',maintainers=['njensen20'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('depends'):
            line = line.replace('wxgtk2', 'wxgtk3')
        print(line)
