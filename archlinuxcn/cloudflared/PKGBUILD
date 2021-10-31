# Maintainer: George Rawlinson <george@rawlinson.net.nz>

pkgname=cloudflared
pkgver=2021.10.5
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
sha512sums=('1c6edfc00b668f491676c7936a8abae7b0bc7305c2f33d3aa5c79e3bc862e728d9e87b35edf5520db5cb971c34da762db16db043c701c7e5a798c8cec56db1f0'
            '52a8e1a71b7195047ea490ade1caae8f82c7c332d9473611853b6cc21c31eb4403a94b66e9efc800faa4a1d3c0d8b5ad01d60896728161eeb4bf2a69ac58b95a'
            'bd8be485adec1a84fdc2395aed75be8cca47e94f968b801699cb379008b63be56e3c4609470d7b1bb0ed25be071779b4f5f19df2bcfb4b659bfdd15ac16ce96f'
            '019e8bf95390d8f4815cf6118d419dba677967a22d9e68c245c71b32b198f188756e213ccada3f00b44a11b1486ef08780702ea0226086fc7e79e6c4466a26ae'
            'db826ea2bb031a1c9c0ff8f81f54894ab116d506700da8e49c207d6a252366f4ce02cf63386a333071a85fe699287a8c8bfc2e49c946845abd4592f5764a433b')
b2sums=('33b5d68896c4c0446de911993e34fa92132de6b0beb4913fd7927f66999e037d9eff128d74f64c21f9431ed526cd8f676c56be3c992bbdc16dcf17de9e923ee4'
        '887218db3b5e7cdbb90c86b60aac1597d70b59fccece18c8c5e6e2357d04aa219b2438436f23f913a0c8dc6eb425ef3e22901e28fd30e5130d17e414e67ec4af'
        '0fa4ac918b4c72e2b1a1bd36e025fdb6078364363cba167e6d91e7815c8bd6f5c4b412f0651d1a75991ef7e069da6e81917f22bd40ef87fd1ccd41171e64e0b2'
        '7a15fc73f02cc74e2cea55ba51632724bae16f140e07904a88daa3179ed320e9e6efa9a1901d8249fd1618a2a91f93384a93bfaba6eba6990457b7c2d2155f58'
        '83ffe6d68df4c98d23bef780f891797793321022a8d50897383f3cc9730cce5660704cd51ee791033e09ad4c1ce33c992e40d542a0685293c328faeba00aa864')

prepare() {
  cd "$pkgname-$pkgver"

  # create directory for build output
  mkdir build
}

build() {
  cd "$pkgname-$pkgver"

  # define buildtime for use in man page & binary
  local build_time="$(date -d@"$SOURCE_DATE_EPOCH" +%Y%m%d-%H:%M:%S)"

  # generate man page
  sed -e "s/\${VERSION}/${pkgver}/" \
      -e "s/\${DATE}/${build_time}/" \
    cloudflared_man_template > "build/$pkgname.1"

  # verify go modules
  go mod verify

  # build cloudflared
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
