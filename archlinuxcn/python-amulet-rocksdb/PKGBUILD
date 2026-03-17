# Maintainer: Kimiblock Moe

pkgname=python-amulet-rocksdb
pkgdesc="A pybind11 wrapper for RocksDB."
license=(custom)
arch=(any)
pkgver=1.0.1
pkgrel=2
url="https://github.com/Amulet-Team/Amulet-RocksDB"
makedepends=(python-build python-installer python-wheel python-setuptools python-versioneer python-packaging git cmake)
depends=(python pybind11 python-amulet_pybind11_extensions)
source=(
	"source"::"git+$url.git#tag=${pkgver}"
)
md5sums=('2d3b7f1540f9ba15a52a7e81bffad369')

function prepare() {
	cd source
	git clean -fdx
#	sed -i 's/versioneer-518/versioneer/g' "${srcdir}/Minecraft-Model-Reader-${pkgver}/pyproject.toml"
	sed -i 's|{PYBIND11_REQUIREMENT}||g' requirements.py
}

function build() {
	cd "source"
	python -m build --wheel --no-isolation
}

function package() {
	cd "source"
	python -m installer --destdir="${pkgdir}" dist/*.whl
}
