# Maintainer:  Oliver Goethel <deezy>
# Contributor: eolianoe eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Mathias Anselmann <mathias.anselmann@gmail.com>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Michele Mocciola <mickele>
# Contributor: Simon Zilliken <simon____AT____zilliken____DOT____name>
# Contributor: chuckdaniels

pkgname=paraview
_pkgver=5.4.1
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc='Parallel Visualization Application using VTK'
arch=('i686' 'x86_64')
url='http://www.paraview.org'
license=('custom')
depends=('qt5-tools' 'qt5-x11extras'  'qt5-xmlpatterns'
         'openmpi' 'python-matplotlib' 'python-numpy'
         'ffmpeg' 'boost' 'glew' 'protobuf'
         'expat' 'freetype2' 'libjpeg' 'libxml2' 'libtheora' 'libpng' 'libtiff' 'zlib'
         'ospray' 'cgns')
makedepends=('cmake' 'mesa' 'gcc-fortran' 'ninja')
source=("http://paraview.org/files/v${pkgver:0:3}/ParaView-v${_pkgver}.tar.gz"
        "visit_fix_gcc7.patch")
sha1sums=('3b7df6f6bbf978bb9a8583c97208a58af9afcdde'
          'f86feb14e7e17ce3ad5341ee4f52b40111cecbec')

prepare() {
  cd "${srcdir}/ParaView-v${_pkgver}"

  #rm -rf "${srcdir}/build"
  mkdir -p "${srcdir}/build"

  patch Utilities/VisItBridge/databases/readers/Vs/VsStaggeredField.C \
    "${srcdir}/visit_fix_gcc7.patch"
}

build() {
  cd "${srcdir}/build"

  # flags to enable system libs
  local VTK_USE_SYSTEM_LIB=""
  for lib in CGNS EXPAT FREETYPE GLEW HDF5 JPEG LIBXML2 OGGTHEORA PNG PROTOBUF TIFF ZLIB
  do
    VTK_USE_SYSTEM_LIB+="-DVTK_USE_SYSTEM_${lib}:BOOL=ON "
  done

  cmake \
    -DBUILD_DOCUMENTATION:BOOL=OFF \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_TESTING:BOOL=OFF \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DCMAKE_C_COMPILER:STRING=mpicc \
    -DCMAKE_CXX_COMPILER:STRING=mpicxx \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DOSPRAY_INSTALL_DIR:PATH=/usr \
    -DPARAVIEW_ENABLE_CGNS:BOOL=ON \
    -DPARAVIEW_ENABLE_FFMPEG:BOOL=ON \
    -DPARAVIEW_ENABLE_MATPLOTLIB:BOOL=ON \
    -DPARAVIEW_ENABLE_PYTHON:BOOL=ON \
    -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \
    -DPARAVIEW_QT_VERSION:STRING=5 \
    -DPARAVIEW_USE_MPI:BOOL=ON \
    -DPARAVIEW_USE_VISITBRIDGE:BOOL=ON \
    -DPARAVIEW_USE_OSPRAY:BOOL=ON \
    -DVISIT_BUILD_READER_CGNS:BOOL=ON \
    -DVTK_PYTHON_FULL_THREADSAFE:BOOL=ON \
    -DVTK_PYTHON_VERSION:STRING=3 \
    -DVTK_QT_VERSION:STRING=5 \
    -DVTK_RENDERING_BACKEND:STRING=OpenGL2 \
    -DVTK_SMP_IMPLEMENTATION_TYPE:STRING=OpenMP \
    -DVTK_USE_TK:BOOL=ON \
    ${VTK_USE_SYSTEM_LIB} \
    -GNinja \
    ../ParaView-v${_pkgver}

  ninja ${MAKEFLAGS}
}

package() {
  cd "${srcdir}/build"

  DESTDIR="${pkgdir}" ninja install

  #Install license
  install -Dm644 "${srcdir}/ParaView-v${_pkgver}/License_v1.2.txt" "${pkgdir}/usr/share/licenses/paraview/LICENSE"

  # Remove IceT man pages to avoid conflicts
  rm -- "${pkgdir}/usr/share/man/man3/icet"*.3
}
