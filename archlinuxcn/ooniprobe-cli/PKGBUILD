# Maintainer: bgme <i@bgme.me>
# Contributor: ml <>

_pkgname=probe-cli
pkgname=ooniprobe-cli
pkgver=3.23.0
_pkgver=3.23.0
pkgrel=1
pkgdesc='Next generation OONI Probe CLI'
arch=('x86_64')
url='https://ooni.org/'
license=('GPL-3.0-or-later')
depends=('glibc')
makedepends=('go')
source=("${_pkgname}-${_pkgver}.tar.gz::https://github.com/ooni/${_pkgname}/archive/refs/tags/v${_pkgver}.tar.gz")
sha256sums=('ff4717e8fd0075bcb011d738e12a47a5be17deaa0b23346f354ddd6d95fed728')
sha512sums=('0a8c8c418551b600e680a0f248494ada60335028fdad28b4fb9847257164b3fba43ead4c221f0f497f8d1e2f767c3165ae925e4626e34db7af65e7bacc7d5008')

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
