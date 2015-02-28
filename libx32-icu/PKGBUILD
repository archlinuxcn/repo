# Maintainer: josephgbr <rafael.f.f1@gmail.com>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-icu
pkgver=54.1
pkgrel=1.1
pkgdesc="International Components for Unicode library (x32 ABI)"
arch=('x86_64')
url="http://www.icu-project.org/"
license=('custom:icu')
depends=('libx32-gcc-libs' 'icu')
makedepends=('gcc-multilib-x32')
source=(http://download.icu-project.org/files/icu4c/${pkgver}/icu4c-${pkgver//./_}-src.tgz
        'icu.8198.revert.icu5431.patch')
md5sums=('e844caed8f2ca24c088505b0d6271bc0'
         '2e0fb97c7a64ea43c29c6142c22da35a')

build() {
  export CC='gcc -mx32'
  export CXX='g++ -mx32'
  export PKG_CONFIG_PATH='/usr/libx32/pkgconfig'

  cd icu/source

  # fix Malayalam encoding https://bugzilla.redhat.com/show_bug.cgi?id=654200
  patch -Rp3 -i "${srcdir}"/icu.8198.revert.icu5431.patch

  ./configure --prefix=/usr --sysconfdir=/etc --mandir=/usr/share/man --libdir=/usr/libx32

  make
}

check() {
  cd "$srcdir/icu/source"
  make -k check # passes all
}

package() {
  cd icu/source

  make -j1 DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}/usr"/{include,sbin,share}

  # keep icu-config-x32
  find "${pkgdir}/usr/bin" -type f -not -name icu-config -delete
  mv "${pkgdir}/usr/bin"/icu-config{,-x32}

  install -d m644 "${pkgdir}/usr/share/licenses"
  ln -s icu "${pkgdir}/usr/share/licenses/${pkgname}"
}

