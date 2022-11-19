# Maintainer: HaoCheng <ch1994@outlook.com>
pkgname=netease-cloud-music-gtk4
_pkgname=netease-cloud-music-gtk
pkgver=2.1.0
pkgrel=3
pkgdesc="Linux 平台下基于 Rust + GTK4 开发的网易云音乐播放器"
arch=('x86_64')
url="https://github.com/gmg137/netease-cloud-music-gtk"
license=('GPL3')
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
	"0001-Single-isahc-client.patch"
	"0002-More-ncmapi-log.patch"
)
sha256sums=('1ff23078038c63a1365d6a6f76461080df446d343f1bf69ee0ae56b46a2f9099'
            'b22ecebacee3334971e3403e6a78e7d72a8970fc31c3274ead81e206a634b33f'
            '7c65bb4f93c552f550fe9b440995867d5a5c25285dbff685f3fe1abc32a8cc41')

prepare(){
	cd $_pkgname-$pkgver
	patch -Np1 < $srcdir/0001-Single-isahc-client.patch
	patch -Np1 < $srcdir/0002-More-ncmapi-log.patch

}
build() {
	CFLAGS+=" -ffat-lto-objects"
	arch-meson --buildtype release "$_pkgname-$pkgver" build
	meson compile -C build
}

package() {
	meson install -C build --destdir "$pkgdir"
}

