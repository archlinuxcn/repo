_name=Telethon
pkgname=python-telethon
pkgver=1.10.8
pkgrel=9
pkgdesc="Full-featured Telegram client library for Python 3"
arch=(any)
url="https://github.com/LonamiWebs/Telethon"
license=(MIT)
depends=('python-pyaes' 'python-rsa')
makedepends=('python-setuptools')

source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('af88697e2e2faf724dd8c42ff50842bfaa6631f55ea3f8fc35ceb1dda6c11fec')

build() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}


