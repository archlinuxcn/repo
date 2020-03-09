# Maintainer: mark.blakeney at bullet-systems dot net
pkgname=libinput-gestures
pkgver=2.49
pkgrel=1
pkgdesc="Actions gestures on your touchpad using libinput"
url="https://github.com/bulletmark/$pkgname"
license=("GPL3")
arch=("any")
depends=("python>=3.5" "libinput" "xdotool" "wmctrl" "hicolor-icon-theme")
conflicts=("$pkgname-git")
replaces=("$pkgname-git")
backup=("etc/$pkgname.conf")
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
install=install.sh
md5sums=('353fdcf8c28f281fe04757c8a7a8dce7')

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}

# vim:set ts=2 sw=2 et:
