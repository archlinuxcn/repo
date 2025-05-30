# Maintainer: Jingbei Li <i@jingbei.li>
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
pkgver=20.0
pkgrel=1
pkgdesc="Dlib is a general purpose cross-platform C++ library designed using contract programming and modern C++ techniques."
arch=('x86_64')
url="http://www.dlib.net/"
license=('Boost')
depends=('cblas' 'ffmpeg' 'giflib' 'lapack' 'libjpeg-turbo' 'libjxl' 'libpng' 'libx11')
makedepends=('boost' 'cmake' 'python-setuptools' 'sqlite')
[[ $_build_cuda -eq 1 ]] && makedepends+=('ccache-ext' 'cuda' 'cudnn')
optdepends=('sqlite')
#source=("$url/files/${_pkgname}-${pkgver}.tar.bz2")
#source=("https://pypi.io/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
source=("https://github.com/davisking/dlib/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('705749801c7896f5c19c253b6be639f4cef2c1831a9606955f01b600b3d86d80')
[[ $_build_cuda -eq 1 ]] && options=(!lto)

prepare() {
	cd "$srcdir/"
	if [[ $_build_cuda -eq 1 ]]; then cp -a "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-cuda"; fi
}

build_python-dlib(){
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py build --no DLIB_USE_CUDA
}

build_python-dlib-cuda(){
	cd "${srcdir}/${_pkgname}-${pkgver}-cuda"
	python setup.py build \
		--set CUDA_HOST_COMPILER=/usr/bin/gcc-14 \
		--set CUDA_NVCC_EXECUTABLE=/usr/lib/ccache/bin/nvcc-ccache \
		--set CMAKE_C_COMPILER=/usr/bin/gcc-14 \
		--set CMAKE_CXX_COMPILER=/usr/bin/g++-14
}

build(){
	if [[ $_build_cpu -eq 1 ]]; then build_python-dlib; fi
	if [[ $_build_cuda -eq 1 ]]; then build_python-dlib-cuda; fi
}

package_python-dlib(){
	depends+=('python')
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}

package_python-dlib-cuda(){
	depends+=('cuda' 'cudnn' 'python')
	provides=('python-dlib')
	conflicts=('python-dlib')
	cd "${srcdir}/${_pkgname}-${pkgver}-cuda"
	python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
