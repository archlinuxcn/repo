# Maintainer: Dct Mei <dctxmei@gmail.com>
# Contributor: Michael Carlberg <c@rlberg.se>

pkgname=polybar-full
_pkgname=polybar
pkgver=3.4.0
pkgrel=1
pkgdesc="A fast and easy-to-use status bar - Full module support"
arch=(x86_64)
url="https://github.com/polybar/polybar"
license=('MIT')
depends=('alsa-lib' 'cairo' 'curl' 'i3-wm' 'jsoncpp' 'libmpdclient' 'libnl' 'pulseaudio' 'wireless_tools' 'xcb-util-cursor' 'xcb-util-image' 'xcb-util-wm' 'xcb-util-xrm')
makedepends=('cmake' 'git' 'python' 'python2' 'pkg-config')
optdepends=("ttf-unifont: Font used in example config"
            "siji-git: Font used in example config"
            "xorg-fonts-misc: Font used in example config")
provides=('polybar')
conflicts=('polybar' 'polybar-git')
install="${_pkgname}.install"
source=("$url/releases/download/$pkgver/polybar-$pkgver.tar")
sha512sums=('e8e0b39c45d7496429f063bf104b8b84596de957decdaf717fc658a5fb717cd25a2588e4296ed8f33a6fc0371ff9094f4f072adb660f72cf1f3966abb74ee9e9')

prepare() {
    mkdir -p "$_pkgname/build"
}

build() {
    cd "$_pkgname/build" || exit 1
    cmake -DCMAKE_INSTALL_PREFIX=/usr ..
    cmake --build .
}

package() {
    cmake --build "$_pkgname/build" --target install -- DESTDIR="$pkgdir"
    install -Dm644 "$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}
