from lilaclib import aur_pre_build, aur_post_build, edit_file

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        # Work-around https://aur.archlinux.org/packages/lxqt-build-tools-git#comment-959565
        line = line.replace("'qt5-base'", "'qt6-base'")
        print(line)

def post_build():
    aur_post_build()
