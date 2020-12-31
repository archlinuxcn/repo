# Maintainer :  Kr1ss  $(tr +- .@ <<<'<kr1ss+x-yandex+com>')


pkgname=getmail6

pkgver=6.12
pkgrel=1

pkgdesc='POP3 mail retriever with reliable Maildir and command delivery; Python 3 port'
arch=('any')
url="http://$pkgname.org"
license=('GPL2')

provides=("getmail=$pkgver")
conflicts=('getmail')

makedepends=('git')
depends=('python-chardet')
optdepends=('python-keyring: secure password store'
            'python-keyrings-alt: alternative backends')

changelog=CHANGELOG
source=("$pkgname-$pkgver.tgz::https://github.com/$pkgname/$pkgname/archive/v$pkgver.tar.gz")
b2sums=('f1d0fd9f5b2020ccdb3506afcfdaf1f153fac79d7dc7ce33100b1565c4a0db73873bea8d71f19c0e82d146f719b55e8a4fc8c65ec6b64d2cf7c90ecbc16bec20')


build() {
  cd "$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$pkgname-$pkgver"
  python setup.py install --skip-build --optimize=1 --root="$pkgdir"
}


# vim: ts=2 sw=2 et ft=PKGBUILD:
