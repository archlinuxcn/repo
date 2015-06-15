# Maintainer: M0Rf30

pkgname=whatweb
pkgver=0.4.7
pkgrel=2
pkgdesc="Next generation web scanner that identifies what websites are running."
arch=('i686' 'x86_64')
url="http://www.morningstarsecurity.com/research/whatweb"
license=('GPL')
depends=('ruby1.8')
conflicts=('whatweb-git')
source=("http://www.morningstarsecurity.com/downloads/$pkgname-$pkgver.tar.gz")

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR=$pkgdir
  sed 's#/usr/bin/env ruby#/usr/bin/ruby-1.8#g' -i ${pkgdir}/usr/bin/whatweb
}

md5sums=('c1bdbc4a6d757f2aa3172b2c8c8c8be9')
