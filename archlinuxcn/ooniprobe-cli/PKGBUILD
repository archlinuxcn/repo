# Maintainer: bgme <i@bgme.me>
# Contributor: ml <>

_pkgname=probe-cli
pkgname=ooniprobe-cli
pkgver=3.29.0
_pkgver=3.29.0
pkgrel=1
pkgdesc='Next generation OONI Probe CLI'
arch=('x86_64')
url='https://ooni.org/'
license=('GPL-3.0-or-later')
depends=('glibc')
makedepends=('go')
source=("${_pkgname}-${_pkgver}.tar.gz::https://github.com/ooni/${_pkgname}/archive/refs/tags/v${_pkgver}.tar.gz")
sha256sums=('5c5fd7aac8875f6e825b615d99b0890e6a9856b8647702318c32b1e43a6a1149')
sha512sums=('68badfbc07e04ca8c21c013b7450a60e3892679502a49ca30b0ecdb3e351ec34f46190c734e7a847d354a3d096dafa211151541f897d5ae12533a1787784957e')

build() {
  cd "${_pkgname}-${_pkgver}"
  GOVERSION=$(cat GOVERSION)
  export GOTOOLCHAIN=go${GOVERSION}

  export CGO_ENABLED=1
  export CGO_LDFLAGS="$LDFLAGS"
  export CGO_CFLAGS="$CFLAGS"
  export CGO_CPPFLAGS="$CPPFLAGS"
  export CGO_CXXFLAGS="$CXXFLAGS"
  export GOFLAGS='-ldflags=-linkmode=external -buildmode=pie -trimpath -modcacherw'
  go build ./cmd/ooniprobe
}

package() {
  cd "${_pkgname}-${pkgver}"
  install -Dm755 ooniprobe -t "$pkgdir/usr/bin"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 Readme.md -t "$pkgdir/usr/share/doc/$pkgname"
}
