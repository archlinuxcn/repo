# Maintainer: Morgenstern <charles [at] charlesbwise [dot] com>
# Contributor: Alexander Rødseth <rodseth@gmail.com>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Stefan Husmann  <stefan-husmann@t-online.de>
# Contributor: Manuel "ekerazha" C. (www.ekerazha.com)

_pyname=configobj
pkgname=('python2-configobj')
pkgver=5.0.6
pkgrel=6
pkgdesc='Simple but powerful Python config file reader and writer, python2 version'
arch=('any')
url="https://github.com/DiffSK/configobj"
license=('BSD')
depends=('python2-six')
makedepends=('python2')
source=("$pkgname-$pkgver.tar.gz::https://github.com/DiffSK/configobj/archive/v$pkgver.tar.gz")
sha256sums=('2e140354efcca6f558ff9ee941b435ae09a617bc071797bef62c8d6ed2033d5e')

package() {
  cd "$_pyname-$pkgver"
  python2 setup.py install --root="$pkgdir" --optimize=1
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
