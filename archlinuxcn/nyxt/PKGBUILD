# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Eric S. Londres <elondres@stevens.edu>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Cillian Berragan <cjberragan@gmail.com>
# Contributor: Felix Golatofski <contact@xdfr.de>

pkgname=nyxt
pkgver=2.pre.release.6
pkgrel=1
pkgdesc="A keyboard-oriented, infinitely extensible web browser designed for power users"
arch=('x86_64')
url="https://github.com/atlas-engineer/nyxt"
license=('custom:BSD')
conflicts=('nyxt-browser')
provides=('nyxt-browser' 'next-browser')
source=("git+https://github.com/atlas-engineer/nyxt.git#commit=37914e99febff8faad6a1ab595e63165e1dd694c")
sha256sums=('SKIP')
# If someday Next works with other Lisps, replace 'sbcl' with 'common-lisp'.
makedepends=('git' 'sbcl' 'cl-asdf')
depends=('webkit2gtk' 'glib-networking' 'gsettings-desktop-schemas' 'libfixposix' 'enchant')
optdepends=('gstreamer: for HTML5 audio/video'
            'gst-plugins-base: for HTML5 audio/video'
            'gst-plugins-good: for HTML5 audio/video'
            'gst-plugins-bad: for HTML5 audio/video'
            'gst-plugins-ugly: for HTML5 audio/video')
# Binary will not run otherwise.
options=('!strip' '!makeflags')

package() {
    cd "${srcdir}"/"${pkgname}"/
    make install PREFIX=/usr DESTDIR="${pkgdir}"/
    install -Dm 644 licenses/ASSET-LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
    install -Dm 644 licenses/SOURCE-LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
}
