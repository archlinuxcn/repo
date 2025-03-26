#Maintainer Yury Bobylev <bobilev_yury@mail.ru>
pkgname="mylibrary"
pkgver="3.2"
pkgrel="3"
pkgdesc="Home librarian"
arch=('x86_64')
provides=("${pkgname}")
source=("https://github.com/ProfessorNavigator/mylibrary/archive/refs/tags/v3.2.tar.gz")
url="https://github.com/ProfessorNavigator/mylibrary"
license=('GPLv3')
makedepends=('cmake' 'pkgconf' 'gcc')
depends=('gtkmm-4.0' 'icu' 'libgcrypt' 'poppler' 'djvulibre' 'libarchive' 'onetbb')
sha256sums=('018c2565177e472cbef3612df0ea140b36b7c3829c9c9e2af609dc981581de00')

build() {   
   mkdir -p $srcdir/builddir
   cd $srcdir/$pkgname-$pkgver   
   cmake -DCMAKE_BUILD_TYPE=release \
   -DCMAKE_INSTALL_PREFIX=/usr \
   -DUSE_OPENMP=ON \
   -DUSE_TBB=ON \
   -B$srcdir/builddir
   make -C $srcdir/builddir -j$(nproc)
}

package() {
    DESTDIR=$pkgdir make -C $srcdir/builddir install
}
