# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
pkgname=go-tun2socks
pkgver=1.16.11
pkgrel=2
pkgdesc="A tun2socks implementation written in Go."
arch=(x86_64)
url=https://github.com/eycorsican/go-tun2socks
license=(MIT)
makedepends=(go git)
source=(
	$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz
	build-flags.patch
	go-tun2socks.service
	go-tun2socks.conf
	go-tun2socks-setup
)
sha512sums=('e64bab61feefadfa5af1752b7b7dbad78d4d1ba706e7b07a130c1a7a78638036cc439f394fbdc92337eb718acc50f2b6b58b46eb2a248e698eaafbd75c0ceeb4'
            'e2fdd62f9b4f6077c08f0783840294177e46874a28ff4fe5a0b09e18419f9d44e0f318f8986e8d5b12156eac01775e7d2cecdc86c17dce4f300a33575b62fc22'
            'bed1333077c69517e6c02bfc73b62a0d87e27c8e8f7b141dedd7a0e4be87dd7fba76b10f2cf254b8efcd4aa657b2c7fa4c6b83ca2127f5a8904757aa9f5a1656'
            '3c878b5004f4aed59635d832b22199c2550abb46b4ede49221d904a37f0e1088cb976d4d73966c7d2826b5b86b352937d37824f1e76ce461eed1ca8ce9ca6521'
            '48866fe1daebaad2575cee74d43c74274a1a879d821d4b4aed08215dd1642e0a76f3a865d0e0ea6675c630b81f3a7d907edfa6112c957a47245da5e116f1fabc')
gosrcdir=gopath/src/github.com/eycorsican
prepare() {
	mkdir -p $gosrcdir
	ln -rTsf $pkgname-$pkgver $gosrcdir/$pkgname
	export GOPATH="$PWD/gopath"
	cd $gosrcdir/$pkgname
	patch -Np1 -i "$srcdir/build-flags.patch"
	go get -d -v ./...
}
build() {
	cd "$gosrcdir/$pkgname"
	make VERSION=v$pkgver
}
package() {
	install -Dm755 $gosrcdir/$pkgname/build/tun2socks "$pkgdir/usr/bin/go-tun2socks"
	install -Dm644 go-tun2socks.service "$pkgdir/usr/lib/systemd/system/go-tun2socks.service"
	install -Dm644 go-tun2socks.conf "$pkgdir/etc/systemd/system/go-tun2socks.service.d/go-tun2socks.conf"
	install -Dm755 go-tun2socks-setup "$pkgdir/usr/lib/systemd/scripts/go-tun2socks-setup"
}
