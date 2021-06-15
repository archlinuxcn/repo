# Maintainer :  Kr1ss  $(tr +- .@ <<<'<kr1ss+x-yandex+com>')


pkgname=getmail6

pkgver=6.17
pkgrel=1

pkgdesc='POP3 mail retriever with reliable Maildir and command delivery; Python 3 port'
arch=('any')
url="http://$pkgname.org"
license=('GPL2')

provides=("getmail=$pkgver")
conflicts=('getmail')

makedepends=('git' 'python-setuptools')
depends=('python-chardet')
optdepends=('python-keyring: secure password store'
            'python-keyrings-alt: alternative backends')

changelog=CHANGELOG
source=("$pkgname-$pkgver.tgz::https://github.com/$pkgname/$pkgname/archive/v$pkgver.tar.gz")
b2sums=('cfb7f2b751d90b5322200496b9d1298261fe9e27207ffc8285d7ebc8b61dbd1a01683b21a75cf7d65455c754e2262cce4dbfb94ccd9cabd1679deaeeb9a0a7a4')


build() {
  cd "$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$pkgname-$pkgver"
  PYTHONHASHSEED=0 python setup.py install --skip-build --optimize=1 --root="$pkgdir"
}


# vim: ts=2 sw=2 et ft=PKGBUILD:
