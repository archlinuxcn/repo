pkgname=paper-icon-theme-git
pkgver=368.45207e8
pkgrel=1
pkgdesc="Paper is an icon theme for GTK based desktops and fits perfectly the paper-gtk-theme"
arch=(any)
url="https://github.com/snwh/paper-icon-theme"
license=('CC BY-SA 4.0')
depends=('gtk-update-icon-cache')
makedepends=('git' 'automake')
provides=('paper-icon-theme')
source=("$pkgname"::'git+https://github.com/snwh/paper-icon-theme.git')
# Because the sources are not static, skip Git checksum:
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$pkgname"
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
	cd "$srcdir/$pkgname"
	./autogen.sh --prefix=/usr
	make
}

package() {
  cd "$srcdir/$pkgname"
  make DESTDIR="$pkgdir" install
  rm -f "${pkgdir}/usr/share/icons/gnome/icon-theme.cache"
}
