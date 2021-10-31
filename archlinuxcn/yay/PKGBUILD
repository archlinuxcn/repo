# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=11.0.2
pkgrel=1
pkgdesc="Yet another yogurt. Pacman wrapper and AUR helper written in go."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/Jguer/yay"
options=(!lto)
license=('GPL3')
depends=(
  'pacman>5'
  'git'
)
optdepends=(
  'sudo'
)
makedepends=(
  'go'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Jguer/yay/archive/v${pkgver}.tar.gz")
sha256sums=('2e29f70bf332895c80c722d5d180fd9833c31d5a1dfe5cfa9d47b6f8cdcaca3a')

# With pacman 6 arriving a rebuild of yay will be necessary, if you upgrade pacman without upgrading yay at the same time, yay will not run after.
# I'm bumping the pkgrel so it shows up on the upgrade list (and will do so when pacman transitions from staging->core)
# In case you end up with a non-functioning yay after the upgrade follow the
# instructions on the github page

build() {
  export GOPATH="$srcdir"/gopath
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export CGO_ENABLED=1

  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX="/usr" build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX="/usr" install
}
