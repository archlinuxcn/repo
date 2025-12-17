# Maintainer: Kimiblock Moe

pkgname=python-minecraft-model-reader
pkgdesc="Minecraft-Model-Reader for Amulet-Core"
license=(custom)
arch=(any)
pkgver=1.4.7
pkgrel=1
url="https://github.com/gentlegiantJGC/Minecraft-Model-Reader"
makedepends=(python-build python-installer python-wheel python-setuptools python-versioneer)
depends=(python)
source=(
	"model-reader-${pkgver}"::"https://github.com/gentlegiantJGC/Minecraft-Model-Reader/archive/refs/tags/${pkgver}.tar.gz"
)
md5sums=('1b0947b72d337da261b06f164ee663f5')

function prepare() {
	sed -i 's/versioneer-518/versioneer/g' "${srcdir}/Minecraft-Model-Reader-${pkgver}/pyproject.toml"
}

function build() {
	cd "${srcdir}/Minecraft-Model-Reader-${pkgver}"
	python -m build --wheel --no-isolation
}

function package() {
	cd "${srcdir}/Minecraft-Model-Reader-${pkgver}"
	python -m installer --destdir="${pkgdir}" dist/*.whl
}

