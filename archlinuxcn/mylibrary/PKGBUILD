#Maintainer Yury Bobylev <bobilev_yury@mail.ru>
pkgname="mylibrary"
pkgver="3.1.1"
pkgrel="1"
pkgdesc="Home librarian"
arch=('x86_64')
provides=("${pkgname}")
source=("https://github.com/ProfessorNavigator/mylibrary/archive/refs/tags/v3.1.1.tar.gz")
url="https://github.com/ProfessorNavigator/mylibrary"
license=('GPLv3')
makedepends=('cmake' 'pkgconf' 'gcc')
depends=('gtkmm-4.0' 'icu' 'libgcrypt' 'poppler' 'djvulibre' 'libarchive' 'onetbb')
sha256sums=('57aa411830e79ea91a66a87992bea3cb567fc59cd61c3f3f7bb0611607209681')

build() {   
   mkdir -p $srcdir/builddir
   cd $srcdir/$pkgname-$pkgver   
   cmake -DCMAKE_BUILD_TYPE=release \
   -DCMAKE_INSTALL_PREFIX=/usr \
   -DUSE_OPENMP=ON \
   -DUSE_TBB=ON \
   -B$srcdir/builddir
   cd $srcdir/builddir
   make -j$(nproc)
}

package() {
    cd $srcdir/builddir
    DESTDIR=$pkgdir make install
}
