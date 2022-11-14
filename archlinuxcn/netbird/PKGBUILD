# Maintainer: tarball <bootctl@gmail.com>

pkgname=netbird
pkgver=0.10.8
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
  'wiretrustee@.service'
  'netbird.sysusers'
  '0001-fix-run-paths.patch'
)
sha256sums=('b5bd21d96179f18784d66f4c1438cb41d08cff26475e25a75d33884dbc6352bd'
            '128e36e1f814a12886f3122a1809a404be17f81481275b6624e66937941f5269'
            '5bea27f707291fc5fe7c43f3ff9ea302a07029e7a4866180a4933df41fa7c45f'
            '5bea27f707291fc5fe7c43f3ff9ea302a07029e7a4866180a4933df41fa7c45f'
            '67d4207501c8adca053ffa2bd8fe0e44564b7c5f59501b70a05ebf0155d918c2'
            '6238c54600f46af09169d320dc236c3d0f4f945ba1f3aca885f5ff7a99c261e9')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p build

  for patch in "$srcdir"/*.patch; do
    patch -p1 -i "$patch"
  done

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

  # users
  install -Dm644 "$pkgname.sysusers" "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"

  # binary
  install -Dm755 "$_source/build/$pkgname" "$pkgdir/usr/bin/$pkgname"

  # config directory
  install -Ddm755 -o root -g root "$pkgdir/etc/$pkgname"

  # environment file
  install -Dm644 environment "$pkgdir/etc/default/$pkgname"

  # systemd unit
  install -Dm644 "$pkgname@.service" \
    "$pkgdir/usr/lib/systemd/system/$pkgname@.service"

  install -Dm644 "wiretrustee@.service" \
    "$pkgdir/usr/lib/systemd/system/wiretrustee@.service"

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
