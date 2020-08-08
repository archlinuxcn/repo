# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-gettext-tools-git
pkgver=1.0.8.r3.gc4d7bdb
pkgrel=1
pkgdesc='Deepin Gettext Tools'
arch=('any')
url="https://github.com/linuxdeepin/deepin-gettext-tools"
license=('GPL3')
depends=('gettext' 'python' 'perl-config-tiny' 'perl-xml-libxml')
makedepends=('git')
conflicts=('deepin-gettext-tools')
replaces=('deepin-gettext-tools')
provides=('deepin-gettext-tools')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/deepin-gettext-tools/")
sha512sums=('SKIP')

pkgver() {
    cd deepin-gettext-tools
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd deepin-gettext-tools

  sed -e 's/sudo cp/cp/' -i src/generate_mo.py
  sed -e 's/qmake/qmake-qt5/' -e '/lupdate/d' -i Makefile
}

check() {
  cd deepin-gettext-tools
  perl src/desktop_ts_convert.pl --help
  python src/generate_mo.py --help
  python src/update_pot.py --help
}

package() {
  cd deepin-gettext-tools
  make DESTDIR="$pkgdir" install
}
