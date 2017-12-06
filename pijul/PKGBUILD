pkgname=pijul
pkgver=0.8.3
pkgrel=1
pkgdesc="Patch-based distributed version control system"
url='https://pijul.org'
makedepends=('cargo')
depends=('gcc-libs')
arch=('i686' 'x86_64')
license=('GPL')
source=("${url}/releases/${pkgname}-${pkgver}.tar.gz")
sha256sums=('45ef9ca3ae9d62953731b0c4b88c78fda7efae48e6970454c20581d49e10d4f6')

build() {
  cd "$pkgname-$pkgver"/pijul
  cargo build --release
}

package() {
  cd "$pkgname-$pkgver"/pijul
  install -Dm755 "target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"
}
