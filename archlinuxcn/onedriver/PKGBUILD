# Maintained by Faisal Moledina (faisal at moledina dot me)
pkgname=onedriver
pkgver=0.11.2
pkgrel=1
pkgdesc="Native Linux filesystem for Microsoft OneDrive"
arch=('x86_64')
url='https://github.com/jstaf/onedriver'
license=('GPL3')
depends=('fuse2' 'webkit2gtk')
makedepends=('pkgconf' 'go')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('aac4f93691ea9a7beac2ef1dedbed8f82a76f161418f8d2da3651ca2194ca46da82ae847f8b5a2d21b88783821ed46bab574f14023ad476545f99f83420b35a3')

build() {
  cd "$pkgname-$pkgver"

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"

  go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode external -extldflags \"${LDFLAGS}\""

  make $pkgname-launcher
}

package() {
  cd "$pkgname-$pkgver"

  install -Dm 755 $pkgname "$pkgdir"/usr/bin/$pkgname
  install -Dm 755 $pkgname-launcher "$pkgdir"/usr/bin/$pkgname-launcher

  install -Dm 644 "resources/onedriver@.service" "$pkgdir"/usr/lib/systemd/user/onedriver@.service
  install -Dm 644 resources/$pkgname.desktop "$pkgdir"/usr/share/applications/$pkgname.desktop
  install -Dm 644 resources/$pkgname.png "$pkgdir"/usr/share/icons/onedriver/$pkgname.png
  install -Dm 644 resources/$pkgname.svg "$pkgdir"/usr/share/icons/onedriver/$pkgname.svg
  install -Dm 644 resources/$pkgname.1 "$pkgdir"/usr/share/man/man1/$pkgname.1
}
