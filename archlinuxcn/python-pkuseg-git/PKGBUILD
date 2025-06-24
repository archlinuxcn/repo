# Maintainer: Kimiblock Moe

pkgname=python-pkuseg-git
pkgdesc="pkuseg多领域中文分词工具; The pkuseg toolkit for multi-domain Chinese word segmentation"
url="https://github.com/lancopku/pkuseg-python"
license=(MIT)
arch=(any)
pkgver=r200.071d57c
pkgrel=1
makedepends=(python-numpy cython python-build python-installer python-wheel python-setuptools git)
depends=(python python-numpy cython)
source=(
	"git+https://github.com/lancopku/pkuseg-python.git"
)
md5sums=(
	"SKIP"
)
provides=(python-pkuseg)

function pkgver() {
	cd "${srcdir}/pkuseg-python"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

function build() {
	cd "${srcdir}/pkuseg-python"
	#python -m build --wheel --no-isolation
	python setup.py build
}

function package() {
	cd "${srcdir}/pkuseg-python"
	#python -m installer --destdir="${pkgdir}" dist/*.whl
	python setup.py install --root="$pkgdir" --optimize=1
}
