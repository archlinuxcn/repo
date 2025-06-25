# Maintainer: Kimiblock Moe

pkgname=synapse-http-antispam
pkgdesc="A Synapse module that forwards spam checking to an HTTP server."
url="https://github.com/maunium/synapse-http-antispam"
license=(MIT)
arch=(any)
pkgver=0.4.0
pkgrel=1
makedepends=(python-build python-installer python-wheel git python-hatchling)
depends=(python python-twisted matrix-synapse)
source=(
	"git+https://github.com/maunium/synapse-http-antispam.git#tag=v${pkgver}"
)

#function prepare() {}

function build() {
	cd "${srcdir}/${pkgname}"
	python -m build --wheel --no-isolation
}

function package() {
	cd "${srcdir}/${pkgname}"
	python -m installer --destdir="${pkgdir}" dist/*.whl
}

sha256sums=('b33c97686f6af0441a89397793b2055d4dac77f98efcdd35fa79b01ae1a30bd3')
