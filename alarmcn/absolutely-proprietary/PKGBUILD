# Maintainer: Daniel Peukert <daniel@peukert.cc>
pkgname='absolutely-proprietary'
pkgver='20220518'
_commit='632ebf75bff68959e48ad7db06a9350fede806d0'
pkgrel='2'
pkgdesc="Proprietary package detector for arch-based distros that uses Parabola's package blacklist"
arch=('any')
url="https://github.com/vmavromatis/$pkgname"
license=('GPL-3.0-only')
depends=('python')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$_commit.tar.gz")
sha512sums=('d6b10dd6b89171e568b07a86617b0b731aa8cbd20f61968f4fd1e4bf42e73665d4746034a6181a210b1644070abfe80d91b1378ad0dab0413ffe58516b3332b2')

_sourcedirectory="$pkgname-$_commit"

build() {
	cd "$srcdir/$_sourcedirectory/"
	python setup.py build
}

check() {
	python "$srcdir/$_sourcedirectory/absolutely_proprietary/__init__.py" --help | tee '/dev/stderr' | grep -q '^Find proprietary packages$'
}

package() {
	cd "$srcdir/$_sourcedirectory/"
	python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
