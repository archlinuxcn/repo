# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-uao
_pkgname=pyUAO
pkgver=0.2.0
pkgrel=2
pkgdesc='Big5-UAO table in pure Python'
arch=(any)
url='https://github.com/eight04/pyUAO'
license=(MIT)
depends=(python)
makedepends=(python-setuptools)
source=("https://github.com/eight04/pyUAO/archive/v$pkgver/$_pkgname-$pkgver.tar.gz")
sha256sums=('15e070230c9478692ee4923d312bda813df4dd37878f4af13c40a6fc7a7db4b8')

build() {
  cd $_pkgname-$pkgver
  python setup.py build
}

check() {
  cd $_pkgname-$pkgver
  python test.py
}

package() {
  cd $_pkgname-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
