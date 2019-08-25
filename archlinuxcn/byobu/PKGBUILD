# Maintainer: Daniel Landau <aur@landau.fi>
# Contributor: Sibren Vasse <arch at sibrenvasse dot nl> 
# Contributor:  oozyslug <oozyslug at gmail dot com>
# Submitter: oozyslug <oozyslug at gmail dot com>

pkgname=byobu
pkgver=5.129
pkgrel=2
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
md5sums=('7ec69e1c169e3bc8494423176733c8de'
         '23db3b90ae454c00384fcd3af8ad3020')

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
