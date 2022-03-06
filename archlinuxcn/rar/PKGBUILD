# Maintainer Musikolo <musikolo {at} hotmail [dot] com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=6.11.0
__pkgver=611
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
sha512sums_i686=('5bfbfc3cbf0b67790dfb3c17ebf49d557b2344074317143200c4fbcea17b793106f9f2345f15fae0db3a9d6893f7408218251ef6fd33c6444931c4557e1b57b5')
sha512sums_x86_64=('135091821bd66828872b719481c1b0b186ab5e9ca6c0e0b6010502845911a593586f323e0fb86391b44b49bfdd96ae9d1902f4674c5b6c450050d6535b7231cb')


package() {
    cd "${srcdir}/${pkgname}"
    install -Dm755 rar          "${pkgdir}/usr/bin/rar"
    install -Dm755 unrar        "${pkgdir}/usr/bin/unrar"
    install -Dm755 default.sfx  "${pkgdir}/usr/lib/default.sfx"
    install -Dm644 license.txt  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 ../rar.1     "${pkgdir}/usr/share/man/man1/rar.1"
    install -Dm644 rarfiles.lst "${pkgdir}/etc/rarfiles.lst"
}
