# Maintainer: John Jenkins <twodopeshaggy@gmail.com>

pkgname=drive
pkgver=0.2.4
pkgrel=2
pkgdesc="Pull or push Google Drive files"
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h')
url="http://github.com/odeke-em/drive"
license=('Apache')
depends=('hicolor-icon-theme' 'gtk-update-icon-cache')
makedepends=('go' 'git')
conflicts=('drive-git')
options=('!strip' '!emptydirs')
install=$pkgname.install
source=("https://github.com/odeke-em/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('b4b3799c1b6abf0f15cef8df34e6963a9f63f5fd6430c4b450ca83041c8b59f1')

prepare() {
 mkdir -p "$srcdir/go"
 export GOPATH="$srcdir/go"
 go get github.com/odeke-em/drive/cmd/drive
 go get github.com/odeke-em/drive/config
 go get github.com/rakyll/command
 go get github.com/odeke-em/drive/src
 go get github.com/odeke-em/ripper/src
 go get github.com/odeke-em/xon/pkger/src
 export GOPATH="$srcdir/$pkgname-$pkgver"
 go get github.com/odeke-em/drive/drive-gen
 cd $srcdir/$pkgname-$pkgver/bin/
 ./drive-gen
}

package() {
  cd $srcdir/$pkgname-$pkgver/bin/
  install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p $pkgdir/usr/share/licenses/$pkgname
  install -m 0644 LICENSE $pkgdir/usr/share/licenses/$pkgname/
  mkdir -p "$pkgdir/usr/share/icons/hicolor/128x128/mimetypes"
  cp $srcdir/$pkgname-$pkgver/icons/*.png $pkgdir/usr/share/icons/hicolor/128x128/mimetypes
  mkdir -p "$pkgdir/usr/share/icons/hicolor/scalable/mimetypes"
  cp $srcdir/$pkgname-$pkgver/icons/*.svg $pkgdir/usr/share/icons/hicolor/scalable/mimetypes
  rm -r  "$srcdir/go"
}
# vim:set ts=2 sw=2 et:
