# Maintainer: George Rawlinson <george@rawlinson.net.nz>

pkgname=cloudflared
pkgver=2022.6.3
pkgrel=1
pkgdesc='Command-line client for Cloudflare Tunnel'
arch=('x86_64' 'armv7h' 'aarch64')
url='https://github.com/cloudflare/cloudflared'
license=('Apache')
depends=('glibc')
makedepends=('git' 'go')
conflicts=('cloudflared-bin')
backup=("etc/$pkgname/config.yml")
options=('!lto')
_commit='6a6ba704f1d5b83e5fa6e8f6e80c6243b3018c2a'
source=(
  "$pkgname::git+$url.git#commit=$_commit"
  'config.yml'
  'systemd.service'
  'sysusers.conf'
  'tmpfiles.conf'
)
sha512sums=('SKIP'
            '52a8e1a71b7195047ea490ade1caae8f82c7c332d9473611853b6cc21c31eb4403a94b66e9efc800faa4a1d3c0d8b5ad01d60896728161eeb4bf2a69ac58b95a'
            '74ddc921fc374785f92ff08a7f74b498d358859176bbb957d41fb5d2e9464d9ae1f60debf231c4233aa91a9151ba3d82d9a8f712d2ac4ed95be73f4f75324f86'
            '24af69f69fa49a4d4f703ce4f7093817e2b8e942e5f3b2ab296ea6bf1a3b54530dc99c9569cda4132b47625f2d4a3478bd1e0d4268794db735e7d02d32e57d17'
            'db826ea2bb031a1c9c0ff8f81f54894ab116d506700da8e49c207d6a252366f4ce02cf63386a333071a85fe699287a8c8bfc2e49c946845abd4592f5764a433b')
b2sums=('SKIP'
        '887218db3b5e7cdbb90c86b60aac1597d70b59fccece18c8c5e6e2357d04aa219b2438436f23f913a0c8dc6eb425ef3e22901e28fd30e5130d17e414e67ec4af'
        '2797460dbaf11bc34ebebd8b051149a0701c5dfffc51089d19413917b7112fdf8356ec4d6e5800d0af5d0a43e52031ab3c9a7cd347105ef224e73285b36dbd07'
        '55fa073feb872e951d206eefa8c32ef0833a348c7b1814c38a75229a971d065463866bd686258b7e6581154494f85cd00531a993d1b6475c696d50e362183683'
        '83ffe6d68df4c98d23bef780f891797793321022a8d50897383f3cc9730cce5660704cd51ee791033e09ad4c1ce33c992e40d542a0685293c328faeba00aa864')

pkgver() {
  cd "$pkgname"

  git describe --tags
}

prepare() {
  cd "$pkgname"

  # create directory for build output
  mkdir build
}

build() {
  cd "$pkgname"

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
  cd "$pkgname"
  go test ./...
}

package() {
  # systemd integration
  install -vDm644 systemd.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
  install -vDm644 sysusers.conf "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
  install -vDm644 tmpfiles.conf "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"

  # config
  install -vDm644 -t "$pkgdir/etc/$pkgname" config.yml

  cd "$pkgname"

  # binary
  install -vDm755 -t "$pkgdir/usr/bin" "build/$pkgname"

  # man page
  install -vDm644 -t "$pkgdir/usr/share/man/man1" "build/$pkgname.1"
}

# vim:set ts=2 sw=2 et:
