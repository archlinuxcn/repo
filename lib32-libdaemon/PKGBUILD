# Maintainer: Gicu Gorodenco <cyclopsihus 'at' gmail 'dot' com>
# Contributor: rafael ff1 <rafael.f.f1 'at' gmail 'dot' com> 
_pkgbasename=libdaemon
pkgname=lib32-$_pkgbasename
pkgver=0.14
pkgrel=4
pkgdesc="A lightweight C library which eases the writing of UNIX daemons (32 bit, library only)"
arch=('x86_64')
# Temporary Down :
#url="http://0pointer.de/lennart/projects/libdaemon/"
url="http://pkgs.fedoraproject.org/repo/pkgs/libdaemon/libdaemon-0.14.tar.gz/509dc27107c21bcd9fbf2f95f5669563"
license=('LGPL')
depends=('lib32-glibc' "$_pkgbasename")
makedepends=('gcc-multilib')
options=('!libtool')
source=(${url}/$_pkgbasename-$pkgver.tar.gz)
md5sums=('509dc27107c21bcd9fbf2f95f5669563')

build() {
  cd $srcdir/$_pkgbasename-$pkgver
  ./configure --prefix=/usr --localstatedir=/var --disable-lynx \
  				--libdir=/usr/lib32 CC='gcc -m32'
  make
}

package() {
  cd $srcdir/$_pkgbasename-$pkgver
  make DESTDIR=$pkgdir install
  # Cleanup for lib32 package
  rm -rf ${pkgdir}/usr/{include,share,lib32/$_pkgbasename.a}
  # Install license
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/$pkgname/LICENSE
}
