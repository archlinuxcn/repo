# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=InsightToolkit
pkgname=itk
_pkgver=5.0.1
pkgver=5.0.1
pkgrel=2
pkgdesc='An open-source, cross-platform library that provides developers with an extensive suite of software tools for image analysis'
arch=('x86_64')
url='https://itk.org/'
license=('Apache')
depends=(
  'dcmtk'
  'double-conversion'
  'eigen'
  'expat'
  'fftw'
  'hdf5'
  'intel-tbb'
  'libjpeg'
  'libpng'
  'libtiff'
  'opencv'
  'openslide'
  'python-numpy'
  'python-xarray'
  'vtk'
  'zlib'
)
makedepends=(
  'ocl-icd'
  'opencl-headers'
  'cmake'
  'git'
  'gtest'
  'python-setuptools'
  'swig'
)
provides=(insighttoolkit=${pkgver} insight-toolkit=${pkgver} python-itk=${pkgver})
conflicts=(insighttoolkit insight-toolkit python-itk)
source=("https://github.com/InsightSoftwareConsortium/ITK/releases/download/v${pkgver}/InsightToolkit-${pkgver}.tar.gz"
"https://github.com/InsightSoftwareConsortium/ITK/releases/download/v${pkgver}/InsightData-${pkgver}.tar.gz")
sha512sums=('f36613ff72c513ded3d32504f71308a94fe75555cf9fd22b77485d1375601f6e1f1539cc5ac82a9e1e229bcf514a88ccb55122a7dfc74a6ae1b6604aa70bd814'
            'eb766c115049949937d6527937f1f49ef84304a71dc4924581a53173f45c4e5a0c5a0e180550e75ecd840314609580b9d1fe9b2358c5a87c82a2c6aff8e9f50e')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cmake_opts=(
    -DBUILD_EXAMPLES:BOOL=OFF
    -DBUILD_SHARED_LIBS:BOOL=ON
    -DBUILD_TESTING:BOOL=ON
    -DCMAKE_INSTALL_LIBDIR:PATH=lib
    -DCMAKE_INSTALL_PREFIX:PATH=/usr
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
    -DITK_LEGACY_REMOVE:BOOL=ON
    -DITK_USE_64BITS_IDS_DEFAULT:BOOL=ON
    -DITK_USE_SYSTEM_DOUBLECONVERSION:BOOL=ON
    -DITK_USE_SYSTEM_EIGEN:BOOL=ON
    -DITK_USE_SYSTEM_EXPAT:BOOL=ON
    -DITK_USE_SYSTEM_GOOGLETEST:BOOL=ON
    -DITK_USE_SYSTEM_HDF5:BOOL=ON
    -DITK_USE_SYSTEM_JPEG:BOOL=ON
    -DITK_USE_SYSTEM_PNG:BOOL=ON
    -DITK_USE_SYSTEM_TIFF:BOOL=ON
    -DITK_USE_SYSTEM_ZLIB:BOOL=ON
    -DITK_WRAP_PYTHON:BOOL=ON
    -DITK_BUILD_DEFAULT_MODULES:BOOL=OFF
    -DITKGroup_Bridge:BOOL=ON
    -DITKGroup_Compatibility:BOOL=ON
    -DITKGroup_Core:BOOL=ON
    -DITKGroup_Filtering:BOOL=ON
    -DITKGroup_IO:BOOL=ON
    -DITKGroup_Nonunit:BOOL=ON
    -DITKGroup_Numerics:BOOL=ON
    -DITKGroup_Registration:BOOL=ON
    -DITKGroup_Remote:BOOL=ON
    -DITKGroup_Segmentation:BOOL=ON
    -DITKGroup_ThirdParty:BOOL=ON
    -DITKGroup_Video:BOOL=ON
)

  rm -rf "${srcdir}/build"
  mkdir "${srcdir}/build"
  cd "${srcdir}/build"
  cmake \
    ${cmake_opts[@]} \
    ../${_pkgname}-${pkgver}
  make
}

check() {
  cd "${srcdir}/build"
  ctest
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}" install
  python -O -m compileall "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/itk"
  rm -rvf "${pkgdir}/usr/lib/pkgconfig"
  find "${pkgdir}" -type d -empty -delete
}
# vim:set ts=2 sw=2 et:
