# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
epoch=1
pkgver=1.7.0
pkgrel=1
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
license=('GPL')
url="https://srain.silverrainz.me"
makedepends=('python-sphinx' 'meson')
depends=('gtk3' 'libconfig' 'libsoup' 'libsecret' 'libayatana-appindicator')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('a79bc0d3c257db1c1037b75c330a36c40660580f99327710419a0dacb1b5b18d')

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
