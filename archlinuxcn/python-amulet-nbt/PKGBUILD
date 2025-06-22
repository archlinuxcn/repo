# Maintainer: Kimiblock Moe
# Contributor: 0x9fff00 <0x9fff00+git@protonmail.ch>

_name=Amulet-NBT
_lowername=${_name,,}
_pyname=${_lowername/-/_}
pkgname=python-$_lowername
pkgver=2.1.4
pkgrel=2
epoch=1
pkgdesc='A Python and Cython library for reading and writing binary NBT and stringified NBT'
arch=('x86_64')
url="https://github.com/Amulet-Team/$_name"
license=('LicenseRef-Amulet-Team-1.0.0')
depends=('python' 'python-mutf8' 'python-numpy' 'python-amulet_pybind11_extensions' 'python-amulet-zlib' 'python-amulet-io')
makedepends=('cython' 'git' 'python-build' 'python-installer' 'python-setuptools' 'python-versioneer' 'python-wheel' 'python-amulet-compiler-version' 'python-amulet-compiler-target' 'cmake')
source=("git+$url.git#tag=${pkgver}")
sha256sums=('7eb8b0476f701519639b00d860575a366ef9841e79ff08c9b47f4b0ec72b6887')

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
