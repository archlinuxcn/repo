# Maintainer: Artem Vorotnikov <artem@vorotnikov.me>
# Contributor: Abi Hafshin <abi@hafs.in>

pkgname=xfce4-indicator-plugin
_pkgname=xfce4-indicator-plugin
pkgver=2.3.3
_major=2.3
pkgrel=1
pkgdesc="Plugin to display information from applications in the Xfce4 panel"
arch=('i686' 'x86_64')
url="http://goodies.xfce.org/projects/panel-plugins/xfce4-indicator-plugin"
license=('GPL')
depends=('xfce4-panel' 'libindicator-gtk2' 'libindicator-gtk3' 'hicolor-icon-theme' 'xdg-utils')
makedepends=('intltool' 'xfce4-dev-tools')
optdepends=('indicator-application-gtk2: take menus from applications and place them in the panel'
            'indicator-sound-gtk2: unified sound menu'
            'indicator-sound: GTK3 unified sound menu')
install=$pkgname.install
source=(http://archive.xfce.org/src/panel-plugins/xfce4-indicator-plugin/${_major}/${_pkgname}-${pkgver}.tar.bz2)

prepare() {
  cd "$srcdir/$_pkgname-$pkgver"
}

build() {
  cd "$srcdir/$_pkgname-$pkgver"

  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib --disable-static
  make
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  make DESTDIR="$pkgdir/" install
}

sha256sums=('c46b529b0f31c8ba9401fdc3e245ed3f30e61fadc0e8d2ddb6aaa10b02edbd52')
