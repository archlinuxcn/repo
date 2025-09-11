# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Ronald van Haren <ronald.archlinux.org>
pkgname=bdf-unifont
pkgver=17.0.01
pkgrel=1
pkgdesc="GNU Unifont Glyphs"
arch=(any)
license=('custom' 'GPL2')
url="https://ftp.gnu.org/gnu/unifont"
source=("${url}/unifont-${pkgver}/unifont-${pkgver}.bdf.gz"{,.sig} "LICENSE")
validpgpkeys=('95D2E9AB8740D8046387FD151A09227B1F435A33') # Paul Hardy <unifoundry@unifoundry.com>
sha512sums=('408d38aea85dc4e1b2a130baf53c7556cdb751160a4beea871ba155fefe61c74892d2662bfce807f43ee51d5a53a6b7ec2dbb35dece607d67814d4829201d7be'
            'SKIP'
            '064e7c0afe836d48610fcdd5d2d080c2583be0f2b70e565440d743072f41a242aec29a500df7a2bd39f423089c291250eabe0cefae5d000aecd7f27a052ee242')

package() {
  gzip -d --force "$srcdir"/unifont-${pkgver}.bdf.gz
  install -Dm644 "${srcdir}/unifont-${pkgver}.bdf" \
    "${pkgdir}/usr/share/fonts/misc/unifont.bdf"
  install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
