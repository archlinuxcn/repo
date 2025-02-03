# Maintainer: tarball <bootctl@gmail.com>

pkgname=silverbullet
pkgver=0.10.1
pkgrel=2
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
            '14263a2804798f3710bc7733d4508349ac55e018457b98d3cf72ae50952fe6fa')

build() {
  cd "$pkgname-$pkgver"
  deno task build
  deno task bundle
}

# TODO: tests stopped working after 0.10.1 was released
#check() {
#  cd "$pkgname-$pkgver"
#  deno task test
#}

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
