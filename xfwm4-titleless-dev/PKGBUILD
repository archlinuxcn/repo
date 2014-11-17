# $Id$
# Maintainer: Cedric Leporcq <cedric at gmail dot com>

pkgname=xfwm4-titleless-dev
_pkgname=${pkgname%%-*}
pkgver=4.11.4
pkgrel=2
pkgdesc="Xfce window manager with hide title on maximized features, corner tiling and fixes"
arch=('i686' 'x86_64')
url="https://github.com/cedl38/xfwm4-titleless"
license=('GPL2')
groups=('xfce4')
depends=('libxfce4ui>=4.11.0' 'libwnck' 'hicolor-icon-theme')
optdepends=('xfce4-windowck-plugin: to put the maximized window title on the panel.')
makedepends=('intltool' 'xfce4-dev-tools' 'exo')
provides=("xfwm4=${pkgver}")
conflicts=('xfwm4')
options=('!libtool')
install=xfwm4.install
source=("${pkgname}-$pkgver.tar.gz::https://github.com/cedl38/${_pkgname}/archive/v${pkgver}-t.tar.gz")
sha256sums=('eec6ea3ae08e064fa875aa9a36bfd304a5eabe8735e1dbe8b21a11ed81501f3e')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}-t"

    ./autogen.sh \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib \
    --localstatedir=/var \
    --disable-static \
    --enable-startup-notification \
    --enable-randr \
    --enable-compositor \
    --enable-xsync \
    --enable-debug=minimal

  make
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}-t"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
