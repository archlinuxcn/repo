# Maintainer: database64128 <free122448@hotmail.com>

pkgname=mediamtx
pkgver=1.15.5
pkgrel=1
pkgdesc="Ready-to-use RTSP / RTMP / LL-HLS / WebRTC server and proxy that allows to read, publish and proxy video and audio streams"
arch=('x86_64' 'aarch64')
url="https://github.com/bluenviron/$pkgname"
license=('MIT')
makedepends=('git' 'go')
backup=("etc/$pkgname/mediamtx.yml")
source=(
    "$pkgname::git+$url.git#tag=v$pkgver"
    "$pkgname.service"
    "$pkgname@.service"
)
b2sums=(
    'c1d4b4d28023df2fb2a5a7388c629aa30929ff5edfd4d6e9ebede42afd2b4d068489e4d93aa00597b52219403ec11a40816273833a7a596f60d6472c8d6a18ad'
    '636b7c89aec0e54a471464d013fd13fd83bebb21c3ebef9c0259fdea21185e3317ced09ef1c821ed253a62c3825f00cced19e42cdd175d1ddaecdef9800eeb4f'
    '280cab48cc4d513d20952c82aab7474b9eb474dcb37a2b9d559a7caa8cd5ab6527a293c77b8ab7c64f02564c42c91b7141756020adef8ddb54316e8fcea6d0bf'
)

build() {
    cd $pkgname
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath"
    go generate ./...
    go build -ldflags='-s -w -linkmode=external'
}

package() {
    install -Dm644 $pkgname.service "$pkgdir"/usr/lib/systemd/system/$pkgname.service
    install -Dm644 $pkgname@.service "$pkgdir"/usr/lib/systemd/system/$pkgname@.service
    cd $pkgname
    install -d "$pkgdir"/etc/$pkgname
    install -Dm644 $pkgname.yml "$pkgdir"/etc/$pkgname/$pkgname.yml
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
    install -Dm755 $pkgname "$pkgdir"/usr/bin/$pkgname
}
