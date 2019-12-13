# Maintainer: Benjamin Chrétien <chretien dot b plus aur at gmail dot com>
# Contributor: Fabio Loli <loli_fabio@protonmail.com>
# Contributor: Yuxin Wu <ppwwyyxxc@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: hauptmech
# Contributor: figo.zhang
# Contributor: lubosz
# Contributor: ZiXiS

pkgname=pcl
pkgver=1.9.1
pkgrel=3
pkgdesc="A comprehensive open source library for n-D Point Clouds and 3D geometry processing"
arch=('x86_64' 'i686')
url='http://www.pointclouds.org'
license=('BSD')
depends=('boost' 'eigen' 'flann' 'vtk' 'qhull' 'qt5-base' 'glu' 'qt5-webkit'
  'openmpi' 'python' 'libxt' 'libharu' 'proj' 'glew' 'netcdf' 'libusb')
makedepends=('cmake' 'gl2ps' 'python')
optdepends=('cuda' 'openni2' 'python2-sphinx')
source=("pcl-${pkgver}.tar.gz"::"https://github.com/PointCloudLibrary/pcl/archive/pcl-${pkgver}.tar.gz"
        "https://github.com/PointCloudLibrary/pcl/commit/dbadf4143bdc503203da0d87a786752a60d29e76.patch"
        "https://github.com/PointCloudLibrary/pcl/commit/9f7a246f962aa26740b8ded6f45e8a8ae944d588.patch")

sha256sums=('0add34d53cd27f8c468a59b8e931a636ad3174b60581c0387abb98a9fc9cddb6' 
            '1336a5f376ee1791bde5167ff9507883a9c167f04e0e776a1d884c98fd0db12d'
            'd046674b4217a19d61a69ef6fe7f1476eae33216a2bee5d27feaa02b916e29af')

prepare() {
  cd ${srcdir}/pcl-pcl-${pkgver}
  patch -Np1 -i "${srcdir}/9f7a246f962aa26740b8ded6f45e8a8ae944d588.patch"
  patch -Np1 -i "${srcdir}/dbadf4143bdc503203da0d87a786752a60d29e76.patch"
}


build() {
 # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  cmake ${srcdir}/pcl-pcl-${pkgver} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCUDA_HOST_COMPILER=/usr/bin/gcc

#  cd "${srcdir}/pcl-pcl-${pkgver}/build"
  make -j2
}

package() {
  cd "${srcdir}/build"
  make DESTDIR=${pkgdir} install

  install -Dm644 ${srcdir}/pcl-pcl-${pkgver}/LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
