# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: schuay <jakob.gruber@gmail.com>
# Contributor: quantax -- contact via Arch Linux forum or AUR
# Contributor: Christoph Zeiler <archNOSPAM_at_moonblade.dot.org>

pkgname=pcsxr
pkgver=1.9.95
pkgrel=1
pkgdesc="A Sony PlayStation (PSX) emulator based on the PCSX-df project"
arch=("i686" "x86_64")
url="http://${pkgname}.codeplex.com"
license=("GPL")
depends=("gtk3" "libarchive" "libcdio" "libnsl" "libxv" "sdl2")
makedepends=("cmake" "intltool" "mesa" "nasm" "valgrind")
conflicts=("pcsx-df")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/frealgagu/PCSX-Reloaded/archive/${pkgver}.tar.gz"
        "${pkgname}-desktop.patch"
        "${pkgname}-fix-undefined-operations.patch"
        "${pkgname}-remove-assertion-64bit.patch"
        "${pkgname}-fix-uncompress2.patch")
md5sums=("ee0f9dfd003d9a5350aafc8cca0cdeee"
         "29bc686e8b68d128796deef60ac1efe1"
         "96a82dcc66851160f452160a538cd6f8"
         "c3ed7fc2a5e395a11f860c305522cb7b"
         "19a8be752dceb236a82e24eefd7e03cb")

prepare() {
  cd "${srcdir}/PCSX-Reloaded-${pkgver}"
  
  patch -Np1 -i "${srcdir}/${pkgname}-desktop.patch"
  patch -Np1 -i "${srcdir}/${pkgname}-fix-undefined-operations.patch"
  patch -Np1 -i "${srcdir}/${pkgname}-remove-assertion-64bit.patch"
  patch -Np1 -i "${srcdir}/${pkgname}-fix-uncompress2.patch"
  mkdir "${srcdir}/PCSX-Reloaded-${pkgver}/${pkgname}/include"
}

build() {
  cd "${srcdir}/PCSX-Reloaded-${pkgver}/${pkgname}"

  autoreconf -f -i
  intltoolize --force

  ./configure \
    --prefix=/usr \
    --enable-libcdio \
    --enable-opengl
  make
}

package() {
  cd "${srcdir}/PCSX-Reloaded-${pkgver}/${pkgname}"
  make DESTDIR="${pkgdir}" install
}
