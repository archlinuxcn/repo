# Maintainer: gyo <gyo_at_archlinux_dot_fr>
# Contributor: gyo <gyo_at_archlinux_dot_fr>
pkgname=repacman
pkgver=0.98
pkgrel=2
pkgdesc="A tool for producing a pacman package from software's existing installation"
arch=('any')
url="http://archlinuxfr/repacman"
license=('GPL')
source=("http://foulmetal.free.fr/archlinux/$pkgname-$pkgver.tar.gz")
md5sums=('361ea0aca3183a99ac73788c49ef18c7')

package() {
  cd $srcdir
  mkdir -p $pkgdir/usr/bin/
  install -m755 $pkgname $pkgdir/usr/bin/
}
