# Maintainer: Giovanni Harting <539@idlegandalf.com>
# Contributor: Pavers_Career <pavers_career_0d AT ícloud DOT com>

pkgname=adguardhome
_pkgname=AdGuardHome
pkgver=0.107.14
pkgrel=1
epoch=1
pkgdesc="Network-wide ads and trackers blocking DNS server"
arch=(x86_64 aarch64 armv7h armv6h)
url="https://github.com/AdguardTeam/AdGuardHome"
license=('GPL')
source=("$pkgname-$pkgver.tar.gz::https://github.com/AdguardTeam/AdGuardHome/archive/v$pkgver.tar.gz"
        "$pkgname.service"
        "$pkgname.defaults"
)
makedepends=(go 'nodejs<17' npm yarn git)
depends=(glibc)
backup=('etc/default/adguardhome')
b2sums=('3dc0f343206dbbad123b344bd59ab4901fdbc0544bc9284735fb0ed71ad0da4f15a3e8c31694f38722b5c6de44aefb7964abc03ad33d1de1e6b64a74189b79cb'
        'd55d1667916e291b201dde5bd0a5d2d6dd16c654ecec4ea47c4a3a54b898e7008ba0538c9d5a4c7572cc304cc625b39accd69692766c1618890efff88e96e5a0'
        'ec3a3cd8debae4dcb4a723ef2ba31960aa1f897e2f8c857fcf9861bc7959072b22fed3091c0d07084c280be0755d03bf6ca4fef5f2d08ae20397378e13cf9c9b')

prepare() {
  cd "$_pkgname-$pkgver"
  npm --prefix client ci
  yarn --cwd client2 install
  go mod download
}

build() {
  cd "$_pkgname-$pkgver"
  npm --prefix client run build-prod
  yarn --cwd client2 build
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
  install -Dm644 "$srcdir"/$pkgname.defaults "$pkgdir/etc/default/$pkgname"
}
