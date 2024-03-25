# Maintainer: Piotr Miller <nwg.piotr@gmail.com>
# Project: nwg-shell for sway, https://github.com/nwg-piotr/nwg-shell
pkgname=('nwg-drawer')
pkgver=0.4.7
pkgrel=1
pkgdesc="Application drawer for sway and other wlroots-based compositors"
arch=('any')
url="https://github.com/nwg-piotr/nwg-drawer"
license=('MIT')
makedepends=('go')
depends=('gtk3' 'gtk-layer-shell' 'xdg-utils')
optdepends=('foot: to open .desktop files with Terminal=true'
            'thunar: to open files and directories')
source=("$pkgname-$pkgver.tar.gz::https://github.com/nwg-piotr/nwg-drawer/archive/v"$pkgver".tar.gz")

md5sums=('ca12405fa32aeb3ae6c0a9f067dfe385')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw -ldflags=-linkmode=external"
  export GOPATH="${srcdir}"/go
  export PATH=$PATH:$GOPATH/bin
  go build -o bin/"$pkgname" *.go
}

package() {
  cd "$srcdir"
  install -d "$pkgdir"/usr/share/"$pkgname"/desktop-directories
  install -Dm644 -t "$pkgdir"/usr/share/"$pkgname"/desktop-directories/ "$pkgname"-"$pkgver"/desktop-directories/*
  install -Dm644 -t "$pkgdir"/usr/share/"$pkgname"/img/ "$pkgname"-"$pkgver"/img/*
  install -Dm644 -t "$pkgdir"/usr/share/"$pkgname" "$pkgname"-"$pkgver"/drawer.css
  install -Dm755 -t "$pkgdir"/usr/bin "$pkgname"-"$pkgver"/bin/"$pkgname"
  cd "$srcdir/$pkgname-$pkgver"
  install -D -t "$pkgdir"/usr/share/licenses/"$pkgname" LICENSE
  install -D -t "$pkgdir"/usr/share/doc/"$pkgname" README.md
}
