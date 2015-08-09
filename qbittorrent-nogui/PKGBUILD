# Maintainer: Vlad M. <vlad@archlinux.net>
# Contributor: Martin Villagra <mvillagra0@gmail.com>

pkgname=qbittorrent-nogui
_pkgname=qbittorrent
pkgver=3.2.3
pkgrel=1
pkgdesc="A bittorrent client based on Qt4 toolkit and libtorrent-rasterbar, w/o gui"
arch=('i686' 'x86_64')
url="http://www.qbittorrent.org/"
license=('GPL')
depends=('boost-libs'
         'libtorrent-rasterbar'
         'qt4')
makedepends=('boost'
             'which')
conflicts=('qbittorrent-git-nogui')
source=("http://downloads.sourceforge.net/sourceforge/${_pkgname}/${_pkgname}-${pkgver}.tar.xz"
        'qbittorrent.service')
sha256sums=('86a79f3772bd06736a4be104180187d76c5c8feb2c1cdf1054135b4ba602a914'
            'be7b259e25cf8badb124672a7e9b3941708f17fd437089a72e838c599405a50c')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  ./configure --prefix=/usr --disable-gui
  make
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make INSTALL_ROOT=${pkgdir} install

  install -Dm755 "$srcdir/qbittorrent.service" "$pkgdir/usr/lib/systemd/system/qbittorrent.service"
}
