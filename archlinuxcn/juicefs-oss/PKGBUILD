# vim: expandtab shiftwidth=2 tabstop=2 softtabstop=4
# Maintainer: Peter Cai <peter@typeblog.net>

pkgname=juicefs-oss
_pkgname=juicefs
pkgver=1.0.2
_pkgver=$(echo $pkgver | sed -E 's/^([0-9\.]+)([^0-9].*)?$/\1-\2/' | sed -E 's/-$//')
pkgrel=1
pkgdesc="A distributed POSIX file system built on top of Redis and S3. (FOSS version)"
arch=('x86_64')
url="https://github.com/juicedata/juicefs"
license=('AGPL3')
conflicts=('juicefs')
depends=('glibc')
makedepends=('go')
source=("juicefs-$_pkgver.tar.gz::https://github.com/juicedata/juicefs/archive/refs/tags/v$_pkgver.tar.gz")
sha256sums=('47e194b912bf14483cb1e3433d745615594ac9e9275afc7b48e22ec39bdb66bc')

prepare() {
  cd "$_pkgname-$_pkgver"
  mkdir -p build/
}

build() {
  cd "$_pkgname-$_pkgver"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -o build/$_pkgname .
}

package() {
  cd "$_pkgname-$_pkgver"
  install -Dm755 build/$_pkgname "$pkgdir"/usr/bin/$_pkgname
  ln -s /usr/bin/$_pkgname "$pkgdir"/usr/bin/mount.$_pkgname
}
