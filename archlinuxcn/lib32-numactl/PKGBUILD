# Original Contributor Dan McGee <dan@archlinux.org>
# Contributor: Florian Zeitz <florob at babelmonkeys dot de>
# Mantainer:  Lorenzo Ferrillo <lorenzofer at live dot it> 
_basename=numactl
pkgname=lib32-numactl
pkgver=2.0.11
pkgrel=3
pkgdesc="Simple NUMA policy support 32-bit version. Libraries only"
arch=('x86_64')
url="http://oss.sgi.com/projects/libnuma/"
license=('LGPL2.1' 'GPL2')
depends=('perl' 'numactl')
source=('https://sources.archlinux.org/other/packages/numactl/numactl-2.0.11.tar.gz' 'numactl-2.0.11-sysmacros.patch')
sha1sums=('0846670269824078a4eae8a977728175437b0da4' '5a9cff7cf1fe687e5be83de0a512325b923e3e21')

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  patch -Np0 -i numactl-2.0.11-sysmacros.patch
  cd "$srcdir/$_basename-${pkgver/_/-}"
  ./configure --prefix=/usr --libdir=/usr/lib32
  make
}

package() {
  cd "$srcdir/$_basename-${pkgver/_/-}"
  make DESTDIR="$pkgdir" install
  rm -rf "$pkgdir/usr/share/" "$pkgdir/usr/bin/" "$pkgdir/usr/include/"
}
 
