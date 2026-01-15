# Contributor: 0x9fff00 <0x9fff00+git@protonmail.ch>

_name=PyMCTranslate
pkgname=python-${_name,,}
pkgver=1.2.40
pkgrel=1
pkgdesc='A library of block mappings that can be used to convert from any Minecraft format into any other Minecraft format'
arch=('any')
url="https://github.com/gentlegiantJGC/$_name"
license=('LicenseRef-Amulet-Team-1.0.0')
depends=('python' 'python-amulet-nbt' 'python-numpy')
makedepends=('git' 'python-build' 'python-installer' 'python-setuptools' 'python-versioneer' 'python-wheel')
source=("git+$url.git#tag=${pkgver}")
sha256sums=('6f7361d078e2395f2504e1bfe39540072a734c3aea2a9309f160b41495fbb78c')

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
