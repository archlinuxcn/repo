# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
epoch=1
pkgver=1.3.1
pkgrel=1
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
makedepends=('python-sphinx' 'meson')
depends=('gtk3' 'libconfig' 'libsoup' 'libsecret')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('30a2e9958084a83e3841b6d5730052fb76e80b32f4499aecc0b822c4a650bdd5')

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
