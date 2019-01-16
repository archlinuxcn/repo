# Maintainer: mwawrzyniak
# Contributor: PlusMinus

pkgname=evdi
pkgver=1.5.1
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
        force_output.patch
        relro.patch)
noextract=()
md5sums=('20a69bf61aef388019afb283bb03ea29'
         '8ebc776d731166661106b1fb3eeb306c'
         '05e64dd295a66c030139d0c8f6f7013b')
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
