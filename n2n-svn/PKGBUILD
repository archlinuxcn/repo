# Contributor: Andreas B. Wagner <AndreasBWagner@pointfree.net>
pkgname=n2n-svn
pkgver=r4591
pkgrel=1
pkgdesc='n2n is a layer-two peer-to-peer virtual private network (VPN) which allows users to exploit features typical of P2P applications at network instead of application level.'
arch=('i686' 'x86_64')
url="http://www.ntop.org/products/n2n/"
license=('GPL3')
makedepends=('subversion')
provides=('n2n')
install="n2n.install"

source=("$pkgname"::"svn+https://svn.ntop.org/svn/ntop/trunk/n2n/n2n_v2#revision=4591")
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
  make PREFIX="$pkgdir/usr/" install
}
