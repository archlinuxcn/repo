# Contributor: Tilman Blumenbach <tilman [AT] ax86 [DOT] net>

pkgname='terminus-font-ttf'
pkgver=4.39
pkgrel=2
pkgdesc="Monospaced bitmap font designed for long work with computers (TTF version)"
arch=('any')
url="http://files.ax86.net/terminus-ttf"
license=('custom:OFL')
depends=('fontconfig' 'xorg-font-utils')
install='terminus-font-ttf.install'
source=("http://files.ax86.net/terminus-ttf/files/${pkgver}/terminus-ttf-${pkgver}.zip")

package()
{
    cd "${srcdir}/terminus-ttf-${pkgver}"

    for i in *.ttf; do
        local destname="$(echo "$i" | sed -E 's|-[[:digit:].]+\.ttf$|.ttf|')"
        install -Dm 644 "$i" "${pkgdir}/usr/share/fonts/TTF/${destname}"
    done

    install -Dm 644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}

md5sums=('6925c62e7b33de8d2fe252799140d4e4')
