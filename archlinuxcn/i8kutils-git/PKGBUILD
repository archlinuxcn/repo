# Maintainer: Gabriel Tremblay gabriel@delvelabs.ca
pkgname=i8kutils-git
_pkgname=i8kutils
pkgrel=3
pkgver=20170307.83622d1
pkgdesc="Fan control for Dell laptops"
makedepends=("git")
conflicts=("$_pkgname")
arch=("i686" "x86_64")
url="https://github.com/vitorafsr/$_pkgname"
license=("GPL")
depends=("bash")
optdepends=("tcl: for i8kmon daemon" "acpi: for i8kmon daemon" "tk: for i8kmon GUI mode")
backup=("etc/$_pkgname/i8kmon.conf")
source=("git+https://github.com/vitorafsr/$_pkgname.git"
	"i8kmon.service")

sha1sums=("SKIP"
	"370d2675d98d7754a265f9b1578975693204f681")

prepare() {
  cd $srcdir
  cd $_pkgname
  # conform to Arch Linux guidelines
  sed -i "s|/etc/i8kmon|/etc/$_pkgname/i8kmon.conf|g" i8kmon.1
  sed -i "s|/etc/i8kmon.conf|/etc/$_pkgname/i8kmon.conf|g" i8kmon
  make clean
}

build() {
  cd $_pkgname
  make
}

package() {
  cd $_pkgname
  install -d "$pkgdir"/usr/{bin,share/man/man1}
  install -D -m644 i8kctl.1 i8kmon.1 "$pkgdir/usr/share/man/man1"
  install -D -m755 i8kctl i8kfan i8kmon "$pkgdir/usr/bin"

  install -D -m644 i8kmon.conf "$pkgdir/etc/i8kutils/i8kmon.conf"
  install -D -m644 ../i8kmon.service "$pkgdir/usr/lib/systemd/system/i8kmon.service"
}
