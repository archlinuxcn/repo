# Maintainer: Jeremy Kescher <jeremy@kescher.at>
# Contributor: Benjamin Maisonnas <ben@wainei.net>
# Contributor: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: Rebin Silva <rebinsilva@gmail.com>
# Contributor: heavysink <heavysink at gmail>

pkgname=vkd3d-valve
pkgver=1.1
pkgrel=2
pkgdesc="D3D12 to Vulkan translation library (Valve version)"
arch=('x86_64')
url='https://github.com/ValveSoftware/vkd3d'
license=('LGPL')
depends=('spirv-tools'
         'vulkan-icd-loader'
         'libxcb'
         )
makedepends=( # Prevent out-of-date SPIRV headers error
             'spirv-headers'
             'vulkan-headers'
             'xcb-proto'
             'wine'
            )
conflicts=('vkd3d')
provides=('vkd3d')
source=("https://github.com/ValveSoftware/vkd3d/archive/vkd3d-$pkgver.tar.gz")
sha256sums=('da223b0ec80570c096317d15c0d29deda8fcf571a539a83eb4e33c5a97c226bb')

prepare() {
    cd vkd3d-vkd3d-$pkgver

    sed -i '/#define VKD3D_MAX_SHADER_STAGES     5u/a #define VKD3D_PIPELINE_BIND_POINT_COUNT 2u' libs/vkd3d/vkd3d_private.h
    sed -i 's/VK_PIPELINE_BIND_POINT_RANGE_SIZE/VKD3D_PIPELINE_BIND_POINT_COUNT/g' libs/vkd3d/vkd3d_private.h 
}
build() {
  cd vkd3d-vkd3d-$pkgver

  ./autogen.sh
  ./configure \
    --prefix=/usr \
    --with-spirv-tools \
    --disable-tests

  make
}

package() {
  cd vkd3d-vkd3d-$pkgver
  make DESTDIR="${pkgdir}" install
}
