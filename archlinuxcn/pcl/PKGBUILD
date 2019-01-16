# Maintainer: Benjamin Chrétien <chretien dot b plus aur at gmail dot com>
# Contributor: Fabio Loli <loli_fabio@protonmail.com>
# Contributor: Yuxin Wu <ppwwyyxxc@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: hauptmech
# Contributor: figo.zhang
# Contributor: lubosz
# Contributor: ZiXiS

pkgname=pcl
pkgver=1.8.1
pkgrel=8
pkgdesc="A comprehensive open source library for n-D Point Clouds and 3D geometry processing"
arch=('x86_64' 'i686')
url='http://www.pointclouds.org'
license=('BSD')
depends=('boost' 'eigen' 'flann' 'vtk' 'qhull' 'qt5-base' 'glu' 'qt5-webkit'
  'openmpi' 'python2' 'libxt' 'libharu' 'proj' 'glew' 'netcdf')
makedepends=('cmake' 'gl2ps' 'python')
optdepends=('cuda' 'openni2' 'python2-sphinx')
source=("pcl-${pkgver}.tar.gz"::"https://github.com/PointCloudLibrary/pcl/archive/pcl-${pkgver}.tar.gz" 
        "https://github.com/PointCloudLibrary/pcl/commit/f527e5819d6a4d0e8ed46658032975b73d617f60.patch"
        "https://github.com/jspricke/pcl/commit/7e0c0eba0bc6917592bb7f0db88dde48c168d24a.patch"
        "https://github.com/PointCloudLibrary/pcl/commit/b588c546e8e78bfdd238f0f943236257549107dd.patch"
        "https://github.com/PointCloudLibrary/pcl/commit/491b7c7e12ce39c59fb1f22718812a02e7f58065.patch"
        "https://github.com/PointCloudLibrary/pcl/commit/b9503084d1c63b02d16b03fe318e3c9b2cb36244.patch"
        )
sha256sums=('5a102a2fbe2ba77c775bf92c4a5d2e3d8170be53a68c3a76cfc72434ff7b9783' 
            '6d48d5665e393c8f5ef3d8f2ead0c903a5cb63dff0c9aed32975bfb96ab843f2'
            '501c8da24841eeb6cdf84805841a751b162f7c94b6afe2513a636320e83dd5b7'
            '78610e04b7119a23b8841c656caaa41a28ab26d4820ee1f9616d7abf107fde9f'
            'de2c2dbff2ce41f6fd8bc8b99551182bbada23854065211be91b7a957bdac489'
            '18e88f0796713e0defd7b719ec8777aab4fc4c4c98a48bd3f00e161224d93f54'
            )

prepare() {
  cd "${srcdir}/pcl-pcl-${pkgver}"

  # Patch to support boost 1.5.6:
  # 1. Api change. See http://www.pcl-users.org/PCL-compilation-errors-Please-help-me-td4035209.html
  # This patch is not necessary for now.
  # sed -i "s/boost::property_tree::xml_writer_settings.*/boost::property_tree::xml_writer_settings<std::string> settings = boost::property_tree::xml_writer_make_settings<std::string>('\\\t', 1);/g" io/src/lzf_image_io.cpp
  # 2. Qt moc parser fails on some boost headers files. Try to get around.
  grep -rl '#include <boost/date_time/posix_time/posix_time.hpp>' . \
    | xargs sed -i "s/#include <boost.*posix_time.hpp>/#ifndef Q_MOC_RUN\n\r#include <boost\\/date_time\\/posix_time\\/posix_time.hpp>\n\r#endif/g"

  # Fix the issue about pcl_feature that cannot be used through pkgconfig due to missing pcl_2d-1.8.pc
  # (see https://github.com/PointCloudLibrary/pcl/issues/1978)
  # Patch that was merged into master : https://github.com/PointCloudLibrary/pcl/pull/1979
  patch -Np1 -i ${srcdir}/f527e5819d6a4d0e8ed46658032975b73d617f60.patch
  patch -Np1 -i ${srcdir}/7e0c0eba0bc6917592bb7f0db88dde48c168d24a.patch
  patch -Np1 -i ${srcdir}/b588c546e8e78bfdd238f0f943236257549107dd.patch
  patch -Np1 -i ${srcdir}/491b7c7e12ce39c59fb1f22718812a02e7f58065.patch
  patch -Np1 -i ${srcdir}/b9503084d1c63b02d16b03fe318e3c9b2cb36244.patch
  
  # [[ -d build ]] && rm -r build
}

build() {
# [[ -d build ]] && rm -r build
#  mkdir -p build && cd build
 # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  cmake ${srcdir}/pcl-pcl-${pkgver} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCUDA_HOST_COMPILER=/usr/bin/gcc

#  cd "${srcdir}/pcl-pcl-${pkgver}/build"
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR=${pkgdir} install

  install -Dm644 ${srcdir}/pcl-pcl-${pkgver}/LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
