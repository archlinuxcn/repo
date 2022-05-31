# Maintainer: John Downey <jdowney@gmail.com>
pkgname=smug
pkgver=0.2.9
pkgrel=1
pkgdesc='A session manager for tmux written in Go'
arch=('x86_64')
url="https://github.com/ivaaaan/smug"
license=('MIT')
makedepends=('go')
source=("https://github.com/ivaaaan/smug/archive/v${pkgver}.tar.gz")
sha256sums=('23b402d49923451fd5f7268eec59f3b9b36841be8bc0ee33e9b93fdf50f7af8c')

prepare(){
  cd "$pkgname-$pkgver"
  mkdir -p build/
}

build() {
  cd "$pkgname-$pkgver"
  go build -o build -buildmode=pie -trimpath -ldflags="-X=main.version=$pkgver -linkmode=external" -mod=readonly -modcacherw
}

check() {
  cd "$pkgname-$pkgver"
  go test
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 build/$pkgname "$pkgdir"/usr/bin/$pkgname
  install -Dm644 man/man1/smug.1 "$pkgdir/usr/share/man/man1/smug.1"
}
