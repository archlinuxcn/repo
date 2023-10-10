# Maintainer Musikolo <musikolo {at} hotmail [dot] com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=6.24.0
__pkgver=624
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
sha512sums_i686=('967ca151e2927f427738c49eedd0bd4a0c1e56bd43d417bfbfb1e940d553c30a4860b279b90a47151838312f8e788f0fee13c424ee3b31ab2574a077de957234')
sha512sums_x86_64=('04b935d918d7636bf7cececee2c306f6c586ac363932a30529dcf0e5e199823ca976269acf26456f9a91830dfe909d67ff0a13e55a68096e59875e46e0e0b0de')


package() {
    cd "${srcdir}/${pkgname}"
    install -Dm755 rar          "${pkgdir}/usr/bin/rar"
    install -Dm755 unrar        "${pkgdir}/usr/bin/unrar"
    install -Dm755 default.sfx  "${pkgdir}/usr/lib/default.sfx"
    install -Dm644 license.txt  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 ../rar.1     "${pkgdir}/usr/share/man/man1/rar.1"
    install -Dm644 rarfiles.lst "${pkgdir}/etc/rarfiles.lst"
}
