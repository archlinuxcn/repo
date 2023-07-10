# Maintainer: Bo Davidson <bo.davidson@go.tarleton.edu> 
# Contributor: Paul Davis <paul@dangersalad.com>
pkgname=openrgb
pkgver=0.9
pkgrel=1
pkgdesc="Open source RGB lighting control that doesn't depend on manufacturer software."
arch=("x86_64")
url="https://gitlab.com/CalcProgrammer1/OpenRGB"
license=('GPL2')
depends=('qt5-base' 'libusb' 'hidapi' 'mbedtls2')
makedepends=('pkgconf' 'qt5-tools') # now need lrelease in qt5-tools for successful build >=v0.8
optdepends=('i2c-tools: Motherboard & RAM access')

# Using Link Time Optimization can cause segment fault at runtime. Disabled until upstream fix
# https://gitlab.com/CalcProgrammer1/OpenRGB/-/commit/8e6e5c1becdd610cd9206bbdcf5616ce4b43e0f1
# https://gitlab.com/CalcProgrammer1/OpenRGB/-/merge_requests/668

# Expect a lot of '-pipe ignored' warnings on build if it's in makepkg.conf. This is benign. 
options=('!lto')
source=(
   "https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_$pkgver/OpenRGB-release_$pkgver.tar.gz"
   openrgb.conf
   openrgb.service
)
sha256sums=('2e62799339b72b6d3afc4792e6ff39487583210bb5ddde93e2daa38ae35381c2'
            'b5a53d747422f8b594e3e9615e238457d696732efce94050cdd72182a8645ef2'
            '272dc43a77d0e48d29f32da753c7e05fd635883b173c21047f4eefa8bfc77938')

prepare() {
   # Searches and applies any .patch file included this git repo 
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
   export CXXFLAGS=${CXXFLAGS/-pipe}
   export LDFLAGS="$LDFLAGS -L/usr/lib/mbedtls2" # props to AndyRTR for linking to mbedtls2 fix

   cd "$srcdir/OpenRGB-release_$pkgver"
   sed -i 's|rules.path=/lib|rules.path=/usr/lib|g' OpenRGB.pro
   qmake INCLUDEPATH+="/usr/include/mbedtls2" OpenRGB.pro
   make 
}

package() {
   cd "$srcdir/OpenRGB-release_$pkgver"
   make INSTALL_ROOT="$pkgdir" install
   install -Dm644 -t "$pkgdir"/usr/lib/modules-load.d ../openrgb.conf
   install -Dm644 -t "$pkgdir"/usr/lib/systemd/system ../openrgb.service
}
