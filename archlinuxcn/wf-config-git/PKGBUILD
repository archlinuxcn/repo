# Maintainer: Solomon Choina <shlomochoina@gmail.com>
pkgname=wf-config-git 
pkgver=r45.dd6f495
pkgrel=1
pkgdesc="A library for managing configuration files, written for wayfire"
arch=('x86_64')
url="https://github.com/WayfireWM/wf-config"
license=('MIT')
depends=('libevdev' 'wlroots-git')
makedepends=('git' 'meson' 'ninja' 'wayland-protocols')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
replaces=()
options=()
source=('git+https://github.com/WayfireWM/wf-config')
sha256sums=('SKIP')

pkgver() {
	cd "$srcdir/wf-config"

# Git, no tags available
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"

}

build() {
	cd "$srcdir/wf-config/"
  arch-meson build
  ninja -C build
}


package() {
	cd "$srcdir/wf-config"
	DESTDIR="$pkgdir/" ninja -C build install
}
