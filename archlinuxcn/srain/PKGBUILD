# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
epoch=2
pkgver=1.8.0
pkgrel=1
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
license=('GPL')
url="https://srain.silverrainz.me"
makedepends=('python-sphinx' 'meson')
depends=('gtk3' 'libconfig' 'libsoup3' 'libsecret' 'libayatana-appindicator')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('0c9830c79a3d5656bfe6aaf926f091b09b57eaacbfdc98270c40274fdbd680c2')

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
