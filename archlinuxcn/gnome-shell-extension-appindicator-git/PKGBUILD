# Maintainer: Surefire <surefire at cryptomile dot net>
# Contributor: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: Dave Kleinschmidt <dave.f.kleinschmidt at gmail dot com>
# Contributor: Frikilinux <frikilinux at gmail dot com>

pkgname=gnome-shell-extension-appindicator-git
pkgver=40+1+g4463b84
pkgrel=3
epoch=1
pkgdesc='AppIndicator/KStatusNotifierItem support for GNOME Shell'
url='https://github.com/ubuntu/gnome-shell-extension-appindicator'
license=('GPL')
arch=('any')
conflicts=(${pkgname%-git})
provides=(${pkgname%-git})
depends=('gnome-shell>=3.34')
makedepends=('git' 'jq' 'meson')
optdepends=(
  'libappindicator-gtk2: support GTK+2 applications'
  'libappindicator-gtk3: support GTK+3 applications'
)
source=("${pkgname}::git+${url}.git")
sha512sums=('SKIP')

pkgver() {
	cd "${pkgname}"
	git describe --long --tags | sed 's/^v//; s/-/+/g'
}

build() {
	arch-meson -Dlocal_install=disabled "${pkgname}" build
}

package() {
	meson install -C build --destdir="${pkgdir}"
	rm "${pkgdir}/usr/share/glib-2.0/schemas/gschemas.compiled"
}
