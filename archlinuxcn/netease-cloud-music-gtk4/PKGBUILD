# Maintainer: HaoCheng <ch1994@outlook.com>
pkgname=netease-cloud-music-gtk4
_pkgname=netease-cloud-music-gtk
pkgver=2.5.2
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
sha256sums=('890aa1fa4d919268d1645bd88791ab9587ae1f55854b8c92410d1c33a99e1b2b')

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

