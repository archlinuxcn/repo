# Maintainer: Christoph Gysin <christoph.gysin@gmail.com>
pkgname=(pasystray)
_pkgname=pasystray
pkgver=0.6.0
pkgrel=1
pkgdesc="PulseAudio system tray (a replacement for padevchooser)"
arch=('i686' 'x86_64')
url="https://github.com/christophgysin/pasystray"
license=('LGPL')
groups=('multimedia')
depends=('libpulse' 'gtk3' 'libnotify' 'avahi' 'libx11' 'gnome-icon-theme'
    'gtk-update-icon-cache')
makedepends=('pkg-config' )
optdepends=(
    'pulseaudio: To control a local pulseaudio instance'
    'paman: Launch PulseAudio manager from tray icon'
    'pavucontrol: Launch PulseAudio mixer from tray icon'
    'pavumeter: Launch PulseAudio volume meter from tray icon'
    'paprefs: Launch PulseAudio preferences from tray icon'
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/christophgysin/$_pkgname/archive/$pkgver.tar.gz)
md5sums=('c7467ac2b75290bd086fc60f8243ad77')


build() {
    cd $srcdir/$_pkgname-$pkgver

    autoreconf -is
    ./configure \
        --prefix=/usr \
        --sysconfdir=/etc
    make
}

package() {
    cd $srcdir/$_pkgname-$pkgver
    make DESTDIR="$pkgdir/" install
}
