# Maintainer: Giovanni Harting <539@idlegandalf.com>
# Contributor: Pavers_Career <pavers_career_0d AT ícloud DOT com>

pkgname=adguardhome
_pkgname=AdGuardHome
pkgver=0.107.45
pkgrel=1
epoch=1
pkgdesc="Network-wide ads and trackers blocking DNS server"
arch=(x86_64 aarch64 armv7h armv6h)
url="https://github.com/AdguardTeam/AdGuardHome"
license=(GPL)
source=("$pkgname-$pkgver.tar.gz::https://github.com/AdguardTeam/AdGuardHome/archive/v$pkgver.tar.gz"
        "$pkgname.service"
        "$pkgname.install")
makedepends=(go nodejs npm git)
depends=(glibc)
install="$pkgname.install"
b2sums=('257fbd716d769657c9b40a03f91f7dcaaee5c59788b43c86d1b90120f301cfbbfdf68f547143b6505d5bed70f03e992ca6ca3d86d0b1e9b760d0a21d9a19db89'
        'd74c0d6c8118a876fddfa045980ab002a6177efda49c3046cee22c6635c5f5caa1c520d8d4c07687dbaf52f7639da7172c25f027b8a499dc76c125940d431a98'
        'b22ae447e0288e64332bcb41cc73f61e9adb58d402ef3ccfb896aa1ecbec4d4ff66bfc1464ca9d0bc99f1a5b4d32bdc5765f42a1b72b0fb3786ecefcf94a7265')

prepare() {
  cd "$_pkgname-$pkgver"
  npm --prefix client ci
  go mod download
}

build() {
  cd "$_pkgname-$pkgver"
  export NODE_OPTIONS=--openssl-legacy-provider
  npm --prefix client run build-prod
  unset NODE_OPTIONS
  go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode external -extldflags \"${LDFLAGS}\" -X 'github.com/AdguardTeam/AdGuardHome/internal/version.version=v$pkgver' -X 'github.com/AdguardTeam/AdGuardHome/internal/version.channel=release'" \
    -o $pkgname
}

package() {
  install -Dm755 "$_pkgname-$pkgver/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"
  mkdir "$pkgdir/etc"
  ln -s "/var/lib/$pkgname/$_pkgname.yaml" "$pkgdir/etc/$pkgname.yaml"
}

# vim:set ts=2 sw=2 et:
