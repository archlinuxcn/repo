# Maintainer: X0rg
# Contributor: Tom Kwok <contact@tomkwok.com>
# Contributor: Jorge Barroso <jorge.barroso.11 at gmail dot com>
# Contributor: Roman Kyrylych <Roman.Kyrylych@gmail.com>
# Contributor: Benjamin Wild <benwild@gmx.de>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# Contributor: Joshua Stiefer <facedelajunk@gmail.com>

pkgname=exaile
pkgver=4.0.2
pkgrel=1
pkgdesc="A full-featured Amarok-style media player for GTK+"
arch=('any')
url="https://www.exaile.org/"
license=('GPL2')
depends=('python2>=2.7'
	'gtk3>=3.10.0'
	'gst-python2>=1.4.0'
	'gst-plugins-base>=1.6.0'
	'gst-plugins-good>=1.4.0'
	'python2-mutagen>=1.10.0'
	'python2-dbus'
	'pygobject-devel>=3.13.2'
	'python2-cairo')
makedepends=('help2man')
checkdepends=('python2-mox3' 'python2-pytest')
optdepends=('udisks2: device detection'
	'cddb-py: CD info'
	'spydaap: DAAP plugins (daapserver and daapclient)'
	'python2-pylast: Last.FM integration'
	'python2-beautifulsoup4: lyrics from lyrics.wikia.com (lyricwiki)'
	'python2-musicbrainzngs: Musicbrainz covers'
	'python2-feedparser: podcast plugin'
	'webkit2gtk: Wikipedia info'
	'libkeybinder3: Xlib-based hotkeys'
	'librsvg: scalable icons')
source=("https://github.com/$pkgname/$pkgname/releases/download/$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('4b0629d68d426493b8ba9295c755919c9d9919ee916952339b06206b8e1eb86145e5c5975cc21ecd8b9ab6b266eaaff0855e9a5154beb951033564a6dcf0ca37')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	make PREFIX="/usr"
}

check() {
	cd "$srcdir/$pkgname-$pkgver"
	make PYTEST="py.test2" test
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make PREFIX="/usr" DESTDIR="$pkgdir" install
}
