# Maintainer: Christopher Arndt <aur -at- chrisarndt -dot- de>
# Contributor: Simon Conseil <contact+aur at saimon dot org>

pkgname=pip-tools
pkgver=6.9.0
pkgrel=1
pkgdesc='A set of tools to keep your pinned Python dependencies fresh'
arch=(any)
url='https://github.com/jazzband/pip-tools/'
license=(BSD)
depends=('python-click>=7' python-build 'python-pip>=21' python-setuptools python-wheel)
makedepends=(python-build python-installer python-setuptools-scm python-wheel)
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('b4762359978fd81a2b4b666e6dca15266bdc65680d06900c4da34243f35e4b5d')


build() {
  cd $pkgname-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $pkgname-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  # license
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
  # documentation
  install -Dm644 CHANGELOG.md CONTRIBUTING.md README.rst \
    -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 img/*.svg -t "$pkgdir"/usr/share/doc/$pkgname/img
  install -Dm644 examples/* -t "$pkgdir"/usr/share/doc/$pkgname/examples
}

# vim:set ts=2 sw=2 et:
