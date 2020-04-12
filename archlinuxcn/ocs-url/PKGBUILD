# PACKAGER: Pol Marcet Sardà <polmarcetsarda@gmail.com>
# Maintainer: Pol Marcet Sardà <polmarcetsarda@gmail.com>
# Maintainer: Bernhard Landauer <oberon@manjaro.org>
# Maintainer: Akira Ohgaki <akiraohgaki@gmail.com>

pkgname=ocs-url
pkgver=3.1.0
pkgrel=6
pkgdesc='An install helper program for items served via OpenCollaborationServices (ocs://).'
arch=('x86_64')
url="https://www.opencode.net/akiraohgaki/$pkgname"
license=('GPL3')
depends=('qt5-base>=5.2.0' 'qt5-svg>=5.2.0' 'qt5-declarative>=5.2.0' 'qt5-quickcontrols>=5.2.0')
makedepends=('git')
conflicts=('xdgurl')
provides=('xdgurl')
source=("git+$url.git#tag=release-$pkgver"
	"new-version-format.patch")
sha256sums=('SKIP'
	    'c80a519c8caa7c1ebb9cc26374f25c7681f5740d64a4d88ffaf495e077e234fc')

prepare() {
    cd $pkgname
    patch --forward --strip=1 --input="${srcdir}/new-version-format.patch"
    ./scripts/prepare
}

build() {
    cd $pkgname
    qmake PREFIX="/usr"
    make
}

package() {
    cd $pkgname
    make INSTALL_ROOT=$pkgdir install
}
