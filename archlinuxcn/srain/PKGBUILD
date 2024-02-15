# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
epoch=1
pkgver=1.6.0
pkgrel=1
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
license=('GPL')
url="https://srain.silverrainz.me"
makedepends=('python-sphinx' 'meson')
depends=('gtk3' 'libconfig' 'libsoup' 'libsecret' 'libayatana-appindicator')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('d7be6bf0def5c5bc4416056fc3e380da8b6383e600e529191b3a9f185c0a511b')

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
