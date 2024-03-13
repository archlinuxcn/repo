#Maintainer Yury Bobylev <bobilev_yury@mail.ru>
pkgname="mylibrary"
pkgver="3.0.2"
pkgrel="1"
pkgdesc="Home librarian"
arch=('x86_64')
provides=("${pkgname}")
source=("https://github.com/ProfessorNavigator/mylibrary/archive/refs/tags/v3.0.2.tar.gz")
url="https://github.com/ProfessorNavigator/mylibrary"
license=('GPLv3')
makedepends=('meson' 'pkgconf' 'gcc')
depends=('gtkmm-4.0' 'icu' 'libgcrypt' 'poppler' 'djvulibre' 'libarchive')
sha256sums=('661daf6a1cf152021c9685cc3abe856c3f25c513b3fd38aee73a51274eeb9f08')

build() {   
   mkdir -p $srcdir/builddir
   cd $srcdir/$pkgname-$pkgver   
   meson setup -Dbuildtype=release -Dprefix=/usr $srcdir/builddir
   cd $srcdir/builddir
   ninja      
}

package() {
    cd $srcdir/builddir
    DESTDIR=$pkgdir ninja install        
}
