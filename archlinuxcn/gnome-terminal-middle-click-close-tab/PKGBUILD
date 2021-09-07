# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>

_pkgname="gnome-terminal"
pkgname="${_pkgname}-middle-click-close-tab"
pkgver=3.40.3
pkgrel=1
pkgdesc="The GNOME Terminal Emulator, with a patch that can use middle click to close tab"
url="https://wiki.gnome.org/Apps/Terminal"
arch=(x86_64)
license=(GPL)
depends=('vte3>=0.64.0' gsettings-desktop-schemas)
makedepends=(docbook-xsl libnautilus-extension gnome-shell yelp-tools git)
# Don't add modified one to gnome group.
#groups=(gnome)
provides=("${_pkgname}=${pkgver}")
conflicts=("${_pkgname}")
_commit=40d226a2d58b5bd2ef38ce9871c7b27fcd4a0928  # tags/3.40.3^0
source=("git+https://gitlab.gnome.org/GNOME/gnome-terminal.git#commit=${_commit}"
        "gnome-terminal-middle-click-close-tab.patch")
sha256sums=('SKIP'
            'd1b8483646b5de4a6a7486667caa56baf70eaee1ba306d9a500ea2bb2db085e1')

pkgver() {
  cd ${_pkgname}
  git describe --tags | sed 's/-/+/g'
}

prepare() {
  cd ${_pkgname}
  patch --forward --strip=1 --input="${srcdir}/gnome-terminal-middle-click-close-tab.patch"
  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd ${_pkgname}
  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var \
    --libexecdir=/usr/lib --disable-static --with-nautilus-extension
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

check() {
  cd ${_pkgname}
  make check
}

package() {
  cd ${_pkgname}
  make DESTDIR="${pkgdir}" install
}
