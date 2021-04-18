# Maintainer: Sam L. Yes <samlukeyes123 at gmail dot com>
# Contributor: Andre Klitzing <aklitzing () gmail () com>

pkgname=msitools
pkgver=0.101
pkgrel=2
pkgdesc="Set of programs to inspect and build Windows Installer (.MSI) files"
arch=('i686' 'x86_64')
url="https://wiki.gnome.org/msitools"
license=('LGPL' 'GPL')
depends=('libgsf' 'gcab')
makedepends=('intltool' 'vala' 'meson' 'gobject-introspection')
source=(http://ftp.gnome.org/pub/GNOME/sources/msitools/${pkgver}/${pkgname}-${pkgver}.tar.xz)
sha256sums=('0cc4d2e0d108fa6f2b4085b9a97dd5bc6d9fcadecdd933f2094f86bafdbe85fe')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  arch-meson . build
  ninja -C build
}

check() {
  cd "$srcdir/$pkgname-$pkgver"
  meson test -C build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  DESTDIR="$pkgdir" meson install -C build
  install -Dm644 copyright "$pkgdir/usr/share/licenses/$pkgname/copyright"
}

