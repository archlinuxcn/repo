# Maintainer Musikolo <musikolo {at} hotmail [dot] com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=6.12.0
__pkgver=612
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
sha512sums_i686=('8f67a365145d6fe7c9db1458a67f29a6b878f1969842f0cb43f639af1f8c304b0f4174f83b070f7d821316fdd9dcd2e1788bca2d6af5ef60fdb951924ebc71a4')
sha512sums_x86_64=('bccb64b077fa044a920f02a826bafd4a07c446f2ff2ce88b7c8f27d49c6ac48108711880ad43aac89c034f582979cad8b332d675ea483eca9f76bcd892949423')


package() {
    cd "${srcdir}/${pkgname}"
    install -Dm755 rar          "${pkgdir}/usr/bin/rar"
    install -Dm755 unrar        "${pkgdir}/usr/bin/unrar"
    install -Dm755 default.sfx  "${pkgdir}/usr/lib/default.sfx"
    install -Dm644 license.txt  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 ../rar.1     "${pkgdir}/usr/share/man/man1/rar.1"
    install -Dm644 rarfiles.lst "${pkgdir}/etc/rarfiles.lst"
}
