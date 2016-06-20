# Maintainer: revel <revelΘmuub·net>

pkgname=cuda_memtest
pkgver=1.2.3
pkgrel=2
pkgdesc="A GPU memory test utility for NVIDIA and AMD GPUs. OpenCL version."
arch=('i686' 'x86_64')
url="http://cudagpumemtest.sourceforge.net/"
license=('Illinois Open Source License')
depends=('libcl')
optdepends=('opencl-nvidia: OpenCL implemention for NVIDIA'
	    'opencl-catalyst: AMD/ATI drivers. OpenCL implemention for AMD Catalyst'
	    'opencl-mesa: OpenCL support for AMD/ATI Radeon mesa drivers')
makedepends=('opencl-headers')
source=("http://downloads.sourceforge.net/project/cudagpumemtest/$pkgname-$pkgver.tar.gz"
	'path.patch')
md5sums=('b81b80fa5d16e7b64a01d3e8b142b62a'
         '6a591ecced8b512adf7fecfdf277b363')
sha256sums=('f0afac0b9df60de6da91cd0f76691879f745bf46821946021e9e1fc162596ad7'
            '25b80161f63b61562015e8c89d1f4ff77b2d1d9140f879d7e29cf3ad7447cbca')

prepare() {
  cd "$pkgname-$pkgver"
  patch -p1 -i ../path.patch
}

build() {
  cd "$pkgname-$pkgver"
  CPPFLAGS="-std=gnu++98 $CPPFLAGS"
  make ocl_memtest
}

package() {
  cd "$pkgname-$pkgver"
  install -d "$pkgdir/usr/bin/"
  install ocl_memtest "$pkgdir/usr/bin/"
  install -d "$pkgdir/usr/share/$pkgname/"
  install -m644 ocl_memtest_kernels.cpp "$pkgdir/usr/share/$pkgname/"
}
