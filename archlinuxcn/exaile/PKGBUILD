# Maintainer: X0rg
# Contributor: Tom Kwok <contact@tomkwok.com>
# Contributor: Jorge Barroso <jorge.barroso.11 at gmail dot com>
# Contributor: Roman Kyrylych <Roman.Kyrylych@gmail.com>
# Contributor: Benjamin Wild <benwild@gmx.de>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# Contributor: Joshua Stiefer <facedelajunk@gmail.com>

pkgname=exaile
pkgver=4.1.1
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
	#'python-discid: CD info'
	'spydaap: DAAP server'
	'python-zeroconf: DAAP plugins (daapserver and daapclient)'
	'ipython: ipconsole plugin'
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
source=("$pkgname-$pkgver.tar.gz::https://github.com/exaile/exaile/archive/$pkgver.tar.gz")
sha512sums=('babf37253054fbeb6dad33aedafe969201860d4f35222d577343256730be943682c1a5f2f7cec7c574695624cb2b7abbdff4e6eaada848d22fea073c2c44bd23')

prepare() {
	sed -i 's/new_for_uri/new_for_path/' "$srcdir/$pkgname-$pkgver/xl/trax/util.py"
}

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
