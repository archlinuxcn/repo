# Maintainer: Maarten Baert <maarten-baert@hotmail.com>

pkgname=simplescreenrecorder-git
pkgver=0.4.2.r11.g7f26bc7
pkgrel=1
pkgdesc="A simple but powerful recording tool for X11, OpenGL and V4L2. (Git version)"
arch=("x86_64")
url="https://www.maartenbaert.be/simplescreenrecorder/"
license=("GPL3")
depends=("qt5-base" "qt5-x11extras"
    "ffmpeg" "alsa-lib" "libpulse" "jack" "libgl" "glu" "v4l-utils"
    "libx11" "libxext" "libxfixes" "libxi" "libxinerama"
    "desktop-file-utils" "gtk-update-icon-cache")
optdepends=("lib32-simplescreenrecorder-git: OpenGL recording of 32-bit applications")
makedepends=("git" "cmake" "qt5-tools")
source=("git+https://github.com/MaartenBaert/ssr.git")
md5sums=("SKIP")
conflicts=("simplescreenrecorder")
provides=("simplescreenrecorder")

install=simplescreenrecorder-git.install

pkgver() {
	cd ssr
	# Use the tag of the last commit
	git describe --long | sed -E 's/([^-]*-g)/r\1/;s/-/./g'
}
prepare() {
	cd ssr
	mkdir -p build
}
build() {
	cd ssr/build
	cmake -DCMAKE_INSTALL_PREFIX="/usr" -DCMAKE_INSTALL_LIBDIR="lib" -DCMAKE_BUILD_TYPE=Release -DWITH_QT5=TRUE ..
	make
}
package() {
	cd ssr/build
	make DESTDIR="$pkgdir" install
}
