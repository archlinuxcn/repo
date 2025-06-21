# Contributor: 0x9fff00 <0x9fff00+git@protonmail.ch>

_name=PyMCTranslate
pkgname=python-${_name,,}
pkgver=1.2.30
_commit=9d747dc87843ba1ee5956e931d6affa11e65cbce
pkgrel=1
pkgdesc='A library of block mappings that can be used to convert from any Minecraft format into any other Minecraft format'
arch=('any')
url="https://github.com/gentlegiantJGC/$_name"
license=('LicenseRef-Amulet-Team-1.0.0')
depends=('python' 'python-amulet-nbt' 'python-numpy')
makedepends=('git' 'python-build' 'python-installer' 'python-setuptools' 'python-versioneer' 'python-wheel')
# tests directory isn't in pypi sdist
# github tarball has unstable hash due to https://github.com/gentlegiantJGC/PyMCTranslate/blob/45024a6ca12592913e6249269d8a180b2940f6aa/PyMCTranslate/_version.py#L25
source=("git+$url.git#commit=$_commit")
sha256sums=('SKIP')

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

check() {
  cd "$_name"

  python -m unittest discover -s tests
}

package() {
  cd "$_name"

  python -m installer --destdir="$pkgdir" dist/*.whl

  # https://wiki.archlinux.org/title/Python_package_guidelines#Using_site-packages
  local _site_packages="$(python -c 'import site; print(site.getsitepackages()[0])')"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  local _license_path="$_site_packages/$_name-$pkgver.dist-info/LICENSE"
  [ -f "$pkgdir/$_license_path" ] || { echo "License file not found"; exit 1; }
  ln -s "$_license_path" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
