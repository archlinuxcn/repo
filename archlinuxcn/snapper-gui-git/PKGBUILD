# Maintainer: Ilias Stamatis <stamatis.iliass at gmail dot com>, Saren Arterius <saren at wtako dot net>
# Contributor: Panagiotis Mavrogiorgos (pmav99) <> (gmail)

pkgname=snapper-gui-git
pkgver=0.1.r2.gc1b454a
pkgrel=1
pkgdesc="Gui for snapper, a tool of managing snapshots of Btrfs subvolumes and LVM volumes"
arch=(any)
url="https://github.com/ricardomv/snapper-gui"
license=('GPL2')
depends=('python3' 'gtk3' 'python-dbus' 'python-gobject' 'python-setuptools' 'gtksourceview3' 'snapper')
optdepends=('gksu: Access snapper-gui from application menu under GTK-base DE'
            'kdesu: Access snapper-gui from application menu under KDE')
makedepends=('git')
provides=('snapper-gui')
conflicts=('snapper-gui')
install=snapper-gui.install
source=("${pkgname}::git+https://github.com/ricardomv/snapper-gui.git")
sha256sums=('SKIP')

pkgver() {
  cd "$pkgname"
  git describe --long | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
  cd "$pkgname"
  python setup.py install --root="${pkgdir}/" --optimize=1
}
