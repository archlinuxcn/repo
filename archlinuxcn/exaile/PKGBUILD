# Maintainer: UnicornDarkness
# Contributor: Tom Kwok <contact@tomkwok.com>
# Contributor: Jorge Barroso <jorge.barroso.11 at gmail dot com>
# Contributor: Roman Kyrylych <Roman.Kyrylych@gmail.com>
# Contributor: Benjamin Wild <benwild@gmx.de>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# Contributor: Joshua Stiefer <facedelajunk@gmail.com>

pkgname=exaile
pkgver=4.1.3
pkgrel=1
pkgdesc="A full-featured Amarok-style media player for GTK+"
arch=('any')
url="https://www.exaile.org/"
license=('GPL2')
depends=('python>=3.8'
	'python-bsddb'
	'gtk3>=3.24.0'
	'gst-python>=1.16.0'
	'gst-plugins-base>=1.16.0'
	'gst-plugins-good>=1.16.0'
	'python-mutagen>=1.44.0'
	'python-dbus'
	'python-cairo'
	'python-gobject>=3.24.0')
makedepends=('pygobject-devel>=3.24.0' 'help2man')
checkdepends=('python-pytest')
optdepends=('udisks2: device detection'
	'python-discid: CD info'
	'python-musicbrainzngs: CD info / Musicbrainz covers'
	'spydaap: DAAP server'
	'python-zeroconf: DAAP plugins (daapserver and daapclient)'
	'python-pylast: Last.FM integration'
	'python-lxml: lyrics from lyricsmania.com (lyricsmania)'
	'python-feedparser: podcast plugin'
	'webkit2gtk: Wikipedia info'
	'libkeybinder3: Xlib-based hotkeys'
	'librsvg: scalable icons'
	'libnotify: native notifications'
	'streamripper: recording streams'
	'moodbar: moodbar plugin'
	'gst-plugins-bad: BPM Counter plugin'
	'python-beautifulsoup4: lyrics from lyrics.wikia.com (lyricwiki)'
	'ipython: ipconsole plugin')
source=("$pkgname-$pkgver.tar.gz::https://github.com/exaile/exaile/archive/$pkgver.tar.gz")
sha512sums=('16b31331a31f0a2e088f177c8a01ef47603b07fe94cbb19869a4caeaec2da03cacaa07d5b0eb50052645449e07620e2c58f202007108af73e20cf744d70bb556')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	make PREFIX="/usr"
}

check() {
	cd "$srcdir/$pkgname-$pkgver"
	make PYTEST=py.test test
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make PREFIX="/usr" DESTDIR="$pkgdir" install
}
