# Maintainer: Stéphane Meyer <tigerlost at tigerfunk dot tk>
# Contributor: Stéphane Meyer <tigerlost at tigerfunk dot tk>

pkgname=bigtime
pkgver=2.4.2
pkgrel=1
pkgdesc="Customizable clock for the terminal"
arch=('any')
url="https://github.com/teegre/bigtime"
license=('MIT')
groups=()
depends=('alsa-utils' 'bash' 'coreutils' 'libnotify' 'ncurses')
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("$url/archive/"${pkgver}".tar.gz")
noextract=()
sha256sums=(2f0c0769c0c4e0bf6a11176449259ea656544fa286b01e2f83449ecec112ed96)

package() {
  cd "$pkgname-${pkgver/_/-}"
  make DESTDIR="$pkgdir/" PREFIX=/usr install
}
