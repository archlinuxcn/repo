# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=srain
pkgver=1.0.0rc5
pkgrel=1
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
sha256sums=('cf5063c584ad671873aa7f0b6d02bce3082b0adab2618a9588822a5e008ff38e')

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
