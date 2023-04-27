# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <youremail@domain.com>
pkgname=payload-dumper-go
pkgver=1.2.2
pkgrel=1
epoch=
pkgdesc="An Android OTA payload dumper written in Go."
arch=(x86_64)
url="https://github.com/ssut/payload-dumper-go"
license=('Apache')
groups=()
depends=()
makedepends=("go>=1.14")
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=(!buildflags)
install=
changelog=
source=(
	$pkgname-$pkgver.tar.gz::https://github.com/ssut/$pkgname/archive/refs/tags/$pkgver.tar.gz
)
noextract=()
md5sums=(SKIP)
validpgpkeys=()

prepare() {
	export GOPATH="$srcdir"/gopath

	cd "$srcdir/$pkgname-$pkgver"
	go mod tidy
	go mod download
}

build() {
	export GOPATH="$srcdir"/gopath
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"

	cd "$srcdir/$pkgname-$pkgver"

	CGO_ENABLE=0 go build -trimpath -o ./$pkgname .
}

package() {
	install -Dt "$pkgdir/usr/bin/" -m755 "$srcdir/$pkgname-$pkgver/$pkgname"
	install -Dt "$pkgdir/usr/share/$pkgname/" -m644 "$srcdir/$pkgname-$pkgver/LICENSE"
}
