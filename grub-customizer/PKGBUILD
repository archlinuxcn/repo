# Maintainer: David Runge <dave@sleepmap.de>

pkgname=grub-customizer
pkgver=5.0.6
pkgrel=8
pkgdesc="A graphical grub2 settings manager"
url="https://launchpad.net/grub-customizer"
arch=('x86_64')
license=('GPL3')
depends=('grub' 'gtkmm3' 'libarchive')
optdepends=('hwinfo: Additional hardware information'
            'polkit: Run grub-customizer from menu')
makedepends=('cmake')
provides=('grub-customizer')
backup=('etc/grub-customizer/grub.cfg')
source=("https://launchpad.net/${pkgname}/${pkgver%.*}/${pkgver}/+download/${pkgname}_${pkgver}.tar.gz"
        'grub.cfg')
sha512sums=('4bf29daac0c34b38179866b30ab035f54cd6156c3fbe333d7c0b0f7e715ab047201006fe1cab29d53126a1170f9990e2c69e426fb0f2d43a48d6337e8ba3079d'
            '40156b6546a4d7e8abbef2ab3dece0481a4a2ca276b9a15c5a7bf7e3b11004335b6a747be391b5c1accb35c9e9e3bc628e571cd245e5f2980e5ecd6a3ceb24f5')

prepare(){
  cd "${pkgname}-${pkgver}"
  mkdir -p bld
}

build(){
  cd "${pkgname}-${pkgver}/bld"
  cmake .. -DCMAKE_INSTALL_PREFIX=/usr \
           -DCMAKE_CXX_FLAGS=" -std=c++11"
  make
}

package(){
  cd "${pkgname}-${pkgver}/bld"
  make install DESTDIR="${pkgdir}"
  # configuration
  install -vDm 644 "${srcdir}/grub.cfg" -t "${pkgdir}/etc/${pkgname}/"
  # additional documentation
  install -vDm 644 ../{changelog,README} \
    -t "${pkgdir}/usr/share/doc/${pkgname}/"
}
# vim:set ts=2 sw=2 et:
