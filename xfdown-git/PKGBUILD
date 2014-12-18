pkgname=xfdown-git
pkgver=70.7bbe604
pkgrel=1
pkgdesc="A python script for QQDownload lixian. Forked from /xfdown."
arch=('any')
url="https://github.com/kikyous/xfdown"
license=('GPL3')
depends=('python2' 'aria2' 'python2-urwid')
makedepends=('git')
source=("git+https://github.com/kikyous/xfdown"
        "xfdown-git.install")
sha256sums=('SKIP'
            'c7d79d1b06714f9c73fc87984f56f41da6e0625976aaa25726869922460b03c2')
install='xfdown-git.install'
_gitname='xfdown'

pkgver() {
    cd $_gitname
    echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {
    cd $_gitname

#    sed -i -r "s|^#!/usr/bin/env python|#!/usr/bin/env python2|" xfdown{,_api}.py

    mkdir -p "$pkgdir/usr/share/$pkgname/"
    cp -r xfdown* "$pkgdir/usr/share/$pkgname/"

    mkdir -p "$pkgdir/usr/bin/"
    ln -sf "/usr/share/$pkgname/xfdown.py" "$pkgdir/usr/bin/xfdown"
}
