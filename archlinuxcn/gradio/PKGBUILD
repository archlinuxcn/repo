# Maintainer: ELmoussaoui Bilal <bil.elmoussaoui@gmail.com>
# Maintainer: Julien Nicoulaud <julien dot nicoulaud at gmail dot com>

pkgname=gradio
_pkgname=Gradio
pkgver=7.3
pkgrel=1
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
sha256sums=('5c5afed83fceb9a9f8bc7414b8a200128b3317ccf1ed50a0e7321ca15cf19412')
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
