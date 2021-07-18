# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
epoch=1
pkgver=1.2.3
pkgrel=1
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
makedepends=('python-sphinx' 'meson')
depends=('gtk3' 'libconfig' 'libsoup' 'libsecret')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('9a02f469ba1e3b977d6b432985809f7cd61f52410b65cff44be9ff4ae90cf0f5')

_prefix='/usr'

build() {
    cd ${pkgname}-${pkgver}

    meson setup                         \
        --prefix="${_prefix}"           \
        --datadir="${_prefix}/share"    \
        --sysconfdir="/etc"             \
        --buildtype=release             \
        builddir
    ninja -C builddir
}

package() {
    cd ${pkgname}-${pkgver}

    DESTDIR="${pkgdir}" ninja -C builddir install
}
