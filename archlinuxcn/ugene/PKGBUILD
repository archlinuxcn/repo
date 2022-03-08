# Maintainer: Hu Butui <hot123tea123@gmail.com>
# Contributor: Jens Staal <staal1978@gmail.com>

_pkgname=ugene
pkgname=('ugene' 'ugene-cuda')
pkgver=42.0
pkgrel=2
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
  gendesk
  qt5-tools
  opencl-headers
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ugeneunipro/ugene/archive/refs/tags/${pkgver}.tar.gz"
        # "ugene.desktop"
)
sha256sums=('200159838d2d2a4a701be8fb51b0e00c0ca52c4054d72c42cdd6913bbef56d53')

prepare() {
  echo "generating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Education;Science" \
    --icon "${_pkgname}" \
    --mimetypes "application/x-ugene-fa;application/x-ugene-uprj;application/x-ugene-uwl;application/x-ugene-uql;application/x-ugene-abi;application/x-ugene-aln;application/x-ugene-embl;application/x-ugene-sw;application/x-ugene-fastq;application/x-ugene-gb;application/x-ugene-gff;application/x-ugene-msf;application/x-ugene-newick;application/x-ugene-pdb;application/x-ugene-sam-bam;application/x-ugene-srfa;application/x-ugene-sto;application/x-ugene-db;application/x-ugene-scf;application/x-ugene-mmdb;application/x-ugene-hmm;" \
    --exec "/opt/ugene/ugeneui"

  sed -i "s#16384#16384l#" "${_pkgname}-${pkgver}/src/libs_3rdparty/breakpad/src/client/linux/handler/exception_handler.cc"
  cp -a ${_pkgname}-${pkgver} ${_pkgname}-cuda-${pkgver}
}

build() {
  cd "${_pkgname}-${pkgver}"
  qmake \
    CONFIG+=x64 \
    PREFIX=/opt/${_pkgname} \
    UGENE_CUDA_DETECTED=0 \
    UGENE_OPENCL_DETECTED=1 \
    UGENE_USE_BUNDLED_ZLIB=0 \
    UGENE_USE_SYSTEM_SQLITE=1
  make
  
  cd "${srcdir}/${_pkgname}-cuda-${pkgver}"
  CUDA_LIB_PATH=/opt/cuda/lib64 \
  CUDA_INC_PATH=/opt/cuda/include \
  qmake \
    CONFIG+=x64 \
    PREFIX=/opt/${_pkgname} \
    UGENE_CUDA_DETECTED=1 \
    UGENE_OPENCL_DETECTED=1 \
    UGENE_USE_BUNDLED_ZLIB=0 \
    UGENE_USE_SYSTEM_SQLITE=1
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
  CUDA_LIB_PATH=/opt/cuda/lib64 \
  CUDA_INC_PATH=/opt/cuda/include \
  make INSTALL_ROOT=${pkgdir} install
  install -d "${pkgdir}/usr/share/applications"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:

