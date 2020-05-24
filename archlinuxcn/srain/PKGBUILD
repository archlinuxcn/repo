# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
pkgver=1.1.0
pkgrel=1
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
makedepends=('python-sphinx')
depends=('gtk3' 'libconfig' 'libsoup' 'libsecret')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('cba8bf195933669c36d712c358504a0da271f65e36ff768c3ca7eb4172a54023')

_prefix='/usr'

build() {
    cd ${pkgname}-${pkgver}

    ./configure                         \
        --prefix="${_prefix}"           \
        --datadir="${_prefix}/share"    \
        --sysconfdir="/etc"             \
        --disable-debug
    make
    make doc
}

package() {
    cd ${pkgname}-${pkgver}

    make DESTDIR="${pkgdir}" install
    make DESTDIR="${pkgdir}" install-doc
}
