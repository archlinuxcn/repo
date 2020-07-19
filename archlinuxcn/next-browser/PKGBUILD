# Contributor: Cillian Berragan <cjberragan@gmail.com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=next-browser
pkgver=1.5.0
pkgrel=4
pkgdesc="Keyboard-oriented, Common Lisp extensible web-browser"
arch=('i686' 'x86_64')
url="https://next.atlas.engineer"
license=('custom:BSD')
source=("$pkgname-$pkgver.tar.gz::https://github.com/atlas-engineer/next/archive/$pkgver.tar.gz")
sha512sums=('a5394b2a7177c8472d5029c1cb040aa3b2445f918a31e4d36cfc55b53154e9659ae4bae0a9bdf26639e803968c99206e1096e1cfb4bbd9a4c2d11ce609ed804c')
# If someday Next works with other Lisps, replace 'sbcl' with 'common-lisp'.
makedepends=('sbcl' 'cl-asdf')
depends=('webkit2gtk' 'sqlite' 'glib-networking' 'gsettings-desktop-schemas' 'libfixposix')
optdepends=('gstreamer: for HTML5 audio/video'
            'gst-plugins-base: for HTML5 audio/video'
            'gst-plugins-good: for HTML5 audio/video'
            'gst-plugins-bad: for HTML5 audio/video'
            'gst-plugins-ugly: for HTML5 audio/video')
conflicts=('nyxt-browser')
# Binary will not run otherwise.
options=('!strip' '!makeflags')

build() {
  cd nyxt-$pkgver
  make all
}

package() {
  cd nyxt-$pkgver
  make install PREFIX=/usr DESTDIR="$pkgdir"
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
