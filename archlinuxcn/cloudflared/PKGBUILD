# Maintainer: George Rawlinson <george@rawlinson.net.nz>

pkgname=cloudflared
pkgver=2021.5.10
pkgrel=1
pkgdesc="Argo Tunnel client"
arch=(x86_64 armv7h aarch64)
url="https://github.com/cloudflare/cloudflared"
license=('custom:cloudflared')
depends=(glibc)
makedepends=(go)
conflicts=(cloudflared-bin)
backup=("etc/$pkgname/config.yml")
source=("$pkgname-$pkgver.tar.gz::https://github.com/cloudflare/cloudflared/archive/$pkgver.tar.gz"
        "config.yml"
        "$pkgname.service"
        "sysusers.d.conf"
        "tmpfiles.d.conf")
b2sums=('7296da770918b46290911f70f4147e050e698228f3ef1d73592a05e01c7c5e403bc1666bf34a49453e47b6b7b3ec580e5406233f4e792cee8d17193773b10269'
        '887218db3b5e7cdbb90c86b60aac1597d70b59fccece18c8c5e6e2357d04aa219b2438436f23f913a0c8dc6eb425ef3e22901e28fd30e5130d17e414e67ec4af'
        '0fa4ac918b4c72e2b1a1bd36e025fdb6078364363cba167e6d91e7815c8bd6f5c4b412f0651d1a75991ef7e069da6e81917f22bd40ef87fd1ccd41171e64e0b2'
        '7a15fc73f02cc74e2cea55ba51632724bae16f140e07904a88daa3179ed320e9e6efa9a1901d8249fd1618a2a91f93384a93bfaba6eba6990457b7c2d2155f58'
        '83ffe6d68df4c98d23bef780f891797793321022a8d50897383f3cc9730cce5660704cd51ee791033e09ad4c1ce33c992e40d542a0685293c328faeba00aa864')

prepare() {
  cd "$pkgname-$pkgver"
  mkdir build
}

build() {
  cd "$pkgname-$pkgver"
  go build -v \
    -buildmode=pie \
    -trimpath \
    -mod=vendor \
    -modcacherw \
    -ldflags "-extldflags $LDFLAGS -X "main.Version=${pkgver}" -X "main.BuildTime="$(date --iso-8601=seconds --utc)""" \
    -o build ./cmd/...
}

check() {
  cd "$pkgname-$pkgver"
  go test ./...
}

package() {
  # binary
  install -Dm755 -t "$pkgdir/usr/bin" "$pkgname-$pkgver/build/$pkgname"

  # license
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" "$pkgname-$pkgver/LICENSE"

  # systemd files
  install -Dm644 -t "$pkgdir/usr/lib/systemd/system" "$pkgname.service"
  install -Dm644 sysusers.d.conf "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
  install -Dm644 tmpfiles.d.conf "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"

  # config
  install -Dm644 -t "$pkgdir/etc/$pkgname" config.yml
}

# vim:set ts=2 sw=2 et:
