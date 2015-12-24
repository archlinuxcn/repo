# Maintainer: CanalGuada <dguadal at free dot fr>
# Author: horst3180 @ deviantart

pkgname=vertex-themes
pkgver=20150923
pkgrel=2
pkgdesc='Vertex Gtk2, Gtk3, Metacity, Xfwm, Cinnamon and GNOME Shell themes (GNOME 3.18 version)'
_gnomever=3.18
_releasever=20150923
arch=('any')
url='http://horst3180.deviantart.com/art/Vertex-Theme-470663601'
license=('GPL3')
depends=('gtk-engine-murrine')
conflicts=('vertex-themes-git')
source=("${pkgname}-${_releasever}.tar.gz::https://github.com/horst3180/Vertex-theme/archive/${_releasever}.tar.gz")
sha256sums=('8484edaf1e9324676a9ebe76c58bb46e0aacbe289a3ee40d01f717e8fde3eb51')

build() {
  cd Vertex-theme-${_releasever}
  ./autogen.sh --prefix=/usr --with-gnome=${_gnomever}
}
package() {
  cd Vertex-theme-${_releasever}

  make DESTDIR="$pkgdir" install
  cd extra
  for name in "Chrome" "Firefox" "Vertex-Plank" "Vertex_alt_metacity"; do
    find "$name" -type f -not -name *~ -exec install -Dm644 '{}' "$pkgdir/usr/share/themes/{}" \;
  done

  cd ..
  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
  install -Dm644 README.md "$pkgdir/usr/share/themes/Vertex/README"
}

# vim: ts=2 sw=2 et:
