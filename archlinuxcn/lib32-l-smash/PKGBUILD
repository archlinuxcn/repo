# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Gustavo Alvarez <sl1pkn07@gmail.com>

_pkgbasename=l-smash
pkgname=lib32-l-smash
pkgver=2.14.5
pkgrel=1
pkgdesc='MP4 muxer and other tools'
arch=('x86_64')
url='https://github.com/l-smash/l-smash'
license=('custom')
depends=( 'lib32-glibc' 'l-smash')
provides=('liblsmash.so')
source=("l-smash-${pkgver}.tar.gz::https://github.com/l-smash/l-smash/archive/v${pkgver}.tar.gz")
sha256sums=('e6f7c31de684f4b89ee27e5cd6262bf96f2a5b117ba938d2d606cf6220f05935')

build() {
  cd l-smash-${pkgver}
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  ./configure \
    --prefix='/usr' \
    --libdir=/usr/lib32 \
    --cc="gcc -m32" \
    --enable-shared \
    --disable-static \
    --extra-cflags="$CFLAGS" \
    --extra-ldflags="$LDFLAGS"
  make
}

package() {
  cd l-smash-${pkgver}

  make DESTDIR="${pkgdir}" install

  # Keep files in bin since this is not a library only package. 
  # Use the same naming scheme as proposed in Arch's wiki:  https://wiki.archlinux.org/index.php/32-bit_package_guidelines
  # which is "--program-suffix="-32" with Autoconf
  for i in "${pkgdir}/usr/bin/"*; do
    mv "$i" "$i"-32
  done

  rm -rf "${pkgdir}"/usr/include

  install -dm 755 "${pkgdir}"/usr/share/licenses/"${pkgname}"
  ln -s /usr/share/licenses/l-smash/LICENSE "${pkgdir}"/usr/share/licenses/"${pkgname}"
}

# vim: ts=2 sw=2 et:
