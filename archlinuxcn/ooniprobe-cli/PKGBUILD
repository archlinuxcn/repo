# Maintainer: bgme <i@bgme.me>
# Contributor: ml <>

_pkgname=probe-cli
pkgname=ooniprobe-cli
pkgver=3.31.0
_pkgver=3.31.0
pkgrel=2
pkgdesc='Next generation OONI Probe CLI'
arch=('x86_64')
url='https://ooni.org/'
license=('GPL-3.0-or-later')
depends=('glibc')
makedepends=('go')
source=("${_pkgname}-${_pkgver}.tar.gz::https://github.com/ooni/${_pkgname}/archive/refs/tags/v${_pkgver}.tar.gz")
sha256sums=('0c7aab87ef755c5c5454ba81df7fb800249fd3a26d1e7e77043be766e19013a0')
sha512sums=('8b65ab6c80954fb525b45ca01adf48bb19f2beec25df868d43430f380418059dd3eb403de61cc3a826223a57a2014e9ec1efa57f77f0fb8d115be93b43abd289')

build() {
  cd "${_pkgname}-${_pkgver}"
  export CGO_ENABLED=1
  export CGO_LDFLAGS="$LDFLAGS"
  export CGO_CFLAGS="$CFLAGS"
  export CGO_CPPFLAGS="$CPPFLAGS"
  export CGO_CXXFLAGS="$CXXFLAGS"
  export GOFLAGS='-ldflags=-linkmode=external -buildmode=pie -trimpath -modcacherw'
  make CLI/ooniprobe
}

package() {
  cd "${_pkgname}-${pkgver}"
  install -Dm755 ooniprobe -t "$pkgdir/usr/bin"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 Readme.md -t "$pkgdir/usr/share/doc/$pkgname"
}
