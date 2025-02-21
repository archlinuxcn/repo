#Maintainer Yury Bobylev <bobilev_yury@mail.ru>
pkgname="mylibrary"
pkgver="3.2"
pkgrel="2"
pkgdesc="Home librarian"
arch=('x86_64')
provides=("${pkgname}")
source=("https://github.com/ProfessorNavigator/mylibrary/archive/refs/tags/v3.2.tar.gz" "icu_76_cmake.patch")
url="https://github.com/ProfessorNavigator/mylibrary"
license=('GPLv3')
makedepends=('cmake' 'pkgconf' 'gcc')
depends=('gtkmm-4.0' 'icu' 'libgcrypt' 'poppler' 'djvulibre' 'libarchive' 'onetbb')
sha256sums=('8164fa32eec3d8e9f0dd985825d168b1619596c7d6bc870dbdc3339d26cbea91'
            '27d9d85103ede8ac105dc9301eea29ae24e528b64bdff545511667f38830da2d')

prepare() {
    cd $pkgname-$pkgver
    patch -Np1 -i ../icu_76_cmake.patch
}


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
