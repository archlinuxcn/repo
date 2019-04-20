# Maintainer: Bruce Zhang
pkgname=netease-cloud-music-gtk
pkgver=0.3.0
pkgrel=1
pkgdesc="Linux 平台下基于 Rust + GTK 开发的网易云音乐播放器"
arch=('i686' 'x86_64')
url="https://github.com/gmg137/netease-cloud-music-gtk"
license=('GPL3')
depends=('openssl' 'curl' 'gstreamer' 'gtk3' 'gst-plugins-bad' 'gst-plugins-good' 'gst-plugins-ugly' 'gst-libav')
makedepends=('rustup')
source=("https://github.com/gmg137/$pkgname/archive/$pkgver.tar.gz")
sha256sums=('2ad5fc2647c47eb21bef61d338f7fb6fb05ce32f8fba2492e9a693fec43299cb')

build() {
	cd "$pkgname-$pkgver"
	nightly_installed=$(rustup toolchain list | grep nightly | wc -l)
	
	if [ $nightly_installed == '0' ]; then
		rustup toolchain install nightly
	fi

	cargo +nightly build --release

	if [ $nightly_installed == '0' ]; then
		rustup toolchain uninstall nightly
	fi
}

package() {
	cd "$pkgname-$pkgver"
	
	mkdir -p "$pkgdir/usr/bin"
	mkdir -p "$pkgdir/usr/share/applications"
	mkdir -p "$pkgdir/usr/share/icons/hicolor/scalable/apps"

	install -Dm 755 "target/release/netease-cloud-music-gtk" "$pkgdir/usr/bin/netease-cloud-music-gtk"
	install -Dm 755 "netease-cloud-music-gtk.desktop" "$pkgdir/usr/share/applications/netease-cloud-music-gtk.desktop"
	install -Dm 755 "icons/netease-cloud-music-gtk.svg" "$pkgdir/usr/share/icons/hicolor/scalable/apps/netease-cloud-music-gtk.svg"
}
