# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

pkgname=winusb
pkgver=1.0.11
pkgrel=4
pkgdesc='Simple tool to create a usb stick installer for Windows (Vista and above)'
arch=('i686' 'x86_64')
url="http://en.congelli.eu/prog_info_winusb.html"
license=('GPL3')
depends=('wxgtk' 'grub' 'ntfs-3g' 'gksu' 'parted' 'webkitgtk2')
makedepends=('diffutils')
source=("ftp://ftp.ru.debian.org/gentoo-distfiles/distfiles/${pkgname}-${pkgver}.tar.gz"
        'findFile.patch')
sha512sums=('4d60aa440b811d6fb0a5bb71155f689f767e976572736c324040651b77bfc58d883a98e95afdef63c3cd97b3a49027a059e8e70ebb1d23ba830d7251ac72ae42'
            '9138201df82ac3f256d3f461f6acfcba708bacfda75f623dc7c7f80bdfd08436404a9bb722f90ead548f0fc4e371d6b612d924ae218a3035418f0229955cd79e')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  patch -Np1 -i "${srcdir}/findFile.patch"
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}

# vim:set ts=2 sw=2 et:
