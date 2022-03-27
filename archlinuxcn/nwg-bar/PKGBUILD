# Maintainer: Piotr Miller <nwg.piotr@gmail.com>
# Project: nwg-shell for sway, https://github.com/nwg-piotr/nwg-shell
pkgname=('nwg-bar')
pkgver=0.0.1
pkgrel=2
pkgdesc="GTK3-based button bar for sway and other wlroots-based compositors"
arch=('x86_64')
url="https://github.com/nwg-piotr/nwg-bar"
license=('MIT')
provides=('nwg-bar')
conflicts=('nwg-bar-git' 'nwg-bar-bin')
makedepends=('go')
depends=('gtk3' 'gtk-layer-shell')
source=("$pkgname-$pkgver.tar.gz::https://github.com/nwg-piotr/nwg-bar/archive/v"$pkgver".tar.gz")

md5sums=('6e8170fa29d16c2d4c81a57e2dc183cb')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
  export GOPATH="${srcdir}"/go
  export PATH=$PATH:$GOPATH/bin
  go build -o bin/"$pkgname" *.go
}

package() {
  cd "$srcdir"
  install -d "$pkgdir"/usr/share/"$pkgname"/images
  install -Dm644 -t "$pkgdir"/usr/share/"$pkgname"/images/ "$pkgname"-"$pkgver"/images/*
  install -Dm644 -t "$pkgdir"/usr/share/"$pkgname"/ "$pkgname"-"$pkgver"/config/*
  install -Dm755 -t "$pkgdir"/usr/bin "$pkgname"-"$pkgver"/bin/"$pkgname"
}
