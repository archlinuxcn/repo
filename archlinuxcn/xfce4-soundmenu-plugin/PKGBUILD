# Maintainer: Peter Lamby <peterlamby@web.de>
pkgname=xfce4-soundmenu-plugin
pkgver=0.7.0
pkgrel=2
pkgdesc="A very basic xfce4-panel plugin to control any players MPRIS2 compatible."
arch=('i686' 'x86_64')
url="https://github.com/matiasdelellis/xfce4-soundmenu-plugin"
license=('GPL2')
depends=('xfce4-panel' 'libmpris2client')
makedepends=('intltool')
optdepends=('libclastfm: for Lastfm support'
	'glyr-git: to search lyrics'
	'libkeybinder: for global keyboard shortcuts support'
	'libnotify: Notification support')
source=(https://github.com/matiasdelellis/$pkgname/releases/download/v$pkgver/$pkgname-$pkgver.tar.bz2)
install=$pkgname.install
md5sums=('fe5b914ecc27360b941e3000eac8676e')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --sysconfdir=/etc --libexecdir=/usr/lib 
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install
}
