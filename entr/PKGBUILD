# Maintainer: Veeti Paananen <veeti.paananen@rojekti.fi>
pkgname=entr
pkgver=4.1
pkgrel=1
pkgdesc="Run arbitrary commands when files change"
arch=('i686' 'x86_64')
url="http://entrproject.org/"
license=('MIT')
depends=('glibc')
source=("https://bitbucket.org/eradman/entr/get/entr-$pkgver.tar.gz")
sha256sums=('c503c93ccffc1e6b2da979cdcb88c5a686e261103501eede7077fa089cdfef78')

# bad tar
_srcdir='eradman-entr-f4e2cbe57708'

build() {
  cd "$srcdir/$_srcdir"

  ./configure
  make
}

check() {
  cd "$srcdir/$_srcdir"

  make -k test
}

package() {
  cd "$srcdir/$_srcdir"

  make PREFIX="$pkgdir/usr" install
  install -D -m 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
