# Maintainer: Kimiblock Moe

pkgname=python-amulet-leveldb
pkgdesc="A Cython wrapper for Mojang's modified LevelDB library."
url="https://github.com/Amulet-Team/Amulet-LevelDB"
license=("LicenseRef-Amulet-Team-License")
arch=(any)
pkgver=1.1.1
pkgrel=1
makedepends=(python-portalocker python-leveldb python-setuptools git python-versioneer cython gcc-libs glibc zlib cmake)
depends=(python python-portalocker python-leveldb cython gcc-libs glibc zlib pybind11 python-amulet_pybind11_extensions)
source=(
	"git+https://github.com/Amulet-Team/Amulet-LevelDB.git#tag=${pkgver}"
)
md5sums=('43ef3e071de1b7f31811457e6604a2f2')

function prepare() {
	cd "${srcdir}/Amulet-LevelDB"
	git submodule init
	git submodule update
}

function build() {
	cd "${srcdir}/Amulet-LevelDB"
	python setup.py build
}

function package() {
	cd "${srcdir}/Amulet-LevelDB"
	python setup.py install --root="$pkgdir" --optimize=1
	install -Dm644 "${srcdir}/Amulet-LevelDB/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
