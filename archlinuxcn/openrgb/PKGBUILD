# Maintainer: Bo Davidson <bo.davidson@go.tarleton.edu> 
# Contributor: Paul Davis <paul@dangersalad.com>
pkgname=openrgb
pkgver=0.7
pkgrel=4
pkgdesc="Open source RGB lighting control that doesn't depend on manufacturer software."
arch=("x86_64")
url="https://gitlab.com/CalcProgrammer1/OpenRGB"
license=('GPL2')
depends=('qt5-base' 'libusb' 'hidapi' 'mbedtls')
makedepends=('pkgconf')
optdepends=('i2c-tools: Motherboard & RAM access')
source=(
   "https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_$pkgver/OpenRGB-release_$pkgver.tar.gz"
   openrgb.conf
   openrgb.service
)
sha256sums=('6052e04ad736f94a91a386f6cfc0aaff9554fafdabe99cdd46a296fd49132569'
            'b5a53d747422f8b594e3e9615e238457d696732efce94050cdd72182a8645ef2'
            '272dc43a77d0e48d29f32da753c7e05fd635883b173c21047f4eefa8bfc77938')

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
   install -Dm644 -t "$pkgdir"/usr/lib/modules-load.d ../openrgb.conf
   install -Dm644 -t "$pkgdir"/usr/lib/systemd/system ../openrgb.service
}
