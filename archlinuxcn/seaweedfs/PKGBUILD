# Maintainer: Jonathon Fernyhough <jonathon+m2x.dev>
# Contributor: krevedko <helllamer-gmail.com>

pkgname=seaweedfs
pkgver=2.76
pkgrel=1
pkgdesc="SeaweedFS is a simple and highly scalable distributed file system"
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h' 'arm')
url="https://github.com/chrislusf/seaweedfs"
license=('APACHE')
makedepends=('git' 'go')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('ca73c4eac55463db95dfbcecb32ab89e93eb1402ac5cf66f1e1c31a0cf9d70b6')
_shortcommit=84d2e1b

prepare() {
  cd $pkgname-$pkgver

  export GOPATH="${SRCDEST:-$srcdir}"
  go mod vendor
}

build() {
  export CGO_CPPFLAGS="$CPPFLAGS"
  export CGO_CFLAGS="$CFLAGS"
  export CGO_CXXFLAGS="$CXXFLAGS"
  export CGO_LDFLAGS="$LDFLAGS"
  export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
  export GOPATH="${SRCDEST:-$srcdir}"

  cd $pkgname-$pkgver/weed
  go build -v $GO_FLAGS -ldflags "-X github.com/chrislusf/seaweedfs/weed/util.COMMIT=$_shortcommit -extldflags $LDFLAGS"
}

#check() {
#  cd $pkgname-$pkgver/weed
#  go test -v
#}

package() {
  cd $pkgname-$pkgver
  install -D     weed/weed "$pkgdir"/usr/bin/weed
  install -Dm644 README.md "$pkgdir"/usr/share/doc/$pkgname/README.md
  install -Dm644 LICENSE   "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
