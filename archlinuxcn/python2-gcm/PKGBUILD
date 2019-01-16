# Maintainer: Felix Yan <felixonmars@gmail.com>

pkgname=python2-gcm
pkgver=0.1.5
pkgrel=1
pkgdesc="Python client for Google Cloud Messaging for Android (GCM)"
arch=('any')
url="https://github.com/geeknam/python-gcm"
license=('custom')
depends=('python2')
makedepends=('python2-setuptools')
source=("http://pypi.python.org/packages/source/p/python-gcm/python-gcm-$pkgver.tar.gz")

build() {
  cd python-gcm-$pkgver
  python2 setup.py build
}

package() {
  cd python-gcm-$pkgver
  python2 setup.py install --root="$pkgdir/"
  install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

sha512sums=('bb7993d9674ddb6a5b2296105e0ea4ac4b1e980d7078922a8e9cf20c3e4ab60bc3d8b04ee417a9df93fc9e13a5d26908fe4e370b2841e214e114f0fa8fea0668')
