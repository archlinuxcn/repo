# Maintainer: Giovanni Harting <539@idlegandalf.com>
# Contributor: Pavers_Career <pavers_career_0d AT ícloud DOT com>

pkgname=adguardhome
_pkgname=AdGuardHome
pkgver=0.107.38
pkgrel=1
epoch=1
pkgdesc="Network-wide ads and trackers blocking DNS server"
arch=(x86_64 aarch64 armv7h armv6h)
url="https://github.com/AdguardTeam/AdGuardHome"
license=('GPL')
source=("$pkgname-$pkgver.tar.gz::https://github.com/AdguardTeam/AdGuardHome/archive/v$pkgver.tar.gz"
        "$pkgname.service"
        "$pkgname.install"
)
makedepends=(go nodejs-lts-gallium npm git)
depends=(glibc)
install="$pkgname.install"
b2sums=('c77c1e468f06afdcda41eeed8ec76a48b0f5ef67e299d1fd3afe2d6be24dc6f8bfce9f6d29530a4823df970f4fcf94573a5266371584f7372647d03dc6c88649'
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
