# Maintainer: Štěpán Němec <stepnem@gmail.com>

pkgname=pypinyin
pkgver=0.37.0
pkgrel=1
pkgdesc='Chinese characters transliteration module and tool'
arch=('any')
url='https://github.com/mozillazg/python-pinyin'
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('597b9d375bcd1a8a9c9bda7f813d58bd9e148288006f62d34ab2f3a9ff4cba33')

build() {
  cd "$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
