# Maintainer: mwawrzyniak <arch at cmstactical dot net>
# Contributor: PlusMinus

pkgname=evdi
pkgver=1.8.0
pkgrel=1
pkgdesc="A Linux® kernel module that enables management of multiple screens."
arch=('i686' 'x86_64')
url="https://github.com/DisplayLink/evdi"
license=('GPL')
groups=()
depends=(glibc dkms libdrm)
makedepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=$pkgname.install
changelog=$pkgname.Changelog
source=($pkgname-$pkgver-$pkgrel.tar.gz::https://github.com/DisplayLink/evdi/archive/v$pkgver.tar.gz)
noextract=()
md5sums=('dd48011aa9118a611b7a1bb9cd2fe04b')

prepare() {
  cd "$pkgname-$pkgver"
  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    [[ $src = *.patch ]] || continue
    patch -Np1 < "../$src"
  done
}

build() {
# We only need to build the library in this step, dkms will build the module
cd "$pkgname-$pkgver/library"

make
}

package() {
# Predfine some target folders
SRCDIR="$pkgdir/usr/src/$pkgname-$pkgver"	# This one is needed for dkms
LIBNAME=lib$pkgname

cd "$pkgname-$pkgver"

install -D -m 755 library/$LIBNAME.so $pkgdir/usr/lib/$LIBNAME.so

install -d $SRCDIR
install -D -m 755 module/* $SRCDIR
}
