# Maintainer: Sam L. Yes <samlukeyes123 at gmail dot com>
# Contributor: Andre Klitzing <aklitzing () gmail () com>

pkgname=msitools
pkgver=0.101
pkgrel=5
pkgdesc="Set of programs to inspect and build Windows Installer (.MSI) files"
arch=('i686' 'x86_64')
url="https://wiki.gnome.org/msitools"
license=('LGPL' 'GPL')
depends=('libgsf' 'gcab')
makedepends=('intltool' 'vala' 'meson' 'gobject-introspection')
source=(https://download.gnome.org/sources/msitools/${pkgver}/${pkgname}-${pkgver}.tar.xz
        $pkgname-glib-2.71.patch::https://gitlab.gnome.org/GNOME/msitools/-/commit/18bc0b2ee79438b8e35c0769165a9a105e3792a0.patch)
sha256sums=('0cc4d2e0d108fa6f2b4085b9a97dd5bc6d9fcadecdd933f2094f86bafdbe85fe'
            '8b33b48e8b5a2cb78ea7e2948b8b6b9d264cd1b12c11d3c7870813d6c6a2569e')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  patch -Np1 -i ../$pkgname-glib-2.71.patch
}

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

  # Workaround an upstream bug that will be fixed in the next release
  chmod +x "$pkgdir/usr/bin/msidiff"
  chmod +x "$pkgdir/usr/bin/msidump"
}

