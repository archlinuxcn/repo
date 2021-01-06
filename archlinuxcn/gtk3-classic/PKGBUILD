# Maintainer: Jonathon Fernyhough <jonathon+m2x.dev>
# Upstream maintainer: Luke Horwell
# Contributor: Tomasz Gąsior <tomaszgasior.pl>

# This file is based on original PKGBUILD of GTK3 package.
# https://git.archlinux.org/svntogit/packages.git/plain/trunk/PKGBUILD?h=packages/gtk3

__arch_pkg_commit="408873e9af613dc26f6d434fe489735fb8c5de75"
_gtkver=3.24.24

pkgbase=gtk3-classic
pkgname=($pkgbase lib32-$pkgbase)
pkgver=${_gtkver}
pkgrel=1
pkgdesc="GTK3 patched for classic desktops like XFCE or MATE. Please see README."
url="https://github.com/lah7/gtk3-mushrooms"
conflicts=(gtk3 gtk3-typeahead gtk3-print-backends)
provides=(gtk3=$_gtkver gtk3-typeahead=$_gtkver gtk3-mushrooms=$_gtkver gtk3-print-backends
          libgtk-3.so libgdk-3.so libgailutil-3.so)
arch=(x86_64)
license=(LGPL)
makedepends=(
	gobject-introspection libcanberra gtk-doc sassc libcups meson quilt

	atk cairo libxcursor libxinerama libxrandr libxi libepoxy gdk-pixbuf2 fribidi
	libxcomposite libxdamage pango shared-mime-info at-spi2-atk wayland libxkbcommon
	json-glib librsvg wayland-protocols desktop-file-utils mesa gtk-update-icon-cache
	adwaita-icon-theme cantarell-fonts

	lib32-atk lib32-cairo lib32-libxcursor lib32-libxinerama lib32-libxrandr lib32-libxi
	lib32-libepoxy lib32-gdk-pixbuf2 lib32-fribidi lib32-libxcomposite lib32-libxdamage 
	lib32-pango lib32-at-spi2-atk lib32-wayland lib32-libxkbcommon lib32-json-glib
	lib32-librsvg lib32-mesa lib32-libcups lib32-krb5 lib32-e2fsprogs
)
install=gtk3.install
source=(
	# Patch files.
	series
	appearance__buttons-menus-icons.patch
	appearance__disable-backdrop.patch
	appearance__file-chooser.patch
	appearance__message-dialogs.patch
	appearance__print-dialog.patch
	appearance__smaller-statusbar.patch
	csd__clean-headerbar.patch
	csd__disabled-by-default.patch
	csd__server-side-shadow.patch
	file-chooser__places-sidebar.patch
	file-chooser__typeahead.patch
	fixes__atk-bridge-errors.patch
	fixes__labels-wrapping.patch
	fixes__too-large-menu-covers-bar.disabled-patch
	other__default-settings.patch
	other__hide-insert-emoji.patch
	other__mnemonics-delay.patch
	popovers__color-chooser.patch
	popovers__file-chooser-list.patch
	popovers__places-sidebar.patch

	# Theme CSS stylesheet.
	smaller-adwaita.css

	# GTK source code.
	"https://download.gnome.org/sources/gtk+/${pkgver%.*}/gtk+-$_gtkver.tar.xz"

	# Arch Linux package files.
	"settings.ini::https://git.archlinux.org/svntogit/packages.git/plain/trunk/settings.ini?h=packages/gtk3&id=$__arch_pkg_commit"
	"gtk-query-immodules-3.0.hook::https://git.archlinux.org/svntogit/packages.git/plain/trunk/gtk-query-immodules-3.0.hook?h=packages/gtk3&id=$__arch_pkg_commit"

	README.md
)
sha256sums=('4935ec23cbd0150bd479fc457861d3a665354509c3ff933997827c7141c8657c'
            '6de32e1bee6bf4307aaec072fc8431b044e73299720a490298b8c1b7c502e039'
            'c8f6be1df687bf2ccaaeff63fffdc13e2c1d41f89ad1dfa391120c509dba7f33'
            '760bd3d65b3c5c0be19311d3b9d2be1f33c3bec198bc470de5afe23f5d488b8f'
            '00927690718c65f6b3c025e2e919028f41cd522c573964dd7fdc31b3022b983f'
            'db82bc4647eda7cc102590d5cfffd8524cf126a704358096e0e66f5c068fe46f'
            'f29097aaa6fb8b99ce1a4659856dbc290d299befb1b09fd6158cbb3f539d890c'
            '110d2a2d8fc8f3f4ad1b40abd319f18fbb571b1f1bc121de1a8e0037eb3d9df8'
            'caa4da5e786a38e788617d6c9a844dfc604038d2a5d57033273859cad46d14cd'
            'cf26ab623fec6fc4f24628bdbe4b81ba5f56e8e0c61de78474d5c2411901931a'
            '57b7b7725b9afe24dc29c6315e3162f297632525b32e329e18b32aba1112eed2'
            'c6fd146e7ab332dd9a394b666b19e6ba7d6ac0932f33fb396f66630134257309'
            '54fb3a39475644abaded2ac2db32c72ce8c36ee7b98ced0ee52a3f89dcac8d83'
            '7157b665e2ae724bb6abe8fc382d7178dc4d8d00f29bc63ed2942307ff41914b'
            '2b10b436ebcf8c124fac6e7867f0bf0573ecfb70130893fea37724c5f6719caf'
            '1d1e09a82e138391ae58d67e17110c77ff9451bbbf3ce6250d24a4917a3e14fa'
            '974374f2799aaa48b9ded985c47d2dda45d2fcdcd63f1749e74b243279467d49'
            '9761a289cf93558ec67bb498b765ccb757027b10071da938ff14fca695a0103d'
            'bf0e188ba6cfb24b506e4eab7e62a020348cce307d4eecde571227a058c441ad'
            '17aa98262b96817396c74c303c83eee2a0c9c94b10e31d8de48a44cb17b08dc1'
            'af2d2d4a0d876f9abc350a1cdb09ffc016a8894ee3c46030c3d90c6e99b27c5a'
            'ba93f62e249f2713dbfe6c82de1be4ac655264d6407ed3dc5e05323027520f31'
            'cc9d4367c55b724832f6b09ab85481738ea456871f0381768a6a99335a98378a'
            '01fc1d81dc82c4a052ac6e25bf9a04e7647267cc3017bc91f9ce3e63e5eb9202'
            'a0319b6795410f06d38de1e8695a9bf9636ff2169f40701671580e60a108e229'
            '1d2e3c41c7de03a31d717b09e053c88cbaca2ae74eefd982549c49de81c21ada')

