# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchtext
_pkgname=text
pkgver=0.18.0
pkgrel=4
epoch=1
pkgdesc='Data loaders and abstractions for text and NLP'
arch=('x86_64')
url='https://github.com/pytorch/text'
license=('BSD-3-Clause')
depends=(
  glibc
  gcc-libs
  python-filelock
  python-numpy
  python-pytorch
  python-requests
  python-tqdm
)
optdepends=(
  python-nltk
  python-revtok
  "python-sacremoses: Moses tokenizer port in SacreMoses"
  "python-spacy: English tokenizer from SpaCy"
)
makedepends=(
  cmake
  git
  numactl
  patchelf
  python-build
  python-installer
  python-setuptools
  python-sympy
  python-wheel
)
source=("${_pkgname}::git+https://github.com/pytorch/text.git#tag=v${pkgver}"
        "0001-add-GLOG_USE_GLOG_EXPORT-definition.patch"
        "https://github.com/Kitware/CMake/releases/download/v3.31.6/cmake-3.31.6-linux-x86_64.tar.gz"
)
sha512sums=('696404634cca1d535a5cf19105e4727fe441e47ecfab7e88fbdf0066abfe69b39103addd148cbca1d74471e89a74a1b6ea6e02e71e06e9cc8d9bac4414d36554'
            '8d5faf99d3e82039ebf0daffb1f15e5e6195141a79e1809006d75597bd322bfd6495ae63d4396dbe9ec7a007b0986bf92e66b87cf2f4e062f5732d3675343b5f'
            '42395e20b10a8e9ef3e33014f9a4eed08d46ab952e02d2c1bbc8f6133eca0d7719fb75680f9bbff6552f20fcd1b73d86860f7f39388d631f98fb6f622b37cf04')

prepare() {
  cd "${_pkgname}"
  git submodule update --init --recursive
  # fix glog issue
  patch -p1 -i "${srcdir}/0001-add-GLOG_USE_GLOG_EXPORT-definition.patch"
}

build() {
   # build with cmake 3.31.6, not working with cmake 4.0.0 yet
  export PATH=${srcdir}/cmake-3.31.6-linux-x86_64/bin:${PATH}
  cd "${_pkgname}"
  CMAKE_GENERATOR="Unix Makefiles" \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # fix rpath
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  patchelf --set-rpath '$ORIGIN/lib' "${pkgdir}${site_packages}/torchtext/_torchtext.so"
}
# vim:set ts=2 sw=2 et:
