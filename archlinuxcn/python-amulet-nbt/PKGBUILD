# Maintainer: Kimiblock Moe
# Contributor: 0x9fff00 <0x9fff00+git@protonmail.ch>

_name=Amulet-NBT
_lowername=${_name,,}
_pyname=${_lowername/-/_}
pkgname=python-$_lowername
pkgver=2.1.6
pkgrel=1
epoch=1
pkgdesc='A Python and Cython library for reading and writing binary NBT and stringified NBT'
arch=('x86_64')
url="https://github.com/Amulet-Team/$_name"
license=('LicenseRef-Amulet-Team-1.0.0')
depends=('python' 'python-mutf8' 'python-numpy' 'python-amulet_pybind11_extensions' 'python-amulet-zlib' 'python-amulet-io')
makedepends=('cython' 'git' 'python-build' 'python-installer' 'python-setuptools' 'python-versioneer' 'python-wheel' 'python-amulet-compiler-version' 'python-amulet-compiler-target' 'cmake')
source=("git+$url.git#tag=${pkgver}")
sha256sums=('5ccc324530a3ad9599261519df1e1857745db9291d4f173737367b50a7ba1ffc')

prepare() {
	cd "$_name"
	sed -i "s|numpy ~= 1.17|numpy|g" pyproject.toml
}

build() {
	cd "$_name"
	export AMULET_FREEZE_COMPILER=1
	python -m build --wheel --no-isolation
}

function package() {
	cd "$_name"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
