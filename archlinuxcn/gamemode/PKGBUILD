# Maintainer: Ysblokje <ysblokje at gmail dot com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=('gamemode' 'lib32-gamemode')
pkgbase='gamemode'
pkgver=1.6
pkgrel=8
pkgdesc="A daemon/lib combo that allows games to request a set of optimisations be temporarily applied to the host OS"
arch=('x86_64')
url="https://github.com/FeralInteractive/gamemode"
license=('BSD')
makedepends=('meson' 'lib32-systemd' 'lib32-dbus')
depends=('libinih')
checkdepends=('appstream')
source=("$url/releases/download/$pkgver/$pkgname-$pkgver.tar.xz")
sha256sums=('ede17eb042c1c87f7b35bfe96a00560afaea086f685d25bb3964d794b0af9c80')

build() {
    meson "${pkgbase}-${pkgver}" build64 \
        --prefix /usr \
        --libexecdir lib/gamemode \
        -Dwith-pam-group=gamemode \
        -Dwith-systemd-user-unit-dir=/usr/lib/systemd/user
    meson compile -C build64

    export CFLAGS+=" -m32"
    export CXXFLAGS+=" -m32"
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    meson "${pkgbase}-${pkgver}" build32 \
        --prefix /usr \
        -Dwith-sd-bus-provider=no-daemon \
        -Dwith-examples=false \
        -Dwith-util=false \
        --libdir lib32
    meson compile -C build32
}

check() {
    meson test -C build64
    meson test -C build32
}

package_gamemode() {
    depends=('libinih' 'dbus')
    optdepends=('systemd' 'polkit')
    install="${pkgname}.install"

    DESTDIR="${pkgdir}" meson install -C build64

    install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/LICENSE.txt" -t \
        "${pkgdir}/usr/share/licenses/${pkgname}/"
    install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/example/gamemode.ini" -t \
        "${pkgdir}/usr/share/doc/${pkgname}/example" 
}

package_lib32-gamemode() {
    depends=('gamemode' 'lib32-dbus')

    DESTDIR="${pkgdir}" meson install -C build32

    rm -rf "${pkgdir}/usr/include"
    install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/LICENSE.txt" -t \
        "${pkgdir}/usr/share/licenses/${pkgname}/"
}

# vim: set ts=4 sw=4 tw=0 et :