prepare()
{
	cd gtk+-$_gtkver
	QUILT_PATCHES=.. quilt push -av

	rm -f "$srcdir"/gtk+-"$_gtkver"/gtk/theme/Adwaita/gtk-contained{,-dark}.css
	cat "$srcdir/smaller-adwaita.css" | tee -a "$srcdir"/gtk+-"$_gtkver"/gtk/theme/Adwaita/gtk-contained{,-dark}.css > /dev/null
}

build()
{
	CFLAGS+=" -DG_ENABLE_DEBUG -DG_DISABLE_CAST_CHECKS"

	# 64-bit
	arch-meson gtk+-$_gtkver build \
		-D broadway_backend=true \
		-D colord=no \
		-D demos=true \
		-D examples=false \
		-D tests=false \
		-D installed_tests=false
	ninja -C build

	# 32-bit
	export PKG_CONFIG_LIBDIR="/usr/lib32/pkgconfig"
	export PKG_CONFIG_PATH="/usr/share/pkgconfig"

	CFLAGS+=" -m32"
	CXXFLAGS+=" -m32"
	LDFLAGS+=" -m32"

	linux32 arch-meson gtk+-$_gtkver build32 \
		-D broadway_backend=true \
		-D colord=no \
		-D demos=false \
		-D examples=false \
		-D introspection=false \
		-D tests=false \
		-D installed_tests=false \
		-D libdir=/usr/lib32
	linux32 ninja -C build32
}

package_gtk3-classic()
{
	depends=(
		atk cairo libxcursor libxinerama libxrandr libxi libepoxy gdk-pixbuf2 fribidi
		libxcomposite libxdamage pango shared-mime-info at-spi2-atk wayland libxkbcommon
		json-glib librsvg wayland-protocols desktop-file-utils mesa gtk-update-icon-cache
	)
	optdepends=(
		'libcups: printers in printing dialog'
		'dconf: default GSettings backend'
		'libcanberra: sounds events'
		'adwaita-icon-theme: default icon theme'
		'cantarell-fonts: default font'
	)

	DESTDIR="$pkgdir" meson install -C build

	install -Dt "$pkgdir/usr/share/gtk-3.0" -m644 settings.ini
	install -Dt "$pkgdir/usr/share/libalpm/hooks" -m644 gtk-query-immodules-3.0.hook

	rm "$pkgdir/usr/bin/gtk-update-icon-cache"

	install -Dm644 "$srcdir"/README.md "$pkgdir/usr/share/gtk-3.0/README.md"
	sed -i 's/mushrooms/classic/g' "$pkgdir/usr/share/gtk-3.0/README.md"
}

package_lib32-gtk3-classic()
{
	pkgdesc="GTK3 patched for classic desktops like XFCE or MATE. (32-bit)"
	depends=(
		lib32-atk lib32-cairo lib32-libxcursor lib32-libxinerama lib32-libxrandr lib32-libxi
		lib32-libepoxy lib32-gdk-pixbuf2 lib32-fribidi lib32-libxcomposite lib32-libxdamage 
		lib32-pango lib32-at-spi2-atk lib32-wayland lib32-libxkbcommon lib32-json-glib
		lib32-librsvg lib32-mesa lib32-libcups lib32-krb5 lib32-e2fsprogs
		"gtk3-classic>=$pkgver"
	)
	conflicts=("lib32-gtk3")
	provides=("lib32-gtk3=$pkgver")

	DESTDIR="$pkgdir" linux32 meson install -C build32

	rm -fr "$pkgdir"/etc
	rm -fr "$pkgdir"/usr/{bin,share,include}
}
