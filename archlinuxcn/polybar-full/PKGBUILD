# Maintainer: Dct Mei <dctxmei@gmail.com>
# Contributor: Michael Carlberg <c@rlberg.se>

pkgname=polybar-full
_pkgname=polybar
pkgver=3.3.1
pkgrel=2
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
sha512sums=('701598d0d3435d7e1cb0437dbd43531dfda933093877a517c2cde93584ea47fce81c06e6301a2637656472ba2cda42ad0ea0c15df846c6699f1496a075249382')

prepare() {
    mkdir -p "$_pkgname/build"
}

build() {
    cd "$_pkgname/build" || exit 1
    cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_CXX_FLAGS="-Wno-deprecated-copy" ..
    cmake --build .
}

package() {
    cmake --build "$_pkgname/build" --target install -- DESTDIR="$pkgdir"
    install -Dm644 "$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}
