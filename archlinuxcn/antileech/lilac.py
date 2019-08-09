from lilaclib import add_makedepends, aur_pre_build, edit_file


def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        # makechrootpkg has a bug - if a package that creates user(s) is fed
        # via -I, makepkg in the chroot fails to run as the newly created user
        # might have the same UID (1000) as builduser, and thus the NOPASSWD
        # line for builduser in /etc/sudoers has no effects.
        if line.startswith('depends='):
            line = line.replace('amule-dlp', 'wxgtk')
        print(line)
    add_makedepends(['git'])
