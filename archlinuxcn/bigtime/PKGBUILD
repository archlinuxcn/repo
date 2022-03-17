# Maintainer: Stéphane Meyer <tigerlost at tigerfunk dot tk>
# Contributor: Stéphane Meyer <tigerlost at tigerfunk dot tk>

pkgname=bigtime
pkgver=2.4.8
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
sha256sums=(30f1d37b072ae97b303ca15cca8ec501ddd6a3921509a3b217854f0b89d69f6b)

package() {
  cd "$pkgname-${pkgver/_/-}"
  make DESTDIR="$pkgdir/" PREFIX=/usr install
}
