_name=threadpoolctl
pkgname=python-threadpoolctl
pkgver=1.1.0
pkgrel=4
pkgdesc="threadpoolctl"
arch=(any)
url="https://github.com/joblib/threadpoolctl"
license=(BSD)
depends=('python' 'python-setuptools')

source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('86f330c5ead7fd2d2143e76c4a4cc032d5a2f9cd4c4857fa06847cae2211ab82')

build() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}


