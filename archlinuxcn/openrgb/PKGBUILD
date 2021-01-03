# Maintainer: Bo Davidson <a3JvemFyZXFAZ21haWwuY29tCg== | base64 -d>
# Contributor: Paul Davis <paul@dangersalad.com>
pkgname=openrgb
pkgver=0.5
pkgrel=5
pkgdesc="Open source RGB lighting control that doesn't depend on manufacturer software."
arch=("x86_64")
url="https://gitlab.com/CalcProgrammer1/OpenRGB"
license=('GPL2')
depends=('qt5-base' 'libusb' 'hidapi')
makedepends=('pkgconf')
optdepends=('i2c-tools: Motherboard & RAM access')
conflicts=('openrgb-git')
source=(
   "https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_$pkgver/OpenRGB-release_$pkgver.tar.gz"
   hidapifix.patch # https://gitlab.com/CalcProgrammer1/OpenRGB/-/issues/924
)
sha256sums=(
   'e227dedfe0c3aa8f3bcb0c4149aa5feb1db4b0429a151423d74c0103c55d7d26'
   'eeaed61a7bdbfa98cd9aaa6ea8a55df3eb092bc1f02ba047dd73cf75d1578b88'
)

prepare() {
   cd "$srcdir/OpenRGB-release_$pkgver"
   local src
   for src in "${source[@]}"; do
      src="${src%%::*}"
      src="${src##*/}"
      [[ $src = *.patch ]] || continue
      echo "Applying patch $src..."
      patch -Np1 < "../$src"
   done
}


build() {
   cd "$srcdir/OpenRGB-release_$pkgver"
   sed -i 's|rules.path=/lib|rules.path=/usr/lib|g' OpenRGB.pro
   qmake OpenRGB.pro
   make 
}

package() {
   cd "$srcdir/OpenRGB-release_$pkgver"
   make INSTALL_ROOT="$pkgdir" install
}
