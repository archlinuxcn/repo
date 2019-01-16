# Maintainer: aimileus <me at aimileus dot nl>
# Contributor: zfo <zfoofz1@gmail.com>
pkgname=gcsfuse
pkgver=0.23.0
pkgrel=1
pkgdesc="A user-space file system for interacting with Google Cloud Storage"
url="https://github.com/GoogleCloudPlatform/gcsfuse"
arch=('x86_64')
license=('APACHE')
depends=('glibc')
makedepends=('git' 'go-pie')
optdepends=('google-cloud-sdk: authentication helper')
source=("$pkgname-$pkgver::https://github.com/GoogleCloudPlatform/gcsfuse/archive/v$pkgver.tar.gz")
sha256sums=('beb90ef68d5ab673bf09357c90d1ace94695bebb6f823ba715a92b30e61e7c39')
_gourl=github.com/googlecloudplatform/gcsfuse

prepare() {
  export GOPATH="$srcdir/go"  
  mkdir -p "$GOPATH/src/$(dirname $_gourl)"
  ln -sf "$srcdir/$pkgname-$pkgver" "$GOPATH/src/$_gourl"
}

build() {
  export GOPATH="$srcdir/go"  
  go build "$_gourl"
}

package() {
  install -Dm755 gcsfuse "${pkgdir}/usr/bin/gcsfuse"
}

# vim:set ts=2 sw=2 et:
