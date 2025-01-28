# Maintainer: Alfred Dupont <alfred.dupont@no.email>
# Contributor: Daniel M. Capella <polyzen@archlinux.org>

_name=flake8-bugbear
pkgname=python-flake8-bugbear
pkgver=24.12.12
pkgrel=1
pkgdesc='Plugin for Flake8 finding likely bugs and design problems in your program'
arch=('any')
url=https://github.com/PyCQA/flake8-bugbear
license=('MIT')
depends=('flake8' 'python-attrs')
makedepends=('flake8' 'python-attrs' 'python-setuptools' 'python-build' 'python-installer' 'python-wheel')
checkdepends=('python-hypothesmith')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('d75076b384ce030e094f5e77130462004aaee9ac3b82293c5b3e07da6972a3e05673e77bfd078b416491fa8e7888c8a391c703630065fa13d908da660ba7be07')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd $_name-$pkgver
  python -m tests.test_bugbear
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 -t "$pkgdir"/usr/share/licenses/$pkgname LICENSE
}

# vim:set ts=2 sw=2 et:
