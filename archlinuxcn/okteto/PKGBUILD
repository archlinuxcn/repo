# Maintainer: simonsmh <simonsmh@gmail.com>
pkgname=okteto
pkgver=1.14.3
pkgrel=1
pkgdesc="Build better applications by developing and testing your code directly in Kubernetes."
arch=(x86_64 aarch64)
url="https://github.com/okteto/okteto"
license=(Apache)
optdepends=(kubectl)
makedepends=(go-pie)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/okteto/okteto/archive/${pkgver}.tar.gz")
sha256sums=('a2216fd65b21d4a7cc3517ecdfedd2d7f4850469292f67f4286d54f79150d8e3')

build() {
  cd "$pkgname-$pkgver"
  go build -ldflags "-s -w -X github.com/okteto/okteto/pkg/config.VersionString=$pkgver" -tags "osusergo netgo static_build" -o okteto
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 okteto "$pkgdir"/usr/bin/okteto
  install -Dm644 README.md -t "$pkgdir"/usr/share/doc/"$pkgname"
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
