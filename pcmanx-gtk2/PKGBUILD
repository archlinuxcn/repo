# Maintainer: Shinlun Hsieh <yngwiexx@yahoo.com.tw>
# Contributor: Yenting Chen <coolcyt@gmail.com>
# Contributor: Lyman Li <lymanrb@gmail.com>

pkgname=pcmanx-gtk2
pkgver=1.3
pkgrel=1
pkgdesc="A gtk+ based free BBS client"
arch=('i686' 'x86_64')
url="https://github.com/pcman-bbs/pcmanx"
license=('GPL')
depends=('gtk2' 'libltdl')
optdepends=('wget')
makedepends=('autoconf' 'automake' 'intltool' 'pkg-config')
options=('!libtool')
source=(https://github.com/pcman-bbs/pcmanx/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.xz
    pcmanx.install)
md5sums=('9796c55ca5df674251be713a5019e3bc'
    '6374916400684c2db957be0250a4ca98')
install=pcmanx.install

build() {
    cd ${srcdir}/${pkgname}-${pkgver}
    ./configure --prefix=/usr --enable-wget --enable-iplookup || return 1
    make || return 1
}

package() {
    cd ${srcdir}/${pkgname}-${pkgver}
    make DESTDIR=${pkgdir} install || return 1
}
