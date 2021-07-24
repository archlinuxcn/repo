# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>
# Contributor: Davide Depau <davide@depau.eu>
pkgname="obs-xdg-portal-git"
pkgver=0.1.2.r40.gee5241a
pkgrel=1
pkgdesc="OBS Studio plugin using the Desktop portal for Wayland & X11 screencasting"
arch=(x86_64)
url="https://gitlab.gnome.org/feaneron/obs-xdg-portal"
license=('GPL')
depends=('obs-studio>=27' 'xdg-desktop-portal')
makedepends=('meson' 'git')
conflicts=("${pkgname%%-git}")
provides=("${pkgname%%-git}")
source=("git+$url"
        "fix-gs_texture_create_from_dmabuf.patch")
sha256sums=('SKIP'
            '056fa69ca93b8203a72b7ee5d41ad7fca99fcb1af81a3c61e37b4d699961b18c')

prepare() {
  cd ${pkgname%%-git}
  # Add missing parameter to gs_texture_create_from_dmabuf function call
  # to fix https://gitlab.gnome.org/feaneron/obs-xdg-portal/-/issues/30,
  # see:
  # https://gitlab.gnome.org/feaneron/obs-xdg-portal/-/merge_requests/15
  git apply "$srcdir/fix-gs_texture_create_from_dmabuf.patch"
}

pkgver() {
  cd ${pkgname%%-git}
  git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  arch-meson ${pkgname%%-git} build
  meson compile -C build
}

package() {
  DESTDIR="$pkgdir" meson install -C build
}
