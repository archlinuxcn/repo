# Maintainer: Alexej Magura <sickhadas.nix*gmail*>
#
#
pkgname=libtinfo
pkgver=6
pkgrel=4
pkgdesc="symlink to ncurses for use in cuda and other packages"
arch=('any')
url="http://www.gnu.org/software/ncurses/"
license=('unknown')
conflicts=('libtinfo-5')
depends=('ncurses>=6.0')
_ncurses="$(pacman -Q ${depends[0]/>*/} | awk '{sub(/-[0-9]+/, "", $2); print $2}')"

package() {
  install -d "$pkgdir"/usr/lib
  ln -s /usr/lib/libncursesw.so."$_ncurses" -T "$pkgdir"/usr/lib/libtinfo.so."$pkgver"
  ln -s /usr/lib/libtinfo.so."$pkgver" -T "$pkgdir"/usr/lib/libtinfo.so
}
