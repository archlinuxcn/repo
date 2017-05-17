# Contributor: lucck <lucck@ep.com.pl>
# Maintainer: aksr <aksr at t-com dot me>
pkgname=udftools
pkgver=1.3
pkgrel=1
pkgdesc="Linux tools for UDF filesystems and DVD/CD-R(W) drives"
url="https://github.com/pali/udftools"
arch=('i686' 'x86_64')
license=(GPL)
depends=('ncurses' 'readline')
source=("https://github.com/pali/$pkgname/releases/download/$pkgver/$pkgname-${pkgver}.tar.gz")
options=(!libtool)
md5sums=('0a7d470730fe293157fd17a1a2742b1a')
sha1sums=('be2eb698bccbc5a048753f92fc13877b0c791029')
sha256sums=('00562a440de7b855df8127f8f798df657d53f20d9a205a7041fed37c8a07d4cb')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr --mandir=/usr/share/man --sbindir=/usr/bin
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make -C "$srcdir/$pkgname-$pkgver" DESTDIR="$pkgdir" install
  mkdir -p $pkgdir/usr/share/licenses/$pkgname
  mv $pkgdir/usr/share/doc/$pkgname/COPYING $pkgdir/usr/share/licenses/$pkgname/COPYING
}

