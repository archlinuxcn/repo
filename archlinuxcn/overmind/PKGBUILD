#!/hint/bash -e
# Maintainer: Adrien Smith <adrien@panissupraomnia.dev>

pkgname=overmind
pkgver=2.3.0
pkgrel=1
pkgdesc="Process manager for Procfile-based applications and tmux"
arch=("x86_64")
url="https://github.com/DarthSim/$pkgname"
license=("MIT")
depends=('tmux')
makedepends=("go")
conflicts=("$pkgname-bin" "$pkgname-git")
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha512sums=('ea0b200ac4954846739b9bc771783d62a5b0018ef133b9898c0156d346656163ae41bc7e8f4d8d4ccf9e01aa79e5e8a9e47cda64ea66faf554141b3dfad9a3e1')
b2sums=('4d088231210d534a5bab8fbb597c788efe75b2d5995fd439ebb8509994f715fa129ed23a0215e0c6495219b05c318f2a10c5cdcdaea8f19da6c531781e56f09e')

build() {
  cd "$pkgname-$pkgver"

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -o $pkgname .
}

package() {
  cd "$pkgname-$pkgver"

  install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
