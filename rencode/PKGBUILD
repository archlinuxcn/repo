# Contributor: Bug <bug2000@gmail.com>
# Maintainer: Bug <bug2000@gmail.com>
pkgname=rencode
pkgver=1.0.5
pkgrel=1
pkgdesc="Module similar to bencode from the BitTorrent project"
arch=('i686' 'x86_64')
url="https://github.com/aresch/rencode"
license=('GPL3')
conflicts=('xpra-winswitch<=0.17.4' 'xpra-winswitch-svn<=13296')
depends=('python2')
makedepends=('cython2')
source=("https://github.com/aresch/rencode/archive/v$pkgver.tar.gz")
md5sums=('3bdbec5c50d845e5367ba53c5b85d1a4')

build() {
  cd "$pkgname-$pkgver"
  python2 setup.py build || return 1
}

package() {
  cd "$pkgname-$pkgver"
  python2 setup.py install --root=${pkgdir} || return 1
}

# vim:set ts=2 sw=2 et:
