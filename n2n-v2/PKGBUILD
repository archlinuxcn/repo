# Contributor: Adam Strauch <cx@initd.cz>
pkgname=n2n-v2
pkgver=r8986
pkgrel=1
pkgdesc='n2n is a layer-two peer-to-peer virtual private network (VPN). This is updated PKGBUILD of out-of-date n2n-svn package.'
arch=('i686' 'x86_64' 'armv7h' 'armv6h')
url="http://www.ntop.org/products/n2n/"
license=('GPL3')
makedepends=('subversion')
provides=('n2n')
install="n2n.install"

source=("$pkgname"::"svn+https://svn.ntop.org/svn/ntop/trunk/n2n/n2n_v2#revision=8986")
md5sums=("SKIP")

pkgver() {
   cd "$srcdir/$pkgname"
   local ver="$(svnversion)"
   printf "r%s" "${ver//[[:alpha:]]}"
}

build() {
  cd "$srcdir/$pkgname"
  make
}

package() {
  cd "$srcdir/$pkgname"
  make PREFIX="$pkgdir/usr/" SBINDIR="$pkgdir/usr/bin/" install
}
