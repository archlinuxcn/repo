# Maintainer: Kimiblock Moe

pkgname=python-mdit_plain-git
pkgdesc="A renderer for markdown-it-py that converts markdown documents into plain text by removing all markup. "
url="https://github.com/elespike/mdit_plain"
license=(MIT)
arch=(any)
pkgver=r2.218934e
pkgrel=2
makedepends=(python-build python-installer python-wheel python-setuptools git)
depends=(python)
source=(
	"git+https://github.com/elespike/mdit_plain.git"
)
md5sums=(
	"SKIP"
)
provides=(python-mdlt_plain)

function pkgver() {
	cd "${srcdir}/mdit_plain"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

function build() {
	cd "${srcdir}/mdit_plain"
	python -m build --wheel --no-isolation
}

function package() {
	cd "${srcdir}/mdit_plain"
	python -m installer --destdir="${pkgdir}" dist/*.whl
}
