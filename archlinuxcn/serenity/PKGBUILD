# Maintainer:  Misaka13514 <Misaka13514 at gmail dot com>
# Contributor: Henry-ZHR <henry-zhr@qq.com>

pkgname=serenity
pkgver=1.1.0alpha.4
_tagname='1.1.0-alpha.4'
pkgrel=1
pkgdesc='The configuration generator for sing-box'
arch=('i686' 'x86_64' 'aarch64' 'armv7h')
url='https://github.com/SagerNet/serenity'
license=('custom:GPL-3.0-or-later WITH name use or association addition')
depends=('glibc')
makedepends=('go')
optdepends=('sing-box')
backup=("etc/$pkgname/config.json")
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$_tagname.tar.gz")
sha256sums=('70088696823b73b1ed6ac5fa9ba3c93772b4d905609f447325be48360b92265e')

prepare() {
  cd $pkgname-$_tagname
  mkdir -p build/
}

build() {
  cd $pkgname-$_tagname
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  go build \
    -ldflags "-X github.com/sagernet/serenity/constant.Version=${pkgver} -linkmode external -s -w" \
    -o build -v ./cmd/...
  go run ./cmd/$pkgname completion bash > build/bash-completion
  go run ./cmd/$pkgname completion fish > build/fish-completion
  go run ./cmd/$pkgname completion zsh > build/zsh-completion
}

check() {
  cd $pkgname-$_tagname
  go test ./...
}

package() {
  cd $pkgname-$_tagname
  install -Dm755 build/$pkgname $pkgdir/usr/bin/$pkgname
  install -Dm644 build/bash-completion "$pkgdir/usr/share/bash-completion/completions/$pkgname"
  install -Dm644 build/fish-completion "$pkgdir/usr/share/fish/vendor_completions.d/$pkgname.fish"
  install -Dm644 build/zsh-completion "$pkgdir/usr/share/zsh/site-functions/_$pkgname"
  install -Dm644 release/config/config.json "$pkgdir/etc/$pkgname/config.json"
  install -Dm644 release/config/$pkgname.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
  install -Dm644 release/config/$pkgname@.service "$pkgdir/usr/lib/systemd/system/$pkgname@.service"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
