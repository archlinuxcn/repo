# Maintainer: Steven Honeyman <stevenhoneyman at gmail com>
# Maintainer: Maxim Fomin <maxim at fomin one>

pkgname=wxhexeditor
pkgver=0.24
pkgrel=4
pkgdesc="A free hex editor / disk editor for Linux, Windows and MacOSX"
arch=('i686' 'x86_64')
url="http://www.wxhexeditor.org"
license=('GPL2')
depends=('wxgtk3')
makedepends=('python')
optdepends=('gksu: For root access support'
            'polkit: For root access support')
source=("https://github.com/EUA/wxHexEditor/archive/v$pkgver.tar.gz"
        "01-add-pkexec-support.patch"
        "02-remove-strange-output.patch")
md5sums=('1b77bddc026e22797fd0e7a82e52cd28'
         'e62ae9e6b0aac2afdcc41b51cab39272'
         '9f8f2ea86c7cc1d4706ac8c4862cfb51')
         
prepare() {
    cd "$srcdir/wxHexEditor-$pkgver"
    patch -Np1 -i "${srcdir}/01-add-pkexec-support.patch"
    patch -Np1 -i "${srcdir}/02-remove-strange-output.patch"
}

build() {
    cd "$srcdir/wxHexEditor-$pkgver"
    make WXCONFIG="/usr/bin/wx-config-gtk3"
}

package() {
    cd "$srcdir/wxHexEditor-$pkgver"
    make WXCONFIG="/usr/bin/wx-config-gtk3" DESTDIR="$pkgdir" PREFIX="/usr" install
}
