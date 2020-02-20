# Maintainer: Daniel Landau <aur@landau.fi>
# Contributor: Justin Coffman <jcoffman at datasecu dot red>
# Contributor: Sibren Vasse <arch at sibrenvasse dot nl> 
# Contributor: oozyslug <oozyslug at gmail dot com>
# Submitter: Justin Coffman <jcoffman at datasecu dot red>

pkgname=byobu
pkgver=5.133
pkgrel=1
pkgdesc="Enhanced profile and useful notifications for tmux/screen"
arch=("any")
url="https://launchpad.net/byobu"
license=("GPL3")
depends=("libnewt" "python" "tmux")
install="byobu.install"
makedepends=("gettext")
optdepends=("screen: alternative back-end for byobu (default: tmux)")
source=("${url}/trunk/${pkgver}/+download/${pkgname}_${pkgver}.orig.tar.gz"
"gnome3_desktop_application_not_starting.patch"
)
b2sums=('796cfe22ba60a8cfe41ca6570e4c7f265dd249e7767086341903da7862037f39b1f49434b6dae36d12d82df1ee34306b815ff3f8e703eeedab79cf02e8d86a7d'
	'e3b99b0dfb422b9d0765314901cc29171239262249c2e1714f1d9a85e032dd1bb8161e18f989a43100c8e51c5895ae1c4369904d5215ca3081ead0e83175e31c'
)

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  # arch-specific screens dir
  sed -re 's;^SOCKETDIR=.+$;SOCKETDIR="/tmp/screens";' -i etc/byobu/socketdir	
  sed -re 's;^Icon=byobu+$;Icon=/usr/share/byobu/pixmaps/byobu.svg;' -i usr/share/byobu/desktop/byobu.desktop{,.old}
  ./configure --prefix=/usr --sysconfdir=/etc
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make install DESTDIR="$pkgdir"
  cd "$pkgdir"
  patch -p0 < "${srcdir}/gnome3_desktop_application_not_starting.patch"
}
