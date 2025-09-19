# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=q-dns
pkgdesc='A tiny command line DNS client with support for UDP, TCP, DoT, DoH, DoQ and ODoH.'
arch=('x86_64')
url='https://github.com/natesales/q'
pkgver=0.19.9
pkgrel=1
license=('GPL-3.0-or-later')
depends=('glibc')
makedepends=('unzip' 'go')
# source zip from GitHub contains commit hash in its comment
source=("q-$pkgver.zip::$url/archive/refs/tags/v$pkgver.zip")
sha256sums=('222a7e3cfe248d343ae68867f11861c0b6f75b639e6c60c3526bdc04b4aa8033')

build() {
  local _date=$(date --utc +"%Y-%m-%dT%H:%M:%SZ")
  local _commit=$(unzip -zq "$srcdir/q-$pkgver.zip")
  cd "q-$pkgver"
  # https://wiki.archlinux.org/title/Go_package_guidelines#Supporting_debug_packages
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOPATH="${srcdir}"
  export GOFLAGS="-buildmode=pie -mod=readonly -modcacherw"
  go build -ldflags "-compressdwarf=false -linkmode external -X main.version=$pkgver -X main.commit=$_commit -X main.date=$_date"
}

package() {
  install -Dm755 "$srcdir/q-$pkgver/q" "$pkgdir/usr/bin/q"
}
