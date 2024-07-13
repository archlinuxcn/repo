# Maintainer: Giovanni Harting <539@idlegandalf.com>
# Contributor: Pavers_Career <pavers_career_0d AT ícloud DOT com>

pkgname=adguardhome
_name=AdGuardHome
pkgver=0.107.52
pkgrel=1
epoch=1
pkgdesc='Network-wide ads and trackers blocking DNS server'
arch=(x86_64 aarch64 armv7h)
url='https://github.com/AdguardTeam/AdGuardHome'
license=(GPL-2.0-only)
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        "$pkgname.service"
        "$pkgname.install")
makedepends=(go nodejs npm git)
depends=(glibc)
install="$pkgname.install"
b2sums=('0391ad041e3a4cf9ebcf8ad081c417454311431847cef8020af7ac7569cc2721ab6af269067f6d3f81e0078ed49cb1ef7a15a699c41e88de26a085cd2eb7de8b'
        '161152f91e09fe491db631eb6ed603c0c975453b682467945fdade6091bf427ec932230f3a10e40e2f054dc01567930ecc27343c04882fb0e736b4f6becc96da'
        'b22ae447e0288e64332bcb41cc73f61e9adb58d402ef3ccfb896aa1ecbec4d4ff66bfc1464ca9d0bc99f1a5b4d32bdc5765f42a1b72b0fb3786ecefcf94a7265')

prepare() {
  cd "$_name-$pkgver"
  npm --prefix client ci
  go mod download
}

build() {
  cd "$_name-$pkgver"
  export NODE_OPTIONS=--openssl-legacy-provider
  npm --prefix client run build-prod
  unset NODE_OPTIONS

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode external -extldflags \"${LDFLAGS}\" -X 'github.com/AdguardTeam/AdGuardHome/internal/version.version=v$pkgver' -X 'github.com/AdguardTeam/AdGuardHome/internal/version.channel=release'" \
    -o $pkgname
}

package() {
  install -Dm755 "$_name-$pkgver/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"
  install -dm755 "$pkgdir/etc"
  ln -s "/var/lib/$pkgname/$_name.yaml" "$pkgdir/etc/$pkgname.yaml"
}

# vim:set ts=2 sw=2 et:
