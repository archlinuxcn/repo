# Maintainer:
# Contributor: Bjoern Franke <bjo+aur@schafweide.org>

_module="markdownify"
_pkgname="python-$_module"
pkgname="$_pkgname"
pkgver=0.12.1
pkgrel=1
pkgdesc="Convert HTML to Markdown"
url="https://github.com/matthewwithanm/python-markdownify"
license=('MIT')
arch=('any')

depends=(
  'python'
  'python-beautifulsoup4'
  'python-six'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
checkdepends=(
  'python-pytest'
)

options=(!emptydirs)

_pkgsrc="$_module-${pkgver%%.r*}"
_pkgext="tar.gz"
source=(
  "$_pkgsrc.$_pkgext"::"https://pypi.io/packages/source/${_module::1}/$_module/$_module-${pkgver%%.r*}.$_pkgext"
)
sha256sums=(
  '1fb08c618b30e0ee7a31a39b998f44a18fb28ab254f55f4af06b6d35a2179e27'
)

prepare() {
  cd "$_pkgsrc"

  # don't package tests
  sed -E \
    -e 's@^(\s*packages=find_packages).*$@\1(exclude=["tests"]),@' \
    -i setup.py
}

build() {
  cd "$_pkgsrc"
  python -m build --wheel --no-isolation
}

check() {
  cd "$_pkgsrc"
  python -m pytest
}

package() {
  cd "$_pkgsrc"
  python -m installer --destdir="$pkgdir" "$(ls -1 dist/*.whl | sort -rV | head -1)"

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
