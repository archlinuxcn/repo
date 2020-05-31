# Maintainer: X0rg
# Contributor: Tom Kwok <contact@tomkwok.com>
# Contributor: Jorge Barroso <jorge.barroso.11 at gmail dot com>
# Contributor: Roman Kyrylych <Roman.Kyrylych@gmail.com>
# Contributor: Benjamin Wild <benwild@gmx.de>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# Contributor: Joshua Stiefer <facedelajunk@gmail.com>

pkgname=exaile
_pkgver=4.1.0-alpha1
pkgver=${_pkgver//-/}
pkgrel=2
pkgdesc="A full-featured Amarok-style media player for GTK+"
arch=('any')
url="https://www.exaile.org/"
license=('GPL2')
depends=('python>=3.6'
	'python-bsddb'
	'gtk3>=3.22.0'
	'gst-python>=1.14.0'
	'gst-plugins-base>=1.14.0'
	'gst-plugins-good>=1.14.0'
	'python-mutagen>=1.38.0'
	'python-dbus'
	'python-cairo'
	'python-gobject')
makedepends=('pygobject-devel>=3.22.0' 'help2man')
checkdepends=('python-mox3' 'python-pytest')
optdepends=('udisks2: device detection'
	'cddb-py: CD info'
	'python-zeroconf: DAAP plugins (daapserver and daapclient)'
	'python-pylast: Last.FM integration'
	'python-lxml: lyrics from lyricsmania.com (lyricsmania)'
	'python-beautifulsoup4: lyrics from lyrics.wikia.com (lyricwiki)'
	'python-musicbrainzngs: Musicbrainz covers'
	'python-feedparser: podcast plugin'
	'webkit2gtk: Wikipedia info'
	'libkeybinder3: Xlib-based hotkeys'
	'librsvg: scalable icons'
	'libnotify: recording streams'
	'moodbar: moodbar plugin'
	'gst-plugins-bad: BPM Counter plugin')
source=("$pkgname-$_pkgver.tar.gz::https://github.com/exaile/exaile/archive/$_pkgver.tar.gz")
sha512sums=('56e73f7cc4d250fbc30870170b50f65f0f99d27e97a8f28dd043af9eb93c919a8de3ed790cbd6c441133232afb3c405fa830cb62c8c33bb0a6e4d97b79d5b54d')

build() {
	cd "$srcdir/$pkgname-$_pkgver"
	make PREFIX="/usr"
}

check() {
	cd "$srcdir/$pkgname-$_pkgver"
	make PYTEST=py.test test
}

package() {
	cd "$srcdir/$pkgname-$_pkgver"
	make PREFIX="/usr" DESTDIR="$pkgdir" install
}
