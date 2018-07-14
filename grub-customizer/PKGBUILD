# Maintainer: David Runge <dave@sleepmap.de>

pkgname=grub-customizer
pkgver=5.0.8
pkgrel=1
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
sha512sums=('ce8a4893fd4591ad2319009421f91f97f2e977b5198bf3c6b73e89c022f38bbbdec12e930984fd9167df9f8587f58b13d2296c6d92cd1cc8a179380dc0747975'
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
