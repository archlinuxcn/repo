# Contributor: 0x9fff00 <0x9fff00+git@protonmail.ch>

_name=Amulet-NBT
_lowername=${_name,,}
_pyname=${_lowername/-/_}
pkgname=python-$_lowername
pkgver=5.0.0a4
pkgrel=2
pkgdesc='A Python and Cython library for reading and writing binary NBT and stringified NBT'
arch=('x86_64')
url="https://github.com/Amulet-Team/$_name"
license=('LicenseRef-Amulet-Team-1.0.0')
depends=('python' 'python-mutf8' 'python-numpy' 'python-amulet_pybind11_extensions' 'python-amulet-zlib' 'python-amulet-io')
makedepends=('cython' 'git' 'python-build' 'python-installer' 'python-setuptools' 'python-versioneer' 'python-wheel' 'python-amulet-compiler-version' 'python-amulet-compiler-target' 'cmake')
source=("git+$url.git#tag=${pkgver}")
sha256sums=('79b98719b631ba7c4a38c319671e79e970163968c9c6cea4494ea386c4f9a0a0')

prepare() {
	cd "$_name"
#	sed -i 's|{AMULET_IO_REQUIREMENT},||g' requirements.py
#	sed -i 's|{AMULET_ZLIB_REQUIREMENT},||g' requirements.py
#	sed -i 's|AMULET_IO_REQUIREMENT = "|#AMULET_IO_REQUIREMENT = "|g' requirements.py
#	sed -i 's|AMULET_ZLIB_REQUIREMENT = "|#AMULET_ZLIB_REQUIREMENT = "|g' requirements.py
}

build() {
	cd "$_name"
	#export AMULET_ZLIB_REQUIREMENT="~=$(pacman -Q python-amulet-zlib | awk '{sub(/-.*/, "", $2); print $2}')"
#	unset AMULET_ZLIB_REQUIREMENT
	#export AMULET_IO_REQUIREMENT="~=$(pacman -Q python-amulet-io | awk '{sub(/-.*/, "", $2); print $2}')"
#	unset AMULET_IO_REQUIREMENT
	export AMULET_FREEZE_COMPILER=1
	python -m build --wheel --no-isolation
}

function package() {
  cd "$_name"

  python -m installer --destdir="$pkgdir" dist/*.whl

  # https://wiki.archlinux.org/title/Python_package_guidelines#Using_site-packages
  local _site_packages="$(python -c 'import site; print(site.getsitepackages()[0])')"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
	install -Dm644 "${srcdir}/Amulet-NBT/LICENSE" \
		"${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
