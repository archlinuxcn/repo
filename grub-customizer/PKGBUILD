# Maintainer: David Runge <dave@sleepmap.de>

pkgname=grub-customizer
pkgver=5.0.6
pkgbranch=5.0
pkgrel=3
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
md5sums=('9c8f40bfbe0476c57bf6269ba5c9535c'
         'f914f23d66341925238fd0d1922d2b85')
package(){
  cd "$srcdir"/$pkgname-$pkgver/
  msg "Starting make..."
  cmake -DCMAKE_INSTALL_PREFIX=/usr .&& make
  make install DESTDIR=${pkgdir} || return 1
  msg "Modifying grub-customizer.desktop file..."
  sed -i -e '/^Categories=/s/Settings/GTK/' \
    -e '/^X-Ubuntu/d' \
    -e '/^X-KDE/d' "$pkgdir"/usr/share/applications/grub-customizer.desktop
  msg "Installing custom config to: /etc/grub-customizer/grub.cfg"
  install -d ${pkgdir}/etc/grub-customizer
  install -Dm644 ${srcdir}/grub.cfg ${pkgdir}/etc/grub-customizer/grub.cfg
  msg "Installing changelog to: /usr/share/doc/grub-customizer/CHANGELOG"
  install -d ${pkgdir}/usr/share/doc/grub-customizer/
  install -Dm644 changelog ${pkgdir}/usr/share/doc/grub-customizer/CHANGELOG
}
# vim:set ts=2 sw=2 et:
