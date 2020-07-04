# Maintainer: Katherine J. Cumberbatch <stykers@stykers.moe>
pkgname=binfmt-qemu-static
pkgver=20190112
pkgrel=4
pkgdesc="Register qemu-static interpreters for various binary formats"
arch=('any')
url="http://www.freedesktop.org/software/systemd/man/binfmt.d.html"
license=('GPL')
optdepends=('qemu-user-static')
source=("qemu-static.conf")
md5sums=('6f738b87377817076bd7cf0692069850')

package() {
  install -Dm 644 "$srcdir/qemu-static.conf" "$pkgdir/usr/lib/binfmt.d/qemu-static.conf"
}

# vim:set ts=2 sw=2 et:
