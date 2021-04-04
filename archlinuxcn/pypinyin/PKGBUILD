# Maintainer: Štěpán Němec <stepnem@gmail.com>

pkgname=pypinyin
pkgver=0.41.0
pkgrel=1
pkgdesc='Chinese characters transliteration module and tool'
arch=('any')
url='https://github.com/mozillazg/python-pinyin'
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('1dca63ad22b00c515e5eba2908f602277d9a3cfb47752e150fa1fa0c27670b1b')

build() {
  cd "$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
