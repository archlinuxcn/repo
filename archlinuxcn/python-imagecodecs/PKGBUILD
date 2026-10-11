# Maintainer: Butui Hu <hot123tea123@gmail.com>

_name=imagecodecs
pkgname=python-imagecodecs
pkgver=2026.10.10
pkgrel=2
pkgdesc='Image transformation, compression, and decompression codecs'
arch=('x86_64')
url='https://github.com/cgohlke/imagecodecs'
license=('BSD-3-Clause')
depends=(
  blosc
  blosc2
  brotli
  brunsli
  bzip2
  charls
  giflib
  glibc
  jxrlib
  lcms2
  lerc
  libaec
  libavif
  libdeflate
  libheif
  libjpeg-turbo
  libjxl
  libpng
  libtiff
  libwebp
  lz4
  lzfse
  openjpeg2
  openjph
  python-numpy
  python-pillow
  snappy
  xz
  zfp
  zlib
  zlib-ng
  zopfli
  zstd
)
makedepends=(
  cython
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_name}-${pkgver}.tar.gz::https://github.com/cgohlke/imagecodecs/archive/v${pkgver}.tar.gz"
)
sha256sums=('64f3c5789d28e338e6cd3ede471e15ea92d23820bb233b33b32c55845e4cf722')

prepare() {
  cd "${srcdir}/${_name}-${pkgver}"
  # jxrlib ships JXRGlue.h including JXRVersion.h but never installs it
  # (same bug worked around in freeimage). Generate the missing header.
  if [[ ! -f /usr/include/jxrlib/JXRVersion.h ]]; then
    cat > imagecodecs/JXRVersion.h <<'EOF'
#ifndef JXRVERSION_H
#define JXRVERSION_H
#define JXR_VERSION_MAJOR 1
#define JXR_VERSION_MINOR 4
#define JXR_VERSION_PATCH 4
#define JXR_MAKEVERSION(major, minor, patch) (((major) << 16) | ((minor) << 8) | (patch))
#define JXR_VERSION JXR_MAKEVERSION(JXR_VERSION_MAJOR, JXR_VERSION_MINOR, JXR_VERSION_PATCH)
#endif
EOF
  fi
}

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m build --wheel --no-isolation --skip-dependency-check
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:ts=2:sw=2:et:
