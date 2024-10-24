# Maintainer: Étienne Deparis <etienne@depar.is>

pkgname=goodvibes
pkgver=0.8.1
pkgrel=1
pkgdesc="Lightweight internet radio player"
arch=('i686' 'x86_64')
url="https://gitlab.com/goodvibes/goodvibes"
license=('GPL')
depends=("libkeybinder3" "libsoup" "gst-plugins-base" "gst-plugins-bad" "gst-plugins-good" "gst-plugins-ugly")
makedepends=("meson" "glib2-devel")
source=("https://gitlab.com/${pkgname}/${pkgname}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('7de6b731cbef36921b7be23e6405d6df02e99122b5906bff3c7abbb8d1d105ff')

build() {
    arch-meson -D tests=false "$pkgname-v$pkgver" build
    ninja -C build
}

package() {
    DESTDIR="$pkgdir" ninja -C build install
}
