# Maintainer: Kimiblock Moe

pkgname=python-amulet-compiler-target
pkgdesc="A token library to pin compile-time requirements"
url="https://github.com/Amulet-Team/Amulet-Compiler-Target"
license=("LicenseRef-Amulet-Team-License")
arch=(any)
pkgver=2.0
pkgrel=1
makedepends=(python-setuptools git python-wheel python-build python-installer)
depends=(python)
source=(
	"git+https://github.com/Amulet-Team/Amulet-Compiler-Target.git#tag=${pkgver}"
)
md5sums=('85c55ed1c7f26ac0f4c0fba47f1e42e2')

function prepare() {
	cd "${srcdir}/Amulet-Compiler-Target"
	git submodule init
	git submodule update
}

function build() {
	cd "${srcdir}/Amulet-Compiler-Target"
	#python setup.py build
	python -m build --wheel --no-isolation
}

function package() {
	cd "${srcdir}/Amulet-Compiler-Target"
	#python setup.py install --root="$pkgdir" --optimize=1
	python -m installer --destdir="$pkgdir" dist/*.whl
}
