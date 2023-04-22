# Maintainer: Integral <integral@murena.io>

_pkgname=hyprland
pkgname="${_pkgname}-nvidia-hidpi-git"
pkgver=r2806.d366fc48
pkgrel=1
pkgdesc="A dynamic tiling Wayland compositor based on wlroots that doesn't sacrifice on its looks. (NVIDIA + HiDPI patch)"
arch=(any)
url="https://github.com/hyprwm/Hyprland"
license=('BSD')
depends=(
	libxcb
	xcb-proto
	xcb-util
	xcb-util-keysyms
	libxfixes
	libx11
	libxcomposite
	xorg-xinput
	libxrender
	pixman
	wayland-protocols
	cairo
	pango
	polkit
	glslang
	libinput
	libxcb
	libxkbcommon
	opengl-driver
	pixman
	wayland
	xcb-util-errors
	xcb-util-renderutil
	xcb-util-wm
	seatd
	vulkan-icd-loader
	vulkan-validation-layers
	xorg-xwayland-lily
	libdisplay-info-git)
makedepends=(
	git
	cmake
	ninja
	gcc
	gdb
	meson
	vulkan-headers
	wayland-protocols
	xorgproto)
source=("${_pkgname}::git+https://github.com/hyprwm/Hyprland.git"
	"git+https://gitlab.freedesktop.org/wlroots/wlroots.git"
	"git+https://github.com/hyprwm/hyprland-protocols.git"
	"git+https://github.com/canihavesomecoffee/udis86.git"
	"xwayland-support-HiDPI-scale.patch"
	"fix-configure_notify-event.patch"
	"nvidia.patch")
conflicts=("${_pkgname}")
provides=(hyprland)
sha256sums=('SKIP'
	'SKIP'
	'SKIP'
	'SKIP'
	'497afb5e99cb069ed96a3c4a735ad23afe0d012ca845067aae3176e45e267ba5'
	'e7cf16e39db2bde4dbc9d7ec3b4753f7643b1bf198a3179e6802a9c603437fe9'
	'522b19656d7c1627ec615b6720182590570560e346c1670f9df002015707b340')
options=(!makeflags !buildflags !strip)

pkgver() {
	cd "$_pkgname"
	(
		set -o pipefail
		git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
			printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

prepare() {
	cd "${srcdir}/${_pkgname}"
	rm -rf subprojects/wlroots subprojects/hyprland-protocols
	git submodule init
	git config submodule.wlroots.url "${srcdir}"/wlroots
	git config submodule.subprojects/hyprland-protocols.url "${srcdir}"/hyprland-protocols
	git config submodule.subprojects/udis86.url "${srcdir}"/udis86
	git -c protocol.file.allow=always submodule update subprojects/wlroots
	git -c protocol.file.allow=always submodule update subprojects/hyprland-protocols
	git -c protocol.file.allow=always submodule update subprojects/udis86
	cd subprojects/wlroots
	git revert -n 18595000f3a21502fd60bf213122859cc348f9af
	patch --forward --strip=1 --input="${srcdir}"/xwayland-support-HiDPI-scale.patch
	patch --forward --strip=1 --input="${srcdir}"/fix-configure_notify-event.patch
	patch --forward --strip=0 --input="${srcdir}"/nvidia.patch
}

build() {
export CFLAGS+=-w
	cd "${srcdir}/${_pkgname}"
	make fixwlr
	cd "./subprojects/wlroots/" && meson build/ --prefix="${srcdir}/tmpwlr" --buildtype=release && ninja -C build/ && mkdir -p "${srcdir}/tmpwlr" && ninja -C build/ install && cd ../../
	cd "./subprojects/udis86/" && cmake --no-warn-unused-cli -DCMAKE_BUILD_TYPE:STRING=Release -H./ -B./build -G Ninja && cmake --build ./build --config Release --target all -j$(shell nproc) && cd ../../
	make protocols
	make release
	cd ./hyprctl && make all && cd ..
}

package() {
	cd "${srcdir}/${_pkgname}"
	mkdir -p "${pkgdir}/usr/share/wayland-sessions"
	mkdir -p "${pkgdir}/usr/share/hyprland"
	install -Dm755 build/Hyprland -t "${pkgdir}/usr/bin"
	install -Dm755 hyprctl/hyprctl -t "${pkgdir}/usr/bin"
	install -Dm644 assets/*.png -t "${pkgdir}/usr/share/hyprland"
	install -Dm644 example/hyprland.desktop -t "${pkgdir}/usr/share/wayland-sessions"
	install -Dm644 example/hyprland.conf -t "${pkgdir}/usr/share/hyprland"
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${_pkgname}"
	install -Dm755 ../tmpwlr/lib/libwlroots.so.* -t "${pkgdir}/usr/lib"
}
