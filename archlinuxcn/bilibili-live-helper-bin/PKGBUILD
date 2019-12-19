# Maintainer: OriginCode <origincoder@yahoo.com>

pkgname=bilibili-live-helper-bin
_entryname="Bilibili Live Helper"
_srcname="弹幕库"
_pkgname=bilibili-live-helper
pkgver=2.2.0
pkgrel=1
pkgdesc="A Helper for Bilibili Live Broadcasting."
arch=('x86_64')
url="http://bilibili.danmaku.live/"
install=$_pkgname.install
license=('custom')
depends=('libxtst' 'gtk3' 'libxss' 'nss' 'alsa-lib')
conflicts=('bilibili-live-helper-git')
replaces=('bilibili-live-helper')
provides=('bilibili-live-helper')
source=("http://s2.danmaku.live/$_srcname-linux-v$pkgver.zip" "$_entryname.desktop" "$_pkgname.ico")
sha512sums=('97ca33b3e449f01375398caa312900a72c93cff6704f989687950bb2fb614327cb54fc7cb3950853bef39486532b0f61bba9a8ef9fa24f26308371df61af3471'
            '3e6be3336af1edb333ca519ff01fd4b43920bb02c1197c6768b6bd95abed7e851b4711bcba018d29ce725c7aaf3a202f92427dfb6f9cf0db62fee084b24672a5'
            'e9e2ca9da776ddcf8f259dad2deab208998f22238b2d4ff05d69955324729b71add6b6e628b4b7add354791b175e15525a9ec8371a7ece65a6a8ebe6e052c0e1')
_dirname="$_srcname-linux-v$pkgver"

build() {
	cd "$srcdir/$_dirname"
	mv "$_srcname" "$_pkgname"
}

package() {
	install -Dd "$pkgdir/opt/$_pkgname"
	cp -r "$srcdir/$_dirname"/* "$pkgdir/opt/$_pkgname"
	install -Dm755 ./"$_entryname.desktop" "$pkgdir/usr/share/applications/$_entryname.desktop"
	install -Dm444 ./"$_pkgname.ico" "$pkgdir/usr/share/icons/hicolor/128x128/$_pkgname.ico"
}
