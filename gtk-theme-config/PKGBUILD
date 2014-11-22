# Maintainer: Ner0

pkgname=gtk-theme-config
pkgver=1.0
pkgrel=1
pkgdesc="A tool to configure GTK theme colors."
arch=('i686' 'x86_64')
url="https://github.com/satya164/gtk-theme-config"
license=('GPL3')
depends=('gconf' 'gsettings-desktop-schemas' 'hicolor-icon-theme')
makedepends=('vala')
conflicts=('gtk-theme-config-git' 'gtk-theme-preferences-git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/satya164/gtk-theme-config/tarball/v$pkgver")
install=gtk-theme-config.install
md5sums=('da1c5bab4a906f0b06da2e18a114268c')

package() {
  cd satya164-*
  make DESTDIR="$pkgdir/" install
}

# vim:set ts=2 sw=2 et:
