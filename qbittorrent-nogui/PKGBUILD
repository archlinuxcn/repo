# Mantainer: Martin Villagra <mvillagra0@gmail.com>

pkgname=qbittorrent-nogui
pkgver=3.1.12
pkgrel=1
pkgdesc="A bittorrent client written in C++ / Qt4 using the good libtorrent library, w/o gui, stable version"
arch=('i686' 'x86_64')
url="http://www.qbittorrent.org/"
license=('GPL')
depends=('libtorrent-rasterbar' 'boost-libs' 'qt4')
makedepends=('boost' 'which')
conflicts=('qbittorrent-git-nogui')
source=("http://downloads.sourceforge.net/sourceforge/qbittorrent/qbittorrent-${pkgver}.tar.xz"
        'qbittorrent.service')

build() {
  cd  "${srcdir}/${pkgname/-nogui/}-${pkgver}"
  ./configure --prefix=/usr --disable-gui
  make
}

package() {
  cd  "${srcdir}/${pkgname/-nogui/}-${pkgver}"
  make INSTALL_ROOT=${pkgdir} install

  install -D -m0755 "$srcdir/qbittorrent.service" "$pkgdir/usr/lib/systemd/system/qbittorrent.service"
}
sha256sums=('d5d5b27958297f0b14cf03af8dd24a0d2a990e108c9a7a6159e4a2fbb1111c83'
            'be7b259e25cf8badb124672a7e9b3941708f17fd437089a72e838c599405a50c')
