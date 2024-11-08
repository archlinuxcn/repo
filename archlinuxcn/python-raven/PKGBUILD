# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

pkgname=python-raven
pkgver=6.10.0
pkgrel=1
pkgdesc="Python client for Sentry"
arch=(any)
url="https://github.com/getsentry/raven-python"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=("https://pypi.python.org/packages/source/r/raven/raven-$pkgver.tar.gz")

build() {
    cd "$srcdir/raven-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/raven-$pkgver"
    python setup.py install -O1 --skip-build --root="$pkgdir"
    install -Dm0644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

sha256sums=('3fa6de6efa2493a7c827472e984ce9b020797d0da16f1db67197bcc23c8fae54')
