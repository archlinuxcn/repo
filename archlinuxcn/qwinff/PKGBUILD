# Maintainer: Che-Huai Lin <lzh9102@gmail.com>
pkgname=qwinff
pkgver=0.2.1
pkgrel=1
pkgdesc="A Qt4/5 GUI frontend for ffmpeg"
arch=('i686' 'x86_64')
url="http://qwinff.github.io/downloads.html"
license=('GPL3')
depends=('ffmpeg' 'qt5-base')
optdepends=('sox: audio speed adjusting support'
				'libnotify: display desktop notifications'
				'mplayer: video cutting preview')
source=(http://sourceforge.net/projects/${pkgname}/files/release/v${pkgver}/${pkgname}_${pkgver}.tar.bz2)
sha256sums=('5a3829a482a0c5f9fda3cf6680bff5941f1a6f1661187f3aae73983ec2113975')

build() {
  cd "$srcdir/${pkgname}-${pkgver}"
  make clean
  make QMAKE=qmake-qt5 LRELEASE=lrelease-qt5 PREFIX=/usr
}

package() {
  cd "$srcdir/${pkgname}-${pkgver}"
  make DESTDIR="$pkgdir/" install
}
