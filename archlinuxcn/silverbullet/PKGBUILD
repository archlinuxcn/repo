# Maintainer: tarball <bootctl@gmail.com>

pkgname=silverbullet
pkgver=0.10.1
pkgrel=1
pkgdesc='Clean Markdown-based writing/note taking application'
arch=(any)
url='https://github.com/silverbulletmd/silverbullet'
license=(MIT)
depends=(deno)
backup=("etc/default/$pkgname")
source=(
  "$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz"
  "$pkgname.service"
)
sha256sums=('5dcae3b959a26d9d4a0764ec28233fc9937e882c4c3f1f6055dfadaa67b44ed9'
            'b32f789c76e6db00e69bfbb7b00567dbb84104a723b3130e1afe55b7a72bbb59')

build() {
  cd "$pkgname-$pkgver"
  deno task build
  deno task bundle
}

check() {
  cd "$pkgname-$pkgver"
  deno task test
}

package() {
  install -dm755 "$pkgdir/etc/default"

  cat >"$pkgdir/etc/default/$pkgname" <<EOF
HOST=localhost
PORT=3000
EOF

  install -Dm644 "$pkgname.service" \
    "$pkgdir/usr/lib/systemd/system/$pkgname.service"

  cd "$pkgname-$pkgver"

  install -Dm644 "dist/$pkgname.js" \
    "$pkgdir/usr/lib/$pkgname/$pkgname.js"

  install -Dm644 LICENSE.md \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
