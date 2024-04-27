# Contributor: Matthew Bauer <mjbauer95@gmail.com>
# Contributor: TingPing <tingping@fedoraproject.org>
# Contributor: Christopher Eby <kreed@kreed.org>
# Contributor: Steven Allen <steven@stebalien.com>

pkgname=pithos
pkgver=1.6.2
pkgrel=2
pkgdesc='Native Pandora Radio client'
arch=(any)
url="https://pithos.github.io/"
license=(GPL-3.0-only)
depends=('gtk3' 'python-gobject' 'libsecret' 'python-cairo' 'pango'
         'python' 'dconf' 'gdk-pixbuf2' 'hicolor-icon-theme'
         'gst-plugins-good' 'gst-libav' 'gst-plugins-base')
optdepends=('libkeybinder3: for media keys plugin'
            'python-pacparser: PAC proxy support'
            'python-pylast: Last.fm scrobbling support'
            'python-systemd: Logging to the system journal')
makedepends=('meson' 'appstream-glib')
source=(
  "pithos-${pkgver}.tar.gz::https://github.com/pithos/pithos/archive/refs/tags/${pkgver}.tar.gz"
  "systemd.service"
)
sha256sums=('69fffb5af07787eaf603d9e63b6facf25cc41760109dee5a92514354edd1068d'
            '6d29178697384fb046d9d25c6c2482f353a4484ec4f0a5b9080d1a26aa24f839')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  echo "SystemdService=pithos.service" >> "data/io.github.Pithos.service.in"
}

build() {
  cd "${srcdir}"
  if [[ -d ./build/ ]]; then
         rm -rf ./build/
  fi
  mkdir build
  meson "${pkgname}-${pkgver}" build --prefix=/usr
}

package() {
  cd "${srcdir}/build"
  DESTDIR="${pkgdir}" ninja install
  install -Dm644 "${srcdir}/systemd.service" "${pkgdir}/usr/lib/systemd/user/pithos.service"
}
