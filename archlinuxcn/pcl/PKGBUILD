# Maintainer: Benjamin Chrétien <chretien dot b plus aur at gmail dot com>
# Contributor: Fabio Loli <loli_fabio@protonmail.com>
# Contributor: Yuxin Wu <ppwwyyxxc@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: hauptmech
# Contributor: figo.zhang
# Contributor: lubosz
# Contributor: ZiXiS

pkgname=pcl
pkgver=1.11.0
pkgrel=1
pkgdesc="A comprehensive open source library for n-D Point Clouds and 3D geometry processing"
arch=('x86_64' 'i686')
url='http://www.pointclouds.org'
license=('BSD')
depends=('boost' 'eigen' 'flann' 'vtk' 'qhull' 'qt5-base' 'glu' 'qt5-webkit'
  'openmpi' 'python' 'libxt' 'libharu' 'proj' 'glew' 'netcdf' 'libusb')
makedepends=('cmake' 'gl2ps' 'python')
optdepends=('cuda' 'openni2' 'python-sphinx')
source=("pcl-${pkgver}.tar.gz"::"https://github.com/PointCloudLibrary/pcl/archive/pcl-${pkgver}.tar.gz")

sha256sums=('4255c3d3572e9774b5a1dccc235711b7a723197b79430ef539c2044e9ce65954' )

build() {
 # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  cmake ${srcdir}/pcl-pcl-${pkgver} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_surface_on_nurbs=ON \
    -DCUDA_HOST_COMPILER=/usr/bin/gcc

#  cd "${srcdir}/pcl-pcl-${pkgver}/build"
  make -j8
}

package() {
  cd "${srcdir}/build"
  make DESTDIR=${pkgdir} install

  install -Dm644 ${srcdir}/pcl-pcl-${pkgver}/LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
