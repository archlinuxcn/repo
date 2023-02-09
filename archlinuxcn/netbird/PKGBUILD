# Maintainer: tarball <bootctl@gmail.com>

pkgname=netbird
pkgver=0.13.0
pkgrel=1
pkgdesc='A WireGuard-based mesh network that connects your devices into a single private network'
url='https://netbird.io'
arch=(x86_64 aarch64 armv7h armv7l armv6h)
license=(BSD)

provides=("$pkgname")
conflicts=("$pkgname")
depends=(glibc)
makedepends=(go)
optdepends=()
replaces=(wiretrustee)

_package=github.com/netbirdio/$pkgname

source=(
  "$pkgname-$pkgver.tar.gz::https://$_package/archive/refs/tags/v$pkgver.tar.gz"
  'environment'
  'netbird@.service'
)
sha256sums=('2dbb259e5bffe1f700fb34ba52a706c79bb20a09404234258f61ad0985838359'
            '128e36e1f814a12886f3122a1809a404be17f81481275b6624e66937941f5269'
            '75fd7683b5c1902f58ff446c362b89d6111ee3585f668249d9a0ff071dd4371e')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p build
  go mod download
}

build() {
  export GOFLAGS='-buildmode=pie -trimpath -mod=readonly -modcacherw'
  cd "$srcdir/$pkgname-$pkgver"

  go build \
    -ldflags "-s -w -linkmode=external -X $_package/client/system.version=$pkgver -extldflags \"$LDFLAGS\"" \
    -o build/"$pkgname" \
    client/main.go

  for shell in bash fish zsh; do
    ./build/"$pkgname" completion $shell >build/completion.$shell
  done
}

check() {
  cd "$srcdir/$pkgname-$pkgver/build"

  # check that version was set and it works
  [[ "$(./$pkgname version)" == $pkgver ]]
}

package() {
  _source="$srcdir/$pkgname-$pkgver"

  # binary
  install -Dm755 "$_source/build/$pkgname" "$pkgdir/usr/bin/$pkgname"

  # config directory
  install -Ddm755 -o root -g root "$pkgdir/etc/$pkgname"

  # environment file
  install -Dm644 environment "$pkgdir/etc/default/$pkgname"

  # systemd unit
  install -Dm644 "$pkgname@.service" \
    "$pkgdir/usr/lib/systemd/system/$pkgname@.service"

  # license
  install -Dm644 "$_source/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # shell completions
  install -Dm644 "$_source/build/completion.bash" \
    "$pkgdir/usr/share/bash-completion/completions/$pkgname"

  install -Dm644 "$_source/build/completion.fish" \
    "$pkgdir/usr/share/fish/completions/$pkgname.fish"

  install -Dm644 "$_source/build/completion.zsh" \
    "$pkgdir/usr/share/zsh/site-functions/_$pkgname"
}
