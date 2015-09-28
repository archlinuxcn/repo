# Maintainer: Ian Denhardt <ian@zenhack.net>

pkgname=xinput_calibrator
pkgver=0.7.5
pkgrel=1
pkgdesc="Generic touchscreen calibration program for X.Org"
arch=('i686' 'x86_64')
url="http://www.freedesktop.org/wiki/Software/xinput_calibrator/"
license=('MIT')
depends=('gtkmm')
source=("http://github.com/downloads/tias/${pkgname}/${pkgname}-${pkgver}.tar.gz")

package() {
    cd "$srcdir/$pkgname-$pkgver"
    ./configure --prefix=/usr
    make
    make DESTDIR="$pkgdir" install
    install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}
md5sums=('20da0a2055a5a75962add8c6b44f60fa')
