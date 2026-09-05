# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Denommus <yuridenommus@gmail.com>
# Contributor: Bill Fraser <wfraser@codewise.org>
# Contributor: Felipe Contreras <felipe.contreras@gmail.com>

pkgname=lib32-flex
pkgver=2.6.4
pkgrel=5
pkgdesc='A tool for generating text-scanning programs'
arch=('x86_64')
url='http://flex.sourceforge.net'
license=('custom')
depends=('flex' 'lib32-glibc')
source=("https://github.com/westes/flex/releases/download/v${pkgver}/flex-${pkgver}.tar.gz")
sha256sums=('e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995')

build() {
  cd flex-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32'
  make
}

package() {
  cd flex-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{include,share,bin}

  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s flex "${pkgdir}"/usr/share/licenses/lib32-flex
}

# vim: ts=2 sw=2 et:
