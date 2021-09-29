# Maintainer: George Rawlinson <george@rawlinson.net.nz>

pkgname=cloudflared
pkgver=2021.9.2
pkgrel=1
pkgdesc="Argo Tunnel client"
arch=('x86_64' 'armv7h' 'aarch64')
url="https://github.com/cloudflare/cloudflared"
license=('custom:cloudflared')
makedepends=('go')
conflicts=('cloudflared-bin')
backup=("etc/$pkgname/config.yml")
source=(
  "$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz"
  'config.yml'
  'systemd.service'
  'sysusers.conf'
  'tmpfiles.conf'
)
b2sums=('ef7fb1a0c294b7d33f426e43ae2ae92130a6fabd384a6cba956bf6d1192250b01e2396bce2daafa7755e8566fd4af28679ed4efe71ad628f05b40e82601cdba9'
        '887218db3b5e7cdbb90c86b60aac1597d70b59fccece18c8c5e6e2357d04aa219b2438436f23f913a0c8dc6eb425ef3e22901e28fd30e5130d17e414e67ec4af'
        '0fa4ac918b4c72e2b1a1bd36e025fdb6078364363cba167e6d91e7815c8bd6f5c4b412f0651d1a75991ef7e069da6e81917f22bd40ef87fd1ccd41171e64e0b2'
        '7a15fc73f02cc74e2cea55ba51632724bae16f140e07904a88daa3179ed320e9e6efa9a1901d8249fd1618a2a91f93384a93bfaba6eba6990457b7c2d2155f58'
        '83ffe6d68df4c98d23bef780f891797793321022a8d50897383f3cc9730cce5660704cd51ee791033e09ad4c1ce33c992e40d542a0685293c328faeba00aa864')

prepare() {
  cd "$pkgname-$pkgver"

  # create directory for build output
  mkdir build

  # verify go modules
  go mod verify
}

build() {
  cd "$pkgname-$pkgver"

  # define buildtime for use in man page & binary
  local build_time="$(date -d@"$SOURCE_DATE_EPOCH" +%Y%m%d-%H:%M:%S)"

  # generate man page
  sed -e "s/\${VERSION}/${pkgver}/" \
      -e "s/\${DATE}/${build_time}/" \
    cloudflared_man_template > "build/$pkgname.1"

  go build -v \
    -buildmode=pie \
    -trimpath \
    -mod=vendor \
    -modcacherw \
    -ldflags "-extldflags ${LDFLAGS} \
      -X main.Version=${pkgver} \
      -X main.BuildTime=${build_time}" \
    -o build \
    ./cmd/...
}

check() {
  cd "$pkgname-$pkgver"
  go test ./...
}

package() {
  # systemd integration
  install -vDm644 systemd.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
  install -vDm644 sysusers.conf "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
  install -vDm644 tmpfiles.conf "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"

  # config
  install -vDm644 -t "$pkgdir/etc/$pkgname" config.yml

  cd "$pkgname-$pkgver"

  # binary
  install -vDm755 -t "$pkgdir/usr/bin" "build/$pkgname"

  # license
  install -vDm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE

  # man page
  install -vDm644 -t "$pkgdir/usr/share/man/man1" "build/$pkgname.1"
}

# vim:set ts=2 sw=2 et:
