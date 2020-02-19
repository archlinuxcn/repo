# Contributor: Cillian Berragan <cjberragan@gmail.com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=next-browser
pkgver=1.4.0
pkgrel=2
pkgdesc="Keyboard-oriented, Common Lisp extensible web-browser"
arch=('i686' 'x86_64')
url="https://next.atlas.engineer"
license=('custom:BSD')
source=("$pkgname-$pkgver.tar.gz::https://github.com/atlas-engineer/next/archive/$pkgver.tar.gz")
sha512sums=('a94b81c1b417818a06ddc592aa44620704a91b4ed411c92f19a768c4f7d4f9f74d29b9ad7a320d7a27ebaf880fa356c76626c1e2a9bac2c17bfeb6838cd1f937')
# If someday Next works with other Lisps, replace 'sbcl' with 'common-lisp'.
makedepends=('sbcl' 'cl-asdf')
depends=('webkit2gtk' 'sqlite' 'glib-networking' 'gsettings-desktop-schemas' 'libfixposix')
optdepends=('gstreamer: for HTML5 audio/video'
            'gst-plugins-base: for HTML5 audio/video'
            'gst-plugins-good: for HTML5 audio/video'
            'gst-plugins-bad: for HTML5 audio/video'
            'gst-plugins-ugly: for HTML5 audio/video')
# Binary will not run otherwise.
options=('!strip' '!makeflags')

build() {
  cd ${pkgname%-browser}-$pkgver
  make all
}

package() {
  cd ${pkgname%-browser}-$pkgver
  make install PREFIX=/usr DESTDIR="$pkgdir"
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
