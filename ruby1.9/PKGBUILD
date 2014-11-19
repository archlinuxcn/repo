# Maintainer: Jonne Haß <me@mrzyx.de>
# Contributor: Thomas Dziedzic <gostrc@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: John Proctor <jproctor@prium.net>
# Contributor: Jeramy Rutley <jrutley@gmail.com>

pkgname='ruby1.9'
pkgdesc='An object-oriented language for quick and easy programming'
pkgver=1.9.3_p551
pkgrel=1
arch=('i686' 'x86_64')
url='http://www.ruby-lang.org/en/'
license=('BSD' 'custom')
depends=('openssl' 'libffi' 'libyaml')
optdepends=('tk: for Ruby/TK')
makedepends=('openssl' 'tk' 'libffi' 'doxygen' 'graphviz' 'libyaml')
provides=('rubygems1.9' 'rake1.9')
options=('!emptydirs' '!makeflags')
source=("http://ftp.ruby-lang.org/pub/ruby/${pkgver%.*}/ruby-${pkgver//_/-}.tar.bz2")

build() {
  cd ruby-${pkgver//_/-}

  PKG_CONFIG=/usr/bin/pkg-config ./configure \
    --prefix=/opt/$pkgname \
    --enable-shared \
    --enable-pthread \
    --disable-rpath \
    --program-suffix=-1.9

  make
}

check() {
  cd ruby-${pkgver//_/-}

  make test
}

package() {

  cd ruby-${pkgver//_/-}

  make DESTDIR="${pkgdir}" install-nodoc

  install -dm755 $pkgdir/usr/bin
  install -dm755 $pkgdir/usr/lib

  for i in erb irb rdoc ri ruby testrb rake gem; do
    ln -s /opt/$pkgname/bin/$i-1.9 $pkgdir/usr/bin/$i-1.9
    ln -s /opt/$pkgname/bin/$i-1.9 $pkgdir/opt/$pkgname/bin/$i
  done

  ln -s /opt/$pkgname/lib/libruby.so.1.9 $pkgdir/usr/lib/libruby.so.1.9
  
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
  install -D -m644 BSDL "${pkgdir}/usr/share/licenses/$pkgname/BSDL"
}
sha256sums=('b0c5e37e3431d58613a160504b39542ec687d473de1d4da983dabcf3c5de771e')
