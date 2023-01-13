# Maintainer: Piotr Miller <nwg.piotr@gmail.com>
# Project: nwg-shell for sway, https://github.com/nwg-piotr/nwg-shell
pkgname=('nwg-drawer')
pkgver=0.3.7
pkgrel=1
pkgdesc="Application drawer for sway and other wlroots-based compositors"
arch=('x86_64')
url="https://github.com/nwg-piotr/nwg-drawer"
license=('MIT')
provides=('nwg-drawer')
conflicts=('nwg-drawer-git' 'nwg-drawer-bin')
makedepends=('go')
depends=('gtk3' 'gtk-layer-shell' 'xdg-utils')
optdepends=('alacritty: to open .desktop files with Terminal=true'
            'thunar: to open files and directories')
source=("$pkgname-$pkgver.tar.gz::https://github.com/nwg-piotr/nwg-drawer/archive/v"$pkgver".tar.gz")

md5sums=('6f82b73b8465c30bbb0ff5c81397c27e')

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
  install -Dm644 -t "$pkgdir"/usr/share/"$pkgname" "$pkgname"-"$pkgver"/drawer.css
  install -Dm755 -t "$pkgdir"/usr/bin "$pkgname"-"$pkgver"/bin/"$pkgname"
}
