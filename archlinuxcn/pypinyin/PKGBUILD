# Maintainer: Štěpán Němec <stepnem@gmail.com>

pkgname=pypinyin
pkgver=0.40.0
pkgrel=1
pkgdesc='Chinese characters transliteration module and tool'
arch=('any')
url='https://github.com/mozillazg/python-pinyin'
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('3f48d8fd4e7a5c887be333bb3eac07b7072118cf39f118174cdbd1797d9ec5b3')

build() {
  cd "$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
