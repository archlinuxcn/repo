# Maintainer: John Jenkins <twodopeshaggy@gmail.com>

pkgname=drive
pkgver=0.3.5
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
sha256sums=('f5f0a45c60818526fa6fd7f25024d91425b4f2f9ed841d324ba89c794bc9cc3f')

prepare() {
 mkdir -p "$srcdir/go"
 export GOPATH="$srcdir/go"
 go get github.com/odeke-em/drive/cmd/drive
 go get github.com/odeke-em/drive/config
 go get github.com/odeke-em/command
 go get github.com/odeke-em/drive/src
 go get github.com/odeke-em/ripper/src
 go get github.com/odeke-em/xon/pkger/src
 export GOPATH="$srcdir/$pkgname-$pkgver"
 go get github.com/odeke-em/drive/drive-gen
 cd $srcdir/$pkgname-$pkgver/bin/
 ./drive-gen
 go get github.com/odeke-em/rsc/qr
 go get github.com/martini-contrib/binding
 cd $srcdir/$pkgname-$pkgver/drive-server
 go build -o drive-server
}

package() {
  cd $srcdir/$pkgname-$pkgver/bin/
  install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -p -m755 $srcdir/$pkgname-$pkgver/drive-server/drive-server "$pkgdir/usr/bin"
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
