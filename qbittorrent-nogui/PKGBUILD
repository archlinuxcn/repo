# Maintainer: Vlad M. <vlad@archlinux.net>
# Contributor: Martin Villagra <mvillagra0@gmail.com>

pkgname=qbittorrent-nogui
_pkgname=qBittorrent
pkgver=3.3.0
pkgrel=1
pkgdesc="A bittorrent client based on Qt5 toolkit and libtorrent-rasterbar, w/o gui"
arch=('i686' 'x86_64')
url="http://www.qbittorrent.org/"
license=('GPL')
depends=('boost-libs'
         'libtorrent-rasterbar'
         'qt5-base')
makedepends=('boost'
             'qt5-tools'
             'which')
conflicts=('qbittorrent-git-nogui')
source=("https://github.com/qbittorrent/qBittorrent/archive/release-$pkgver/$_pkgname-$pkgver.tar.gz"
        'qbittorrent.service')
sha256sums=('24e77c94392dd88ecb39f82645d8611eb6a9b434ca20ae9683c573b802aaf921'
            '912bb191cd942131b23d6d6b9a53d2dbbcd86247c3236f68e62c2c1e13393942')

build() {
  cd "$_pkgname-release-$pkgver"
  ./configure --prefix=/usr --disable-gui
  make
}

package() {
  cd "$_pkgname-release-$pkgver"
  make INSTALL_ROOT="$pkgdir/" install

  install -Dm755 "$srcdir/qbittorrent.service" "$pkgdir/usr/lib/systemd/system/qbittorrent.service"
}
