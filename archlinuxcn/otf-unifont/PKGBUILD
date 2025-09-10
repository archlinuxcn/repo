# Maintainer: Martin C. Doege <mdoege at compuserve dot com>
# Maintainer: txtsd <aur.archlinux@ihavea.quest>
# Contributor: nl6720 <nl6720@archlinux.org>
# Contributor: David McInnis <dave@dave3.xyz>
# Contributor: megadriver <megadriver at gmx dot com>

pkgname=otf-unifont
_pkgname="${pkgname#otf-}"
pkgver=17.0.01
pkgrel=1
pkgdesc='OpenType version of the GNU Unifont'
url='https://unifoundry.com/unifont.html'
arch=(any)
license=('OFL-1.1 OR GPL-2.0-or-later WITH Font-exception-2.0')
provides=(emoji-font)
options=(!debug)
source=("https://unifoundry.com/pub/unifont/unifont-${pkgver}/unifont-${pkgver}.tar.gz"{,.sig})
sha256sums=('234af86e7a0e851f020900db5ad0afc32691c248db362df9b2914cf50c42d940'
            'SKIP')
validpgpkeys=('95D2E9AB8740D8046387FD151A09227B1F435A33') # Paul Hardy

package() {
  cd "${_pkgname}-${pkgver}"
  install -Dm644 OFL-1.1.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
  install -Dm644 "font/precompiled/unifont-${pkgver}.otf" "${pkgdir}/usr/share/fonts/Unifont/Unifont.otf"
  install -Dm644 "font/precompiled/unifont_jp-${pkgver}.otf" "${pkgdir}/usr/share/fonts/Unifont/Unifont_jp.otf"
  install -Dm644 "font/precompiled/unifont_upper-${pkgver}.otf" "${pkgdir}/usr/share/fonts/Unifont/Unifont_Upper.otf"
  install -Dm644 "font/precompiled/unifont_csur-${pkgver}.otf" "${pkgdir}/usr/share/fonts/Unifont/Unifont_CSUR.otf"
}
