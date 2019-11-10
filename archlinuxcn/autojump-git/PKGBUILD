# Maintainer: Cedric Girard <cgirard [dot] archlinux [at] valinor [dot] fr>
# Contributor: Jason Axelson <jason.axelsonATgmail.com>
# Contributor: Sean Escriva <sean.escrivaATgmail.com>
# Contributor: William Ting <william.h.tingATgmail.com>

pkgname=autojump-git
pkgver=22.5.3.r0.g06e082c
pkgrel=1
pkgdesc="A faster way to navigate your filesystem from the command line"
arch=(any)
url="http://github.com/wting/autojump"
license=('GPL3')
depends=('python')
makedepends=('git')
conflicts=('autojump')
provides=('autojump')
replaces=()
backup=()
source=('git+https://github.com/wting/autojump.git')
md5sums=('SKIP')

_gitname="autojump"

pkgver() {
    cd ${_gitname}
    git describe --long --tags | sed 's/^release\-v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    cd ${_gitname}
    sed -i 's$#!/usr/bin/env python$#!/usr/bin/env python3$' bin/autojump bin/*.py
}

package() {
    cd ${_gitname}
    ./install.py --prefix 'usr/' --destdir "${pkgdir}" --zshshare 'usr/share/zsh/site-functions'

    cd "${pkgdir}"/usr/share/$_gitname
    for i in $_gitname.* ; do
        ln -s /usr/share/$_gitname/$i \
            "${pkgdir}"/etc/profile.d/$i
    done

    #https://github.com/joelthelion/autojump/pull/339
    sed -i "s!/usr/local/!/usr/!g" "${pkgdir}"/etc/profile.d/$_gitname.sh
    #FS#43762
    sed -i '27,31d' "${pkgdir}"/etc/profile.d/$_gitname.sh
}


# vim:set ts=4 sw=4 et:
