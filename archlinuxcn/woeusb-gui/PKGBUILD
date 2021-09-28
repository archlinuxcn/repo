# Maintainer: Alexey Peschany <nelex111@gmail.com>
# Contributor: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Giovanni Harting <539@idlegandalf.com>
# Contributor: aimileus <me at aimileus dot nl>
# Contributor: Salvador Pardiñas <darkfm@vera.com.uy>

pkgname=woeusb-gui
pkgver=3.3.1
pkgrel=1
pkgdesc='A Linux program to create Windows USB stick installer from a Windows DVD or an image'
arch=('x86_64')
url='https://github.com/slacka/WoeUSB'
license=('GPL3')
conflicts=('woeusb')
depends=('dosfstools' 'grub' 'ntfs-3g' 'parted' 'wget' 'wxgtk2')
source=("https://github.com/slacka/WoeUSB/archive/v${pkgver}/woeusb-${pkgver}.tar.gz")
b2sums=('1423ecca39018c674b0eea36de732f54cfcdd14b8cc465e6d3c0639192cbd8355436b7a39ba453b19fa6f1c5b1f6938ef12f49710bc2a4af0f2eaed967e03ce7')

prepare() {
  cd WoeUSB-${pkgver}
  find . -type f -print0 | xargs -0 sed -i "s/@@WOEUSB_VERSION@@/${pkgver}/" || die
  autoreconf --install
}

build() {
  cd WoeUSB-${pkgver}
  ./configure --prefix=/usr
  make
}

package() {
  cd WoeUSB-${pkgver}
  make DESTDIR="${pkgdir}" install
}
