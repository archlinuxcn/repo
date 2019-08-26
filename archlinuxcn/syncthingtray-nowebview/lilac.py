from lilaclib import aur_pre_build, edit_file


def pre_build():
    aur_pre_build('syncthingtray')

    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgname='):
            line = line.replace('syncthingtray', 'syncthingtray-nowebview')
        elif line.startswith('_webview_provider'):
            line = line.replace('webengine', 'none')
        print(line)
