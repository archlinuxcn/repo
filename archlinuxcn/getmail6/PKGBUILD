# Maintainer :  Kr1ss  $(tr +- .@ <<<'<kr1ss+x-yandex+com>')


pkgname=getmail6

pkgver=6.16
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
b2sums=('ddce2bdb7c886f8a732dc603bad823bbd5bc1e449dec8019c606d37f69eb7807a0c7c37ba849451423dbda9459d0f94fbd3e8eb9464fc2320718b51ae5d29d59')


build() {
  cd "$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$pkgname-$pkgver"
  python setup.py install --skip-build --optimize=1 --root="$pkgdir"
}


# vim: ts=2 sw=2 et ft=PKGBUILD:
