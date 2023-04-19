# Maintainer: simonsmh <simonsmh@gmail.com>
pkgname=okteto
pkgver=2.14.3
pkgrel=1
pkgdesc="Build better applications by developing and testing your code directly in Kubernetes."
arch=(x86_64 aarch64)
url="https://github.com/okteto/okteto"
license=(Apache)
optdepends=(kubectl)
makedepends=(go-pie)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/okteto/okteto/archive/${pkgver}.tar.gz")
sha256sums=('6451623274f50e326a75f7bc6817eda936cedf6b142ebb7064ea5f35586630df')

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
