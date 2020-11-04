# Maintainer: GordonGR <ntheo1979@gmail.com>
# Contributor: Jaroslav Lichtblau <dragonlord@aur.archlinux.org>
# Contributor: Corrado Primier <bardo@aur.archlinux.org>

pkgname=lib32-libreplaygain
_pkgname=libreplaygain
pkgver=475
pkgrel=3
pkgdesc="A library to adjust audio gain (lib32)"
arch=('x86_64')
url="http://www.musepack.net/index.php?pg=src"
license=('LGPL')
depends=('lib32-glibc' "${_pkgname}")
makedepends=('cmake')
source=("http://files.musepack.net/source/${_pkgname}_r${pkgver}.tar.gz")
sha512sums=('b5fce8daf6aa8c8e0adb4c80089b43824b6503cb7d11e0c47c779c57a933b32f0c24722ca3fcf49711199fddcbb92c3fc13876f22418ca1521c7b8e27ba9d409')

build() {
cd "${srcdir}"
mkdir build
cd build
export CC="gcc -m32"
export CXX="g++ -m32"
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

cmake ../${_pkgname}_r${pkgver}/ \
  -DCMAKE_INSTALL_LIBDIR=/usr/lib32 \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DCMAKE_BUILD_TYPE=Release
make
}

package() {
cd "${srcdir}"/build
make DESTDIR="${pkgdir}" install
install -d "${pkgdir}"/usr/include/replaygain/
install -Dm644 "${srcdir}"/${_pkgname}_r${pkgver}/include/replaygain/* \
  "${pkgdir}"/usr/include/replaygain/

cd "$pkgdir/usr"
rm -rf {bin,include,share/imlib2}/
mv lib/ lib32/

}
