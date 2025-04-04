# Maintainer: Mahdi Sarikhani <mahdisarikhani@outlook.com>
# Contributor: jdigi78 <jdigiovanni78 at gmail dot com>

pkgname=varia
pkgver=2025.4.3
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
         'python-gobject'
         'python-requests'
         'yt-dlp')
makedepends=('meson')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('96941b6391a5eec0d3177dd448992192b87e5d5f1ed9ebc90793941e67490dbd')

build() {
    arch-meson "${pkgname}-${pkgver}" build
    meson compile -C build
}

package() {
    meson install -C build --destdir "${pkgdir}"
}
