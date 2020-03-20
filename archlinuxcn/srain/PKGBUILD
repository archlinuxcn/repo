# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
pkgver=1.0.1
pkgrel=5
pkgdesc="Modern IRC client written in GTK."
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
makedepends=('git' 'make' 'gcc' 'pkg-config' 'gettext' 'python-sphinx')
depends=('glib2' 'gtk3' 'libconfig' 'libsoup' 'libsecret')
optdepends=(
    'glib-networking: TLS connection support'
    )
conflicts=('srain')
provides=('srain')
source=("https://github.com/SrainApp/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('104d0b56944b9eabed9ada7bbca28df4b0dedb972e67fa533079dcf5bde35254')

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
