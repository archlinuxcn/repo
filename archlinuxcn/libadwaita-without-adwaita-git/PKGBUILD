# Maintainer: ich <remove dashes in s-c--25-ni at gmail dot com>

pkgname=libadwaita-without-adwaita-git
pkgver=1.4.0
pkgrel=7
url="https://gnome.pages.gitlab.gnome.org/libadwaita"
pkgdesc='libadwaita; Includes a patch to not overwrite the system theme'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
license=('LGPL')

provides=("libadwaita=${pkgver}" "libadwaita-1.so=0-64")
conflicts=('libadwaita')

_commit=c196ee37a2938ce6ed0bfde2b575a0013d997158  # tags/1.4.0^0
source=(
    "${pkgname}::git+https://gitlab.gnome.org/GNOME/libadwaita.git#commit=$_commit"
    theming_patch.diff
    appstream-1.0-test.patch
)
sha256sums=(
    SKIP
    SKIP
    SKIP
)

depends=(gtk4 appstream)
makedepends=(git meson gi-docgen sassc gobject-introspection vala pkg-config patch cmake meson libsass gcc)

prepare() {
  cd $pkgname   # Support appstream 1.0
  git cherry-pick -n c579fbe0c10d2b761cfe1fe4e825aaa19fe81c77
  git cherry-pick -n 3e3967d5f69180644519936991cad10136e84ca9
  patch -p1 < ../appstream-1.0-test.patch
}

build() {
  cd "${srcdir}/${pkgname}"
  git checkout "${pkgver}"
  <"${srcdir}"/theming_patch.diff patch src/adw-style-manager.c
  meson build --prefix=/usr -Dexamples=false
  ninja -C build 
}

package() {
  cd "${srcdir}/${pkgname}"
  DESTDIR="$pkgdir" ninja -C build install
}
