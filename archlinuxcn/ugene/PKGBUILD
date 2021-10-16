# Maintainer: Hu Butui <hot123tea123@gmail.com>
# Contributor: Jens Staal <staal1978@gmail.com>

_pkgname=ugene
pkgname=('ugene' 'ugene-cuda')
pkgver=40.1
pkgrel=1
pkgdesc='A free open-source cross-platform bioinformatics software'
arch=('x86_64')
url='http://ugene.net'
license=('GPL2')
depends=(
  glu
  hicolor-icon-theme
  libxtst
  qt5-script
  qt5-svg
)
makedepends=(
  cuda
  qt5-tools
  opencl-headers
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ugeneunipro/ugene/archive/refs/tags/${pkgver}.tar.gz"
        "ugene.desktop"
)
sha256sums=('92b954449f697957c6b6b2da803ba6ae9ad546f44c584bbb2ab8600ac8b45a6e'
            '5914bc5938dc29f58aeca16233b0bb7dc5271131a3260ed749f9dc009ff3bc03')

prepare() {
  cp -a ${_pkgname}-${pkgver} ${_pkgname}-cuda-${pkgver}
}

build() {
  cd "${_pkgname}-${pkgver}"
  qmake CONFIG+=x64 \
    UGENE_CUDA_DETECTED=0 \
    UGENE_OPENCL_DETECTED=1 \
    UGENE_USE_BUNDLED_ZLIB=0 \
    UGENE_USE_BUNDLED_SQLITE=0
  make
  
  cd "${srcdir}/${_pkgname}-cuda-${pkgver}"
  CUDA_LIB_PATH=/opt/cuda/lib64 \
  CUDA_INC_PATH=/opt/cuda/include \
  qmake CONFIG+=x64 \
    UGENE_CUDA_DETECTED=1 \
    UGENE_OPENCL_DETECTED=1 \
    UGENE_USE_BUNDLED_ZLIB=0 \
    UGENE_USE_BUNDLED_SQLITE=0
  CUDA_LIB_PATH=/opt/cuda/lib64 \
  CUDA_INC_PATH=/opt/cuda/include \
  make
}

package_ugene() {
  cd "${pkgname}-${pkgver}"
  make INSTALL_ROOT=${pkgdir} install
  install -d "${pkgdir}/usr/share/applications"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}

package_ugene-cuda() {
  pkgdesc="${pkgdesc} (with CUDA)"
  provides=(ugene=${pkgver})
  conflicts=(ugene)
  depends+=(
    cuda
)
  cd "${pkgname}-${pkgver}"
  make INSTALL_ROOT=${pkgdir} install
  install -d "${pkgdir}/usr/share/applications"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:

