# Maintainer: Kimiblock Moe

pkgname=synapse-http-antispam
pkgdesc="A Synapse module that forwards spam checking to an HTTP server."
url="https://github.com/maunium/synapse-http-antispam"
license=(MIT)
arch=(any)
pkgver=0.5.1
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

sha256sums=('1b026d58e1492f53d5dae25bfac05d66f4bfac9f05b8c2448c46816607b56490')
