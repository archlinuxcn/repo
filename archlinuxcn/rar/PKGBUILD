# Maintainer Musikolo <musikolo {at} hotmail [dot] com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=6.20.0
__pkgver=620
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
source_i686+=("https://www.rarlab.com/rar/rarlinux-x32-${__pkgver}.tar.gz")
source_x86_64+=("https://www.rarlab.com/rar/rarlinux-x64-${__pkgver}.tar.gz")
sha512sums=('d78fb6d77a3e2c088cdf0586b6346c0025fb18be04f79cc6c081e49a05ba48347d55e1ff62c753c13377e2985978cf0bfdb6c60496a1e298974c70687194b3b6')
sha512sums_i686=('e84571752e92f940249e6db95fcfc9f686351546935d07388b85c74da8df862ecf4d935c68eee0f99c62430c37d855f63708ab874ab87ed7e68a77e81e14b30e')
sha512sums_x86_64=('f9cd780c77241bbe75711d82b7180178c2f647a062b31401e65dd5be7a98ab4ed48577b9b471e8636cb32c62b3c4cfab798e9687ba191819e1b674747ce59574')


package() {
    cd "${srcdir}/${pkgname}"
    install -Dm755 rar          "${pkgdir}/usr/bin/rar"
    install -Dm755 unrar        "${pkgdir}/usr/bin/unrar"
    install -Dm755 default.sfx  "${pkgdir}/usr/lib/default.sfx"
    install -Dm644 license.txt  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 ../rar.1     "${pkgdir}/usr/share/man/man1/rar.1"
    install -Dm644 rarfiles.lst "${pkgdir}/etc/rarfiles.lst"
}
