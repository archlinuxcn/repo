# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
pkgver=1.1.1
pkgrel=1
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
makedepends=('python-sphinx')
depends=('gtk3' 'libconfig' 'libsoup' 'libsecret')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('7bbb139517aef047243c2f04e23aff28dc1b83e1d123c331215cf1b6c0f6594f')

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
