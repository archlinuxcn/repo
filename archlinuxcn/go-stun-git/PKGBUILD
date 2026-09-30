# Maintainer: Edward Pacman <edward@edward-p.xyz>

pkgname=go-stun-git
pkgver=r143.4e9b249
pkgrel=1
pkgdesc="A go implementation of the STUN client (RFC 3489 and RFC 5389)"
arch=('x86_64')
url="https://github.com/ccding/go-stun"
license=('Apache-2.0')
source=(
  "git+https://github.com/ccding/go-stun.git"
)
makedepends=("go" "git")
provides=(go-stun)
conflicts=(go-stun)
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/go-stun"
  ( set -o pipefail
    git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

build(){
    cd "${srcdir}/go-stun"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
    go build
}

package() {
    cd "${srcdir}/go-stun"
    install -Dm755 go-stun "${pkgdir}/usr/bin/go-stun"
}
