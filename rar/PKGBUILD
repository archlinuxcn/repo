# Maintainer Musikolo <musikolo {at} hotmail [dot] com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=5.6.1
pkgrel=2
pkgdesc="A command-line port of the rar compression utility"
url="http://www.rarlab.com"
arch=('i686' 'x86_64')
license=('custom')
depends=('gcc-libs')
backup=('etc/rarfiles.lst')
conflicts=('rar-beta' 'unrar')
provides=('unrar')
source=('rar.1')
source_i686+=("http://www.rarlab.com/rar/rarlinux-${pkgver}.tar.gz")
source_x86_64+=("http://www.rarlab.com/rar/rarlinux-x64-${pkgver}.tar.gz")
sha512sums=('d78fb6d77a3e2c088cdf0586b6346c0025fb18be04f79cc6c081e49a05ba48347d55e1ff62c753c13377e2985978cf0bfdb6c60496a1e298974c70687194b3b6')
sha512sums_i686=('b566d8d05068557987b69aa3b9610597c7226f7ff96ab935be33f3437b78d02dd539366b3a8499dc4c1d953a640a8a27f21b3f979969b71c6e3bde51a1118b00')
sha512sums_x86_64=('b873397cc44ffe722248638f0315a445e7f8b39ce310d45b79e27d8c2662bf7bc8a095a3e7c4a8fa92e24551328530955f6f18a8553a1612ea00bec8ccaf2e37')


package() {
    cd "${srcdir}/${pkgname}"
    install -Dm755 rar          "${pkgdir}/usr/bin/rar"
    install -Dm755 default.sfx  "${pkgdir}/usr/lib/default.sfx"
    install -Dm644 license.txt  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 ../rar.1     "${pkgdir}/usr/share/man/man1/rar.1"
    install -Dm644 rarfiles.lst "${pkgdir}/etc/rarfiles.lst"

    # rar is a superset of unrar - needed for some UI tools to support RAR format.
    ln -s "/usr/bin/rar" "${pkgdir}/usr/bin/unrar"
}
