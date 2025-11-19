# Maintainer: bgme <i@bgme.me>
# Contributor: ml <>

_pkgname=probe-cli
pkgname=ooniprobe-cli
pkgver=3.28.0
_pkgver=3.28.0
pkgrel=1
pkgdesc='Next generation OONI Probe CLI'
arch=('x86_64')
url='https://ooni.org/'
license=('GPL-3.0-or-later')
depends=('glibc')
makedepends=('go')
source=("${_pkgname}-${_pkgver}.tar.gz::https://github.com/ooni/${_pkgname}/archive/refs/tags/v${_pkgver}.tar.gz")
sha256sums=('62d9b51d0a9798b4c1b15641ab31d661b687dedd959945272c9bf6b7112476ab')
sha512sums=('cc97745fc676411ebd5d4fd782c1a60a24ff9635e8b19037ebe7f9f40ddc0217e718597fc674302e16d9fb0c6b2996b4fac6a4dbb20b9b19ba09fa4f1dce466e')

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
