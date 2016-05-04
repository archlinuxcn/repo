# Contributor: Tilman Blumenbach <tilman [AT] ax86 [DOT] net>

pkgname='terminus-font-ttf'
pkgver=4.40
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

md5sums=('c5dabc9853ae9fa15e484501f9832703')
sha384sums=('dce2835135e7e2028fa78360cf2a1108f3c07defb435c364f6765966ecc825c6e8f5c4b512616a0f1222bcb9ce0fad9f')
