# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
pkgver=1.0.0rc4
pkgrel=1
pkgdesc="Modern IRC client, git version"
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
sha256sums=('8630164ccdf89fa88a3a08a3373f14f9440704fa3b4e23977a72c90dd3ac3fb3')

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
