#
# PKGBUILD file for package clapper
#
# Copyright (C) 2020-24 sp1rit
# Copyright (C) 2020  Rafostar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Maintainer: sp1rit <sp1ritCS@protonmail.com>

_basename=clapper
_libver=0.0
pkgname="${_basename}"
pkgver=0.6.1
pkgrel=1
pkgdesc="A modern media player powered by GStreamer and built for the GNOME desktop environment."
arch=(any)
url="https://github.com/Rafostar/clapper"
license=("GPL-3.0-or-later and LGPL-2.1-or-later")
depends=(
	"gtk4>=4.10.0"
	"glib2>=2.76.0" # glib-2.0, gmodule-2.0, gio-2.0
	"gstreamer>=1.20.0" # gstreamer-1.0, gstreamer-base-1.0
	"gst-plugins-base>=1.20.0"
	"gst-plugins-good>=1.20.0"
	"gst-plugins-bad>=1.20.0"
	"libadwaita>=1.4.0"
	"libsoup3"
	"libmicrodns"
)
makedepends=(
	"meson>=0.64"
	"glib2-devel>=2.76.0"
	"gobject-introspection" # /usr/sbin/g-ir-scanner
	"vala"
)
optdepends=(
	"gst-libav>=1.20.0: Popular video decoders"
	"gstreamer-vaapi>=1.20.0: Intel/AMD video acceleration"
	"gst-plugins-ugly>=1.20.0: CD/DVD playback"
	"gst-plugin-va>=1.20.0: Intel/AMD video acceleration (experimental)"
	"gtuber>=r242: Play videos from various services"
)
source=("${_basename}-${pkgver}::https://github.com/Rafostar/${_basename}/archive/${pkgver}.tar.gz")
provides=("${_basename}" "lib${_basename}-${_libver}" "lib${_basename}-gtk-${_libver}")
conflicts=("${_basename}")
md5sums=("a550a4f20e3731ae778a6ab34f790e82")

prepare() {
	cd "${srcdir}/${_basename}-${pkgver}"
	arch-meson . _build
}

build() {
	cd "${srcdir}/${_basename}-${pkgver}"
	ninja -C _build
}

package() {
	cd "${srcdir}/${_basename}-${pkgver}"
	DESTDIR="$pkgdir" meson install -C _build/
}
