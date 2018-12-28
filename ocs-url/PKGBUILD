# Maintainer: Pol Marcet Sardà <polmarcetsarda@gmail.com>
# Maintainer: Bernhard Landauer <oberon@manjaro.org>
# Maintainer: Akira Ohgaki <akiraohgaki@gmail.com>

pkgname=ocs-url
pkgver=3.1.0
pkgrel=3
pkgdesc='An install helper program for items served via OpenCollaborationServices (ocs://).'
arch=('x86_64')
url="https://git.opendesktop.org/OCS/ocs-url"
license=('GPL3')
depends=('qt5-base>=5.2.0' 'qt5-svg>=5.2.0' 'qt5-declarative>=5.2.0' 'qt5-quickcontrols>=5.2.0')
makedepends=('git')
conflicts=('xdgurl')
provides=('xdgurl')
source=("git+https://git.opendesktop.org/OCS/ocs-url.git#tag=release-3.1.0")
sha256sums=('SKIP')

prepare() {
    cd $pkgname
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
