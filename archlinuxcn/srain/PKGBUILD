# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
epoch=1
pkgver=1.3.2
pkgrel=1
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
makedepends=('python-sphinx' 'meson')
depends=('gtk3' 'libconfig' 'libsoup' 'libsecret')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('a9e0a6d36e57c091236f9a4aaddb255173411a8532499658fa6e464d40ebb665')

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
