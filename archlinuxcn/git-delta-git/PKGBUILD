# Maintainer: Matus Benko <matus.benko@gmail.com>

pkgname=git-delta-git
_pkgname=delta
pkgver=r.319.f89300a
pkgrel=1
pkgdesc="A syntax-highlighting pager for git"
arch=('any')
url="https://github.com/dandavison/delta"
license=('custom')
depends=()
makedepends=('git' 'rust')
provides=('delta')
source=(git+https://github.com/dandavison/$_pkgname.git)
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  printf "r.%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "$srcdir/$_pkgname"
  cargo build --release --locked
}

check() {
  cd "$srcdir/$_pkgname"
  cargo test --release --locked
}

package() {
  cd "$srcdir/$_pkgname"

  install -Dm755 "target/release/$_pkgname" -t "$pkgdir/usr/bin"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
