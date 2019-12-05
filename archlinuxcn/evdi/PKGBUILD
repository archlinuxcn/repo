# Maintainer: mwawrzyniak
# Contributor: PlusMinus

pkgname=evdi
pkgver=1.6.4
pkgrel=2
pkgdesc="A Linux® kernel module that enables management of multiple screens."
arch=('i686' 'x86_64')
url="https://github.com/DisplayLink/evdi"
license=('GPL')
groups=()
depends=(dkms libdrm)
makedepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=$pkgname.install
changelog=$pkgname.Changelog
source=($pkgname-$pkgver-$pkgrel.tar.gz::https://github.com/DisplayLink/evdi/archive/v$pkgver.tar.gz
        relro.patch
        evdi-1.6.4-kernel-5.4.x.patch)
noextract=()
md5sums=('67d8ab1bb7a4ca013c5435df42ace5dc'
         '05e64dd295a66c030139d0c8f6f7013b'
         '1938ebead0b2c64f11591970a554fffc')

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
