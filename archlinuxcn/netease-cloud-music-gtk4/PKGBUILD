# Maintainer: HaoCheng <ch1994@outlook.com>
pkgname=netease-cloud-music-gtk4
_pkgname=netease-cloud-music-gtk
pkgver=2.5.0
pkgrel=1
pkgdesc="Linux 平台下基于 Rust + GTK4 开发的网易云音乐播放器"
arch=('x86_64')
url="https://github.com/gmg137/netease-cloud-music-gtk"
license=('GPL-3.0-or-later')
depends=(
	'libadwaita'
	'gst-plugins-base'
	'gst-plugins-good'
)
optdepends=(
	'gst-plugins-bad: extra media codecs'
	'gst-plugins-ugly: extra media codecs'
)
makedepends=('cargo' 'meson')
conflicts=(
	'netease-cloud-music-gtk-bin'
	'netease-cloud-music-gtk4-git'
)
source=(
	"https://github.com/gmg137/$_pkgname/archive/$pkgver.tar.gz"
)
sha256sums=('a0bc68ae3851e66922d96ae3b76701fd1991d699093a5923ae31c96db4a5adc3')

prepare(){
	cd $_pkgname-$pkgver
}
build() {
	CFLAGS+=" -ffat-lto-objects"
	arch-meson --buildtype release "$_pkgname-$pkgver" build
	meson compile -C build
}

package() {
	meson install -C build --destdir "$pkgdir"
}

