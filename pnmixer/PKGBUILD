# $Id: pkgbuild-mode.el,v 1.23 2007/10/20 16:02:14 juergen Exp $
# Maintainer: Nick Lanham <nick@nick>
pkgname=pnmixer
pkgver=0.5.1
pkgrel=2
pkgdesc="PNMixer is a GTK volume mixer applet that runs in the system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
groups=('pnmixer')
depends=('gtk2' 'alsa-lib')

source=(https://github.com/downloads/nicklan/pnmixer/pnmixer-${pkgver}.tar.gz pnmixer-0.5.1-configure.in.patch)
md5sums=('2288af95ab280721b39b7c33601d5dd4'
         'd7aef8eb1cec18858fb2faefe6584276')
build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  patch -Np0 -i ../pnmixer-0.5.1-configure.in.patch
  ./autogen.sh || return 1
  ./configure --prefix=/usr || return 1
  make || return 1
  make DESTDIR="$pkgdir" install || return 1
}
