# Maintainer: Bo Davidson <bo.davidson@go.tarleton.edu> 
# Contributor: Paul Davis <paul@dangersalad.com>
pkgname=openrgb
pkgver=0.6
pkgrel=2
pkgdesc="Open source RGB lighting control that doesn't depend on manufacturer software."
arch=("x86_64")
url="https://gitlab.com/CalcProgrammer1/OpenRGB"
license=('GPL2')
depends=('qt5-base' 'libusb' 'hidapi')
makedepends=('pkgconf')
optdepends=('i2c-tools: Motherboard & RAM access')
source=(
   "https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_$pkgver/OpenRGB-release_$pkgver.tar.gz"
   openrgb.conf
   openrgb.service
   openrgb.desktop
   09e5243-g502detectionfix.patch
   ae88771-g502pidfix.patch
)
sha256sums=(
   'cfcec232550d0c4d00e87b91ba501ca248a07e3b50a07c50d0c0af37dc03dffa'
   'b5a53d747422f8b594e3e9615e238457d696732efce94050cdd72182a8645ef2'
   'd5e61b52d8f753a0500ed2cb951362fee637611a9cae8d59f06f1bf72bc9999f'
   '2f96f6bcb381490dae7132b9533045dd46db8a0fc9f9ab5d00d952545800c6fc'
   '7dc3f07409ff52efdf836d277be9d8bd68093980f0f6f14bed6f1718c31224cf'
   '80baad74c9f5f6109ec6e1179737e85ef93395b8647e2e7efeb29671c26e2701'
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
   install -Dm644 -t "$pkgdir"/usr/lib/modules-load.d ../openrgb.conf
   install -Dm644 -t "$pkgdir"/usr/lib/systemd/system ../openrgb.service
}
