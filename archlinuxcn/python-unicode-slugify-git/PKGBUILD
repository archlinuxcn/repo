# Maintainer: lsf
pkgname=python-unicode-slugify-git
_pkgname=unicode-slugify
pkgver=r41.8a9c3dc
pkgrel=2
pkgdesc="A Python slugify application that handles unicode"
arch=(any)
url="https://github.com/mozilla/unicode-slugify"
license=('BSD')
makedepends=("python-setuptools" "git")
depends=("python" "python-unidecode" "python-six")
source=("git+https://github.com/mozilla/unicode-slugify")
sha256sums=('SKIP')
provides=(python-${_pkgname})

pkgver() {
  cd "$srcdir/$_pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "$srcdir/$_pkgname"
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
