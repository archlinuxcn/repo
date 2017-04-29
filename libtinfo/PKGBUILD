# Maintainer: Alexej Magura <sickhadas.nix*gmail*>
#
#
pkgname=libtinfo
pkgver=6
pkgrel=21
pkgdesc="symlink to ncurses for use in cuda and other packages"
arch=('any')
url="http://www.gnu.org/software/ncurses/"
license=('MIT')
#conflicts=('libtinfo-5')
depends=('ncurses>=6.0')
#optdepends=('libtinfo5: ncurses5-compat-libs')
#_ncurses="$(pacman -Q ncurses | awk '{print $2}' | cut -c 1-3)"
#_libtinfo5="$(pacman -Q ncurses5-compat-libs > /dev/null 2>&1; echo $?)"

package() {
  install -d "$pkgdir"/usr/lib
  ln -s /usr/lib/libncursesw.so."$_ncurses" "$pkgdir"/usr/lib/libtinfo.so."$pkgver"
  ln -s /usr/lib/libtinfo.so."$pkgver" "$pkgdir"/usr/lib/libtinfo.so

  #msg "Is ncurses5-compat-libs present..."

  #if ! ((_libtinfo5)); then
    #msg "\tyes"
    #msg "Do we need to symlink to it..."
    #if [[ -f /usr/lib/libtinfo.so.5 ]]; then
      #msg "\tno"
    #else
      #msg "\tyes"
      #ln -s /usr/lib/libncurses.so.5 "$pkgdir"/usr/lib/libtinfo.so.5
    #fi
  #else
    #msg "\tno"
  #fi
}

#package_lib32_libtinfo() {
#  install -d "$pkgdir"/usr/lib32
#  ln -s /usr/lib32/libncursesw.so."$_ncurses" "$pkgdir"/usr/lib32/libtinfo.so."$pkgver"
#  ln -s /usr/lib32/libtinfo.so."$pkgver" "$pkgdir"/usr/lib32/libtinfo.so
#  ln -s /usr/lib32/libtinfo.so."$pkgver" "$pkgdir"/usr/lib32/libtinfo.so.5
#}
