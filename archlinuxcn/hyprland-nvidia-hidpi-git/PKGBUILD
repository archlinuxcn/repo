# Maintainer: Integral <integral@murena.io>
# Contributor: Aleksana QwQ <me@aleksana.moe>
# Contributor: q234 rty <q23456yuiop at gmail dot com>
# Contributor: ThatOneCalculator <kainoa@t1c.dev>
# Contributor: lilydjwg <lilydjwg@gmail.com>

_pkgname="hyprland"
pkgname="${_pkgname}-nvidia-hidpi-git"
pkgver=0.32.3.r74.ad3f6886
pkgrel=1
pkgdesc="A dynamic tiling Wayland compositor based on wlroots that doesn't sacrifice on its looks. (NVIDIA + HiDPI patch)"
arch=("i686" "x86_64" "arm" "armv6h" "armv7h" "aarch64" "riscv64")
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
	libdisplay-info
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
	xorg-xwayland-hidpi-xprop
	libdisplay-info.so)
makedepends=(
	git
	cmake
	ninja
	gcc
	meson
	vulkan-headers
	wayland-protocols
	xorgproto
	jq)
source=("${_pkgname}::git+https://github.com/hyprwm/Hyprland.git"
	"git+https://gitlab.freedesktop.org/wlroots/wlroots.git"
	"git+https://github.com/hyprwm/hyprland-protocols.git"
	"git+https://github.com/canihavesomecoffee/udis86.git"
	"0001-xwayland-support-HiDPI-scale.patch"
	"0002-Fix-configure_notify-event.patch"
	"0003-Fix-size-hints-under-Xwayland-scaling.patch"
	"nvidia.patch")
conflicts=("${_pkgname}")
provides=("${_pkgname}")
sha256sums=('SKIP'
	'SKIP'
	'SKIP'
	'SKIP'
	'b717f2f61aeb3bf670fe60424a8cd638d51e73dc66bd84277fada289bf2330d8'
	'1314d0ee63a4249698791d86cce5e6cdb4f005b81bbb1c6a747578d2a9223795'
	'c08dd62a1786eeb7506f1839bfcbba791502360392c929e620244f70c8ca5b61'
	'c200d341641ee20a13b1893e27a9d823e9ef5ac2378e3cdecd0efc55a713db1c')

pkgver() {
	git -C "${_pkgname}" describe --long --tags | sed 's/^v//;s/\([^-]*-\)g/r\1/;s/-/./g'
}

prepare() {
	cd "${_pkgname}/"
	rm -rf subprojects/{wlroots,hyprland-protocols}
	git submodule init
	git config submodule.wlroots.url "${srcdir}/wlroots"
	git config submodule.subprojects/hyprland-protocols.url "${srcdir}/hyprland-protocols"
	git config submodule.subprojects/udis86.url "${srcdir}/udis86"
	git -c protocol.file.allow=always submodule update subprojects/wlroots
	git -c protocol.file.allow=always submodule update subprojects/hyprland-protocols
	git -c protocol.file.allow=always submodule update subprojects/udis86

	cd subprojects/wlroots/
	git revert -n 18595000f3a21502fd60bf213122859cc348f9af
	patch -Np1 -i "${srcdir}/0001-xwayland-support-HiDPI-scale.patch"
	patch -Np1 -i "${srcdir}/0002-Fix-configure_notify-event.patch"
	patch -Np1 -i "${srcdir}/0003-Fix-size-hints-under-Xwayland-scaling.patch"
	patch --forward --strip=0 --input="${srcdir}/nvidia.patch"
	sed -i 's/soversion = 12/soversion = 13/g' ../packagefiles/wlroots-meson-build.patch
	patch -p1 <../packagefiles/wlroots-meson-build.patch

	rm -rf build/
}

build() {
	cd "${_pkgname}/"

	meson setup build \
		--prefix /usr \
		--libexecdir lib \
		--sbindir bin \
		--buildtype plain \
		--wrap-mode nodownload \
		-D b_lto=true \
		-D b_pie=true \
		-D default_library=shared \
		-D xwayland=enabled

	ln -sf wlroots build/subprojects/wlroots/include/wlr
	meson compile -C build
}

package() {
	cd "${_pkgname}/"

	meson install -C build --destdir "${pkgdir}"

	rm -rf "${pkgdir}/usr/include/hyprland/wlroots/wlr/"
	ln -sf . "${pkgdir}/usr/include/hyprland/wlroots/wlr"

	# resolve conflicts with system wlr
	rm -f "${pkgdir}/usr/lib/libwlroots.so"
	rm -f "${pkgdir}/usr/lib/pkgconfig/wlroots.pc"

	# resolve conflicts with xdg-desktop-portal-hyprland from repo
	rm -rf "${pkgdir}/usr/share/xdg-desktop-portal/"
	rm -rf "${pkgdir}/usr/share/hyprland-protocols/"
	rm -rf "${pkgdir}/usr/share/pkgconfig/hyprland-protocols.pc"

	# FIXME: meson.build shall install version.h
	install -Dm644 src/version.h -t "${pkgdir}/usr/include/hyprland/src/"

	# License
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${_pkgname}/"
}
