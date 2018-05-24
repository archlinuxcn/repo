# $Id: PKGBUILD 266875 2017-11-15 14:29:11Z foutrelis $
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: David Rosenstrauch <darose@darose.net>

pkgname=qps
pkgver=1.10.18
pkgrel=1
pkgdesc="a visual process manager, an X11 version of 'top' or 'ps'."
url="https://github.com/lxqt/qps"
depends=('qt5-x11extras' 'qt5-tools')
makedepends=('cmake')
arch=('x86_64')
license=("GPL")
source=("$pkgname-$pkgver.tar.xz::https://github.com/QtDesktop/qps/releases/download/$pkgver/$pkgname-$pkgver.tar.xz"
	"qps.desktop")
sha256sums=('5142647be1bdee0ed4a4a1785a9aa79f817dbd9ae63c7cc7f42be6d0b4a4e3fe'
            '5216455ce5ce096b36f1b301325fd44c972ff796aa3b40b60807a06dae0ab3f9')

build() {
  cd "$srcdir"/$pkgname-$pkgver
  cmake .
  make
}

package() {
  cd "$srcdir"/$pkgname-$pkgver
  install -D -m 755 src/qps "$pkgdir"/usr/bin/qps
  install -D -m 644 qps.1 "$pkgdir"/usr/share/man/man1/qps.1
  install -D -m 644 "$srcdir"/qps.desktop "$pkgdir"/usr/share/applications/qps.desktop
  install -D -m 644 icon/icon.xpm "$pkgdir"/usr/share/pixmaps/qps.xpm
}

sha256sums=('8454582a6f709c173a50c5671c91cb9fc658271617263d12025d2575ee40f35f'
            '5216455ce5ce096b36f1b301325fd44c972ff796aa3b40b60807a06dae0ab3f9')
