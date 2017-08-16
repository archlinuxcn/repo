# Maintainer Musikolo <musikolo {at} hotmail [dot] com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=5.5.0
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
sha512sums=('d78fb6d77a3e2c088cdf0586b6346c0025fb18be04f79cc6c081e49a05ba48347d55e1ff62c753c13377e2985978cf0bfdb6c60496a1e298974c70687194b3b6')
sha512sums_i686=('c437d0be55ea90ae1dd9d657517d17d9edbba07cd77325785d8d503883847edeece2cc3993d3beec3a5b36b6830383b7026fbfc53b18f490288395994bc532cb')
sha512sums_x86_64=('1ca8cf7fbe526b43bdc9aeeccb6a0d86efd3bbaeee554e807d58ab62857294abc89662bb42b17b2cfe7e6739876c6345455cd027abbc4cb84312c58314278a66')


package() {
    cd "${srcdir}/${pkgname}"
    install -Dm755 rar          "${pkgdir}/usr/bin/rar"
    install -Dm755 default.sfx  "${pkgdir}/usr/lib/default.sfx"
    install -Dm644 license.txt  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 ../rar.1     "${pkgdir}/usr/share/man/man1/rar.1"
    install -Dm644 rarfiles.lst "${pkgdir}/etc/rarfiles.lst"
}
