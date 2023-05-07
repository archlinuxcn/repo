# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: WorMzy Tykashi <wormzy.tykashi@gmail.com>
pkgname=python-pulsectl
_name=${pkgname#python-}
pkgver=23.5.1
pkgrel=1
epoch=1
pkgdesc="Python high-level interface and ctypes-based bindings for PulseAudio (libpulse)"
arch=('any')
url="https://github.com/mk-fg/python-pulse-control"
license=('MIT')
depends=('python' 'libpulse')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
conflicts=('python-pulse-control')
replaces=('python-pulse-control')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('8efc260ed7212ee4f9e50a8b856c84911265f4eac42cc6c02c7b37c851a2834b')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname/"
}
