# Maintainer: Kimiblock Moe

pkgname=python-amulet-zlib
pkgdesc="A Python and C++ wrapper around zlib"
url="https://github.com/Amulet-Team/Amulet-zlib"
license=("LicenseRef-Amulet-Team-License")
arch=(any)
pkgver=1.0.0a7
pkgrel=1
makedepends=(python-setuptools git python-wheel python-amulet-compiler-version python-packaging python-versioneer cmake)
depends=(python pybind11 python-amulet_pybind11_extensions)
source=(
	"git+https://github.com/Amulet-Team/Amulet-zlib.git#tag=${pkgver}"
)
md5sums=('a297c9e4206ca0d6e8b5cf343e9c2bbb')

function prepare() {
	cd "${srcdir}/Amulet-zlib"
	git submodule init
	git submodule update
}

function build() {
	cd "${srcdir}/Amulet-zlib"
	python setup.py build
}

function package() {
	cd "${srcdir}/Amulet-zlib"
	python setup.py install --root="$pkgdir" --optimize=1
}
