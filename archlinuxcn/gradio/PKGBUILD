# Maintainer: ELmoussaoui Bilal <bil.elmoussaoui@gmail.com>
# Maintainer: Julien Nicoulaud <julien dot nicoulaud at gmail dot com>

pkgname=gradio
_pkgname=Gradio
pkgver=7.2
pkgrel=2
pkgdesc='A GTK3 app for finding and listening to internet radio stations'
arch=('i686' 'x86_64')
license=('GPL3')
url="https://github.com/haecker-felix/gradio"
depends=('desktop-file-utils' 'gstreamer' 'gst-plugins-ugly' 'gst-plugins-bad' 
          'gtk3' 'gobject-introspection' 'gst-plugins-base' 'gst-plugins-good' 
          'json-glib' 'libgee' 'sqlite3' 'libsoup')
optdepends=('gst-libav: H.264 video streaming')
makedepends=('gnome-common' 'meson' 'gettext' 'appstream-glib' 'vala' 'yelp-tools')
options=('!emptydirs')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('5a85d7d4afb1424e46c935114b268e4a65de2629d60f48eccd75d67ff4b113d2')
conflicts=('gradio-git' 'gradio-bin')
provides=("gradio=${pkgver}")

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	meson builddir --prefix=/usr
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
  DESTDIR="${pkgdir}" ninja -C builddir install
}
