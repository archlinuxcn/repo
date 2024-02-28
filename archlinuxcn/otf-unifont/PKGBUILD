# Maintainer: Martin C. Doege <mdoege at compuserve dot com>
# Maintainer: txtsd <aur.archlinux@ihavea.quest>
# Contributor: nl6720 <nl6720@archlinux.org>
# Contributor: David McInnis <dave@dave3.xyz>
# Contributor: megadriver <megadriver at gmx dot com>

pkgname=otf-unifont
pkgver=15.1.05
pkgrel=1
pkgdesc="OpenType version of the GNU Unifont"
url="https://unifoundry.com/unifont.html"
arch=('any')
license=('OFL-1.1 OR GPL-2.0-or-later WITH Font-exception-2.0')
source=("https://unifoundry.com/pub/unifont/unifont-${pkgver}/unifont-${pkgver}.tar.gz"{,.sig})
sha256sums=('d275f55f4358750e0f86305b92e87b88eb330aa46c15f553d2edf047fb1c23fa'
            'SKIP')
validpgpkeys=('95D2E9AB8740D8046387FD151A09227B1F435A33') # Paul Hardy

package() {
	cd "${srcdir}"
	install -d "${pkgdir}/usr/share/fonts/Unifont/"
	install -m644 "unifont-${pkgver}/font/precompiled/unifont-${pkgver}.otf" "${pkgdir}/usr/share/fonts/Unifont/Unifont.otf"
	install -m644 "unifont-${pkgver}/font/precompiled/unifont_jp-${pkgver}.otf" "${pkgdir}/usr/share/fonts/Unifont/Unifont_jp.otf"
	install -m644 "unifont-${pkgver}/font/precompiled/unifont_upper-${pkgver}.otf" "${pkgdir}/usr/share/fonts/Unifont/Unifont_Upper.otf"
	install -m644 "unifont-${pkgver}/font/precompiled/unifont_csur-${pkgver}.otf" "${pkgdir}/usr/share/fonts/Unifont/Unifont_CSUR.otf"
}
