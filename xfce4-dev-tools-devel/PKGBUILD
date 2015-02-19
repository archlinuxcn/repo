# Maintainer: twa022 <twa022 at gmail dot com>

_pkgname=xfce4-dev-tools
pkgname=${_pkgname}-devel
pkgver=4.11.1
pkgrel=1
pkgdesc="Xfce developer tools"
arch=('i686' 'x86_64')
url="http://www.xfce.org/"
license=('GPL2')
depends=('gtk-doc' 'automake' 'make' 'intltool' 'pkg-config')
provides=("${_pkgname}=${pkgver}")
conflicts=("${_pkgname}")
source=(http://archive.xfce.org/src/xfce/xfce4-dev-tools/${pkgver%.*}/$_pkgname-$pkgver.tar.bz2
        xfce4-dev-tools-4.10.0-remove-FORTIFY_SOURCE-2.patch)
sha256sums=('21bff408eb48154b3383bde8fb71a6c9359f93e5752b0af284e0af3bf6a56218'
            '4ecfdf8cdb0940ce1044349bdb6646192dffd2b7f4e890f0ef5f00bfdfad7676')

prepare() {
  cd "$srcdir/$_pkgname-$pkgver"

#  patch -Np1 -i "$srcdir/xfce4-dev-tools-4.10.0-remove-FORTIFY_SOURCE-2.patch"
}

build() {
  cd "$srcdir/$_pkgname-$pkgver"

  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib \
    --localstatedir=/var
  make
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
