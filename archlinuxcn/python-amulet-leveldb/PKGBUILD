# Maintainer: Kimiblock Moe

pkgname=python-amulet-leveldb
pkgdesc="A Cython wrapper for Mojang's modified LevelDB library."
url="https://github.com/Amulet-Team/Amulet-LevelDB"
license=("LicenseRef-Amulet-Team-License")
arch=(any)
pkgver=1.0.4
pkgrel=1
makedepends=(python-portalocker python-leveldb python-setuptools git python-versioneer cython gcc-libs glibc zlib)
depends=(python python-portalocker python-leveldb cython gcc-libs glibc zlib)
source=(
	"git+https://github.com/Amulet-Team/Amulet-LevelDB.git#tag=${pkgver}"
)
md5sums=('e90836ece1c34d496f7571c80e4e3b71')

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
