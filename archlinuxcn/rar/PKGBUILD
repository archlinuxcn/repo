# Maintainer Musikolo <musikolo {at} hotmail [dot] com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=6.0.2
pkgrel=1
pkgdesc="A command-line port of the rar compression utility"
url="https://www.rarlab.com"
arch=('i686' 'x86_64')
license=('custom')
depends=('gcc-libs')
backup=('etc/rarfiles.lst')
conflicts=('rar-beta' 'unrar')
provides=('unrar')
source=('rar.1')
source_i686+=("https://www.rarlab.com/rar/rarlinux-${pkgver}.tar.gz")
source_x86_64+=("https://www.rarlab.com/rar/rarlinux-x64-${pkgver}.tar.gz")
sha512sums=('d78fb6d77a3e2c088cdf0586b6346c0025fb18be04f79cc6c081e49a05ba48347d55e1ff62c753c13377e2985978cf0bfdb6c60496a1e298974c70687194b3b6')
sha512sums_i686=('6b6ef629dd0e681702fb0835cf6fe9962dc2ce774291f800893308a93a0a498099775e7d897d69375f68107b0ce0862bb2a6a169b8fbda534091678e9be3f09c')
sha512sums_x86_64=('909eb3b05c56327ccec101652d1d68ca5eb97ba3a7223954724fbccf4960b07ffa0ff5fe5405c53a248342a3ae171325e7bbf7fadeaf63c1c45bf00853e0a940')


package() {
    cd "${srcdir}/${pkgname}"
    install -Dm755 rar          "${pkgdir}/usr/bin/rar"
    install -Dm755 unrar        "${pkgdir}/usr/bin/unrar"
    install -Dm755 default.sfx  "${pkgdir}/usr/lib/default.sfx"
    install -Dm644 license.txt  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 ../rar.1     "${pkgdir}/usr/share/man/man1/rar.1"
    install -Dm644 rarfiles.lst "${pkgdir}/etc/rarfiles.lst"
}
