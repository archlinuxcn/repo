# Maintainer: Petron <petron@archlinuxcn.org>
pkgname=pinyin-completion
pkgver=34.68173f0
pkgrel=1
pkgdesc="complete path name based upon the pinyin acronym of Chinese characters"
arch=('any')
url="https://github.com/petronny/pinyin-completion"
license=('GPL3')
depends=('python2')
makedepends=('git')
source=("git+https://github.com/petronny/pinyin-completion"
        "pinyin-completion.install")
sha256sums=('SKIP'
            'f6dbcc8fc15c6de71897281f1d64f05df7dfd1e5ec3b1a70bd46a4f3078f9f13')
install='pinyin-completion.install'

pkgver() {
    cd $pkgname
    echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
    cd "$srcdir/$pkgname/tools"
    python2 table-generator.py > ../pinyin/pinyin_initial.py
}

package() {
    cd $pkgname

    mkdir -p "$pkgdir/usr/share/$pkgname/"
    cp -r shell "$pkgdir/usr/share/$pkgname/"
    cp -r tools "$pkgdir/usr/share/$pkgname/"

    python2 setup.py install --root=$pkgdir/ --optimize=1
}
