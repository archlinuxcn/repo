# Maintainer: FadeMind <fademind@gmail.com>
# Maintainer: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=5.4.0
pkgrel=1
pkgdesc="A command-line port of the rar compression utility"
url="http://www.rarlab.com"
arch=('i686' 'x86_64')
license=('custom')
depends=('gcc-libs')
backup=('etc/rarfiles.lst')
conflicts=('rar-beta')
source=('rar.1')
source_i686+=("http://www.rarlab.com/rar/rarlinux-${pkgver}.tar.gz")
source_x86_64+=("http://www.rarlab.com/rar/rarlinux-x64-${pkgver}.tar.gz")
md5sums=('4cffd2771bb4a51e4a68500d799550d8')
md5sums_i686=('cd1fede60f8dde36f62283f371e7cc6b')
md5sums_x86_64=('f7181c0aed3b7be402b95185bd61e646')


package() {
    cd "${srcdir}/${pkgname}"
    install -Dm755 rar          "${pkgdir}/usr/bin/rar"
    install -Dm755 rar_static   "${pkgdir}/usr/bin/rar_static"
    install -Dm755 default.sfx  "${pkgdir}/usr/lib/default.sfx"
    install -Dm644 license.txt  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 ../rar.1     "${pkgdir}/usr/share/man/man1/rar.1"
    install -Dm644 rarfiles.lst "${pkgdir}/etc/rarfiles.lst"
}
