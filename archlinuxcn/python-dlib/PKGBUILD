# Maintainer: Zen Wen <zen.8841@gmail.com>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Lev Velykoivanenko <velykoivanenko dot lev at gmail dot com>
# Contributor: Flávio Zavan <flavio dot zavan at gmail dot com>
# Contributor: pingplug
# Contributor: perlawk
# Contributor: xsmile

_build_cpu=1
_build_cuda=1

pkgbase=python-dlib
[[ $_build_cpu -eq 1 ]] && pkgname+=('python-dlib')
[[ $_build_cuda -eq 1 ]] && pkgname+=('python-dlib-cuda')
_pkgname=dlib
pkgver=20.0.1
pkgrel=1
pkgdesc="Dlib is a general purpose cross-platform C++ library designed using contract programming and modern C++ techniques."
arch=('x86_64')
url="http://www.dlib.net/"
license=('BSL-1.0')
depends=('cblas' 'giflib' 'lapack' 'libjpeg-turbo' 'libjxl' 'libpng' 'libx11')
makedepends=('boost' 'cmake' 'python-setuptools' 'sqlite')
[[ $_build_cuda -eq 1 ]] && makedepends+=('ccache-ext' 'cuda' 'cudnn')
optdepends=('sqlite')
#source=("$url/files/${_pkgname}-${pkgver}.tar.bz2")
#source=("https://pypi.io/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
source=("https://github.com/davisking/dlib/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('dab5b4ec4b68bd7dc128a1fb7900723f89d2da107e44cd5def7d38fc57252a9d')
[[ $_build_cuda -eq 1 ]] && options=(!lto)

prepare() {
  cd "$srcdir/"
  if [[ $_build_cuda -eq 1 ]]; then cp -a "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-cuda"; fi
}

build_python-dlib() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  DLIB_USE_CUDA=OFF python setup.py build
}

build_python-dlib-cuda() {
  cd "${srcdir}/${_pkgname}-${pkgver}-cuda"
  DLIB_USE_CUDA=ON python setup.py build
}

build() {
  if [[ $_build_cpu -eq 1 ]]; then build_python-dlib; fi
  if [[ $_build_cuda -eq 1 ]]; then build_python-dlib-cuda; fi
}

package_python-dlib() {
  depends+=('python')
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}

package_python-dlib-cuda() {
  depends+=('cuda' 'cudnn' 'python')
  provides=('python-dlib')
  conflicts=('python-dlib')
  cd "${srcdir}/${_pkgname}-${pkgver}-cuda"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
