# Maintainer: drakkan <nicola.murino@gmail.com>
# Contributor: drakkan <nicola.murino@gmail.com>

pkgname=botan-1.10
pkgver=1.10.9
pkgrel=1
pkgdesc='Crypto library written in C++'
license=('BSD')
arch=('x86_64' 'i686')
url='http://botan.randombit.net/'
depends=('gcc-libs' 'sh')
makedepends=('python2')
source=("http://botan.randombit.net/releases/Botan-${pkgver}.tgz")
sha256sums=('487d27d3a081ae403cf87c0fc78c2a64183f001b48f9feb87e8de1e16fba8df2')

build() {
  cd "Botan-$pkgver"

  python2 configure.py --prefix=/usr --enable-modules=cvc
  make 
}

package() {
  cd "Botan-$pkgver"

  make DESTDIR="$pkgdir/usr" install
  find "$pkgdir/usr/share/doc" -type f -exec chmod 0644 {} \;
  install -Dm644 doc/license.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
