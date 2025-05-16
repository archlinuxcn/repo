# Maintainer: Mahdi Sarikhani <mahdisarikhani@outlook.com>
# Contributor: jdigi78 <jdigiovanni78 at gmail dot com>

pkgname=varia
pkgver=2025.5.14
pkgrel=1
pkgdesc="Download manager based on aria2"
arch=('any')
url="https://github.com/giantpinkrobots/varia"
license=('MPL-2.0')
depends=('aria2'
         'aria2p'
         'bash'
         'dconf'
         'ffmpeg'
         'glib2'
         'gtk4'
         'hicolor-icon-theme'
         'libadwaita'
         'pango'
         'python'
         'python-dbus-next'
         'python-gobject'
         'python-pystray'
         'python-requests'
         'yt-dlp')
makedepends=('meson')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('c50a77aec556a48d7e97e40340cc1fdb2201f673f9f71615fec457451ac2dc54')

build() {
    arch-meson "${pkgname}-${pkgver}" build
    meson compile -C build
}

package() {
    meson install -C build --destdir "${pkgdir}"
}
