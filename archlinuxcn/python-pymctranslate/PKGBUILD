# Contributor: 0x9fff00 <0x9fff00+git@protonmail.ch>

_name=PyMCTranslate
pkgname=python-${_name,,}
pkgver=1.2.51
pkgrel=1
pkgdesc='A library of block mappings that can be used to convert from any Minecraft format into any other Minecraft format'
arch=('any')
url="https://github.com/gentlegiantJGC/$_name"
license=('LicenseRef-Amulet-Team-1.0.0')
depends=('python' 'python-amulet-nbt' 'python-numpy')
makedepends=('git' 'python-build' 'python-installer' 'python-setuptools' 'python-versioneer' 'python-wheel')
source=("git+$url.git#tag=${pkgver}")
sha256sums=('1c9fdf7d4431fb297882e4b77027c7ea0d0c775670bab1e1b6fc5062d50555f0')

prepare() {
  cd "$_name"

  # expand placeholders
  git archive --format tar HEAD PyMCTranslate/_version.py | tar -x

  # use current versioneer
  sed -Ei 's/(versioneer)-518/\1/' pyproject.toml
}

build() {
  cd "$_name"

  python -m build --wheel --no-isolation
}

package() {
  cd "$_name"

  python -m installer --destdir="$pkgdir" dist/*.whl
}
