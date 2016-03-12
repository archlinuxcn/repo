# Maintainer: Vlad M. <vlad@archlinux.net>
# Contributor: Martin Villagra <mvillagra0@gmail.com>

pkgname=qbittorrent-nogui
_pkgname=qBittorrent
pkgver=3.3.3
pkgrel=2
pkgdesc="A bittorrent client based on Qt toolkit and libtorrent-rasterbar, w/o gui"
arch=('i686' 'x86_64')
url="http://www.qbittorrent.org"
license=('GPL')
depends=('libtorrent-rasterbar'
         'qt5-base')
makedepends=('boost'
             'qt5-tools')
conflicts=('qbittorrent-git-nogui')
source=("https://github.com/qbittorrent/qBittorrent/archive/release-$pkgver/$_pkgname-$pkgver.tar.gz"
        'qbittorrent.service'
        'qbittorrent@.service')
sha256sums=('04f03623be427294238f119d1ab3311e8560a091778f12df03cc9380fad2c6d9'
            '8c5879673c66368ada97f6d70a1d8fe3b6a4995f79aab4fc6bf54fbdcbe811d0'
            '12dfd06104eaf302b79328c8096248c051208f69348e33f7fb2e4a2fb49caa29')

build() {
  cd "$_pkgname-release-$pkgver"
  ./configure --prefix=/usr --disable-gui
  make
}

package() {
  cd "$_pkgname-release-$pkgver"
  make INSTALL_ROOT="$pkgdir/" install

  install -Dm755 "$srcdir/qbittorrent.service" "$pkgdir/usr/lib/systemd/user/qbittorrent.service"
  install -Dm755 "$srcdir/qbittorrent@.service" "$pkgdir/usr/lib/systemd/system/qbittorrent@.service"
}
