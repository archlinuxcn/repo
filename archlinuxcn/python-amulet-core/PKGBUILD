# Maintainer: Kimiblock Moe

pkgname=python-amulet-core
pkgdesc="A Python library for reading and writing the Minecraft save formats. See Amulet for the actual editor."
url="https://github.com/Amulet-Team/Amulet-Core"
license=(unknown)
arch=(any)
pkgver=1.9.33
pkgrel=1
makedepends=(python-build python-installer python-wheel git)
depends=(python python-amulet-nbt python-numpy python-pymctranslate python-versioneer python-portalocker python-leveldb python-amulet-leveldb)
source=(
	"git+https://github.com/Amulet-Team/Amulet-Core.git#tag=${pkgver}"
)
md5sums=('18dd1caf342e5e522e595426ab9e9951')

function prepare() {
	sed -i 's/versioneer-518/versioneer/g' "${srcdir}/Amulet-Core/pyproject.toml"
	sed -i 's| ~= 1.17||g' "${srcdir}/Amulet-Core/pyproject.toml"
	cd "${srcdir}/Amulet-Core"
	git clean -fdx
}

function build() {
	cd "${srcdir}/Amulet-Core"
	python -m build --wheel --no-isolation
}

function package() {
	cd "${srcdir}/Amulet-Core"
	python -m installer --destdir="${pkgdir}" dist/*.whl
}
