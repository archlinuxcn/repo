# Contributor: kitsunyan <`echo a2l0c3VueWFuQGFpcm1haWwuY2MK | base64 -d`>
# Maintainer: j-james <jj@j-james.me>

pkgname=pakku
pkgver=0.16
pkgrel=1
pkgdesc='Pacman wrapper and AUR helper with a pacman-like user interface'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/zqqw/$pkgname"
license=('GPL3')
depends=('libcurl.so' 'git')
makedepends=('nim' 'git' 'asciidoc')
backup=('etc/pakku.conf')
source=("$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('38338000ac436cbc1a1058b125db5e569170fabe1c48bac8bec8c539c982bae4')

build() {
  local addargs=()
  grep -Fxq debug <<< "`printf '%s\n' "${options[@]}"`" &&
  addargs=(NIM_TARGET='debug' NIM_OPTIMIZE='none')

  cd "$srcdir/$pkgname-$pkgver"
  make "${addargs[@]}" NIM_CACHE_DIR='../nimcache' PREFIX='/usr'
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make PREFIX='/usr' DESTDIR="$pkgdir" install
}
