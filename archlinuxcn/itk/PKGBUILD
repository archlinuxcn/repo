# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=ITK
pkgname=(itk python-itk)
pkgver=5.3.0
pkgrel=1
pkgdesc='An open-source, cross-platform library that provides developers with an extensive suite of software tools for image analysis'
arch=('x86_64')
url='https://www.itk.org'
license=('Apache')
depends=(
  dcmtk
  double-conversion
  eigen
  expat
  fftw
  gdcm
  hdf5
  intel-oneapi-mkl
  libpng
  libtiff
  vxl
)
makedepends=(
  castxml
  cmake
  git
  gtest
  subversion
  swig
)
options=(!emptydirs !lto)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/InsightSoftwareConsortium/ITK/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('66cd0b0e959753f722fa277baeadd4cdbc51905d666f794e44b4768fad4e55e88dcfbd43e3f46b3ec673fc0d11335edec0f11f2a54813b1ff46a3e4d1491260f')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
# we build the default modules by default
# you could add additional modules by setting -DModule_<NAME>=ON
  cmake_opts=(
    -DBUILD_SHARED_LIBS=ON
    -DBUILD_TESTING=OFF
    -DCMAKE_BUILD_TYPE=Release
    -DCMAKE_INSTALL_PREFIX=/usr
    -DCMAKE_SKIP_INSTALL_RPATH=ON
    -DCMAKE_SKIP_RPATH=ON
    -DITK_BUILD_DEFAULT_MODULES=ON
    -DITK_USE_MKL=ON
    -DITK_USE_SYSTEM_CASTXML=ON
    -DITK_USE_SYSTEM_DCMTK=ON
    -DITK_USE_SYSTEM_DOUBLECONVERSION=ON
    -DITK_USE_SYSTEM_EIGEN=ON
    -DITK_USE_SYSTEM_EXPAT=ON
    -DITK_USE_SYSTEM_FFTW=ON
    -DITK_USE_SYSTEM_GDCM=ON
    -DITK_USE_SYSTEM_GOOGLETEST=ON
    -DITK_USE_SYSTEM_HDF5=ON
    -DITK_USE_SYSTEM_JPEG=ON
    -DITK_USE_SYSTEM_KWIML=ON
    -DITK_USE_SYSTEM_MINC=OFF
    -DITK_USE_SYSTEM_PNG=ON
    -DITK_USE_SYSTEM_SWIG=ON
    -DITK_USE_SYSTEM_TIFF=ON
    -DITK_USE_SYSTEM_VXL=ON
    -DITK_USE_SYSTEM_ZLIB=ON
    -DITK_WRAP_IMAGE_DIMS="2;3;4"
    -DITK_WRAP_PYTHON=ON
    -DITK_WRAP_complex_double=ON
    -DITK_WRAP_covariant_vector_double=ON
    -DITK_WRAP_double=ON
    -DITK_WRAP_rgb_unsigned_short=ON
    -DITK_WRAP_rgba_unsigned_short=ON
    -DITK_WRAP_signed_char=ON
    -DITK_WRAP_signed_long_long=ON
    -DITK_WRAP_unsigned_long_long=ON
    -DITK_WRAP_unsigned_short=ON
    -DITK_WRAP_vector_double=ON
    -DModule_MorphologicalContourInterpolation=ON
    -DPY_SITE_PACKAGES_PATH=/usr/lib/python$(get_pyver)/site-packages
)

  cmake -B "build" -S "${srcdir}/${_pkgname}-${pkgver}" \
    ${cmake_opts[@]} \
    -DITK_USE_GPU=OFF
  make -C "${srcdir}/build"
}

package_itk() {
  make -C "${srcdir}/build" DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}/usr/lib/python$(get_pyver)"
}

package_python-itk() {
  pkgdesc="${pkgdesc} (Python binding)"
  depends+=(
    itk
    python-numpy
    python-xarray
  )

  make -C "${srcdir}/build" DESTDIR="${srcdir}/dist" install
  install -dm755 "${pkgdir}/usr/lib"
  cp -a "${srcdir}/dist/usr/lib/python$(get_pyver)" "${pkgdir}/usr/lib"
  python -O -m compileall "${pkgdir}/usr/lib"
}
# vim:set ts=2 sw=2 et:
