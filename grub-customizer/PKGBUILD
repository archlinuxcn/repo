# Maintainer: David Runge <dave@sleepmap.de>

pkgname=grub-customizer
pkgver=5.0.6
pkgbranch=5.0
pkgrel=4
pkgdesc="A graphical grub2 settings manager"
url="https://launchpad.net/grub-customizer"
arch=('i686' 'x86_64')
license=("GPL3")
depends=('gtkmm3' 'openssl' 'hicolor-icon-theme' 'grub-common' 'libarchive' )
optdepends=('hwinfo')
makedepends=('cmake')
provides=(grub-customizer)
backup=('etc/grub-customizer/grub.cfg')
options=()
install=${pkgname}.install
source=("https://launchpad.net/${pkgname}/${pkgbranch}/${pkgver}/+download/${pkgname}_${pkgver}.tar.gz" \
        grub.cfg)
sha512sums=('4bf29daac0c34b38179866b30ab035f54cd6156c3fbe333d7c0b0f7e715ab047201006fe1cab29d53126a1170f9990e2c69e426fb0f2d43a48d6337e8ba3079d'
            '40156b6546a4d7e8abbef2ab3dece0481a4a2ca276b9a15c5a7bf7e3b11004335b6a747be391b5c1accb35c9e9e3bc628e571cd245e5f2980e5ecd6a3ceb24f5')

package(){
  cd "$srcdir"/$pkgname-$pkgver/
  cmake -DCMAKE_INSTALL_PREFIX=/usr .&& make
  make install DESTDIR=${pkgdir} || return 1

  # modifying desktop file
  sed -i -e '/^Categories=/s/Settings/GTK/' \
    -e '/^X-Ubuntu/d' \
    -e '/^X-KDE/d' \
    "${pkgdir}/usr/share/applications/grub-customizer.desktop"

  # configuration
  install -d ${pkgdir}/etc/grub-customizer
  install -Dm644 ${srcdir}/grub.cfg ${pkgdir}/etc/grub-customizer/grub.cfg

  # CHANGELOG
  install -d ${pkgdir}/usr/share/doc/grub-customizer/
  install -Dm644 changelog ${pkgdir}/usr/share/doc/grub-customizer/CHANGELOG
}
# vim:set ts=2 sw=2 et:
