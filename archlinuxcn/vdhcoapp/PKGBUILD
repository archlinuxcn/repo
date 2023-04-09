# Maintainer: Damien Guihal <dguihal@gmail.com>
# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>

pkgname=vdhcoapp
pkgver=1.6.3
pkgrel=2
pkgdesc="Companion application for Video DownloadHelper browser add-on"
arch=('x86_64')
url="https://github.com/mi-g/vdhcoapp"
license=('GPL2')
depends=('ffmpeg')
makedepends=('gulp' 'nodejs' 'npm')
options=(!strip)
source=($pkgname-$pkgver.tar.gz::https://github.com/mi-g/vdhcoapp/archive/v${pkgver}.tar.gz
        vdhcoapp.patch
        vdhcoapp-build.patch
        vdhcoapp-install.hook
        vdhcoapp-remove.hook)
sha256sums=('0b15f1f623193cf6c09fb830e3f5db0a71a63586fa1cb5cb73bf1a819d7c2f55'
            'ab240d9d9fea27792d008eaffe14de5f798ced0938cc79351ed108185baf93a3'
            '9866e599048cc63f4a09182f8539fe1ba39315c5e33a6e2df41c88efa895064d'
            '9f8cbe84b2543738390b70d770551259c6db2b67235b7792e9094908cecbc955'
            '448ee36b350b6bcd304d33cf7638c13bda88d5086f2256e823d73ccc22e52ce0')

prepare() {
    cd ${pkgname}-${pkgver}

    patch -Np2 -i "${srcdir}/vdhcoapp.patch"
    patch -N -i "${srcdir}/vdhcoapp-build.patch"
}

build() {
    cd "${pkgname}-${pkgver}"

    npm install

    gulp
}

package() {
    cd "${pkgname}-${pkgver}"

    install -Dm755 bin/net.downloadhelper.coapp-* "${pkgdir}/usr/bin/vdhcoapp"
    install -Dm644 config.json "${pkgdir}/usr/share/vdhcoapp/config.json"

    install -dm755 "${pkgdir}/usr/lib/mozilla/native-messaging-hosts/"
    install -dm755 "${pkgdir}/etc/opt/chrome/native-messaging-hosts/"
    install -dm755 "${pkgdir}/etc/chromium/native-messaging-hosts/"

    install -Dm644 "${srcdir}/vdhcoapp-install.hook" "${pkgdir}/usr/share/libalpm/hooks/vdhcoapp-install.hook"
    install -Dm644 "${srcdir}/vdhcoapp-remove.hook" "${pkgdir}/usr/share/libalpm/hooks/vdhcoapp-remove.hook"
}
