# Maintainer: Kimiblock Moe

pkgname=python-amulet_pybind11_extensions
pkgdesc="Some useful extensions to pybind11"
url="https://github.com/Amulet-Team/Amulet-pybind11-extensions"
license=("LicenseRef-Amulet-Team-License")
arch=(any)
pkgver=1.2.0a3
pkgrel=1
makedepends=(python-setuptools git python-wheel python-amulet-compiler-version python-packaging python-versioneer)
optdepends+=(python-black)
depends=(python pybind11)
source=(
	"git+https://github.com/Amulet-Team/Amulet-pybind11-extensions.git#tag=${pkgver}"
)
md5sums=('76e6d617156f033b13ae0e068c416178')

function prepare() {
	cd "${srcdir}/Amulet-pybind11-extensions"
	git submodule init
	git submodule update
}

function build() {
	cd "${srcdir}/Amulet-pybind11-extensions"
	python setup.py build
}

function package() {
	cd "${srcdir}/Amulet-pybind11-extensions"
	python setup.py install --root="$pkgdir" --optimize=1
	install -d "${pkgdir}/usr/include/amulet"
	cp -r "${srcdir}/Amulet-pybind11-extensions/"src/amulet/pybind11_extensions "${pkgdir}/usr/include/amulet/pybind11_extensions"
}
