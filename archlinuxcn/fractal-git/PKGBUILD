# Maintainer: xiretza <xiretza+aur@xiretza.xyz>
# Contributor: Falk Alexander Seidl <fa@terminal.run>

pkgname=fractal-git
_gitname=fractal
epoch=1
pkgver=5.beta1.r6.g5816bdbb
pkgrel=2
pkgdesc="Matrix messaging app for GNOME written in Rust"
arch=('i686' 'x86_64')
license=('GPL3')
url="https://gitlab.gnome.org/GNOME/fractal"
depends=('gtk4' 'gtksourceview5' 'gst-plugins-base-libs' 'gst-editing-services'
         'libadwaita>=1:1.3alpha' 'pipewire' 'libshumate' 'org.freedesktop.secrets'
         'xdg-desktop-portal')
conflicts=('fractal')
provides=("fractal=$pkgver" 'fractal-next')
replaces=('fractal-next')
makedepends=('rust' 'git' 'meson' 'clang')
source=("git+https://gitlab.gnome.org/GNOME/fractal.git")
md5sums=('SKIP')

pkgver() {
	cd "$_gitname"
	git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cd "${srcdir}/${_gitname}/"
	arch-meson . _build
	ninja -C _build
}

package() {
	cd "${srcdir}/${_gitname}/"
	DESTDIR="${pkgdir}" ninja -C _build install
}
