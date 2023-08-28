# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: AUTplayed <fips.hem@gmail.com>
# Contributor: pavanjadhaw <pavanjadhaw96@gmail.com>

pkgname=betterlockscreen
pkgver=4.1.0
pkgrel=1
pkgdesc="A simple, minimal lockscreen"
arch=('any')
url="https://github.com/betterlockscreen/${pkgname}"
license=('MIT')
depends=('bc' 'feh' 'i3lock-color' 'imagemagick' 'xorg-xdpyinfo' 'xorg-xrandr')
conflicts=('betterlockscreen-git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "betterlockscreen@.service")
sha256sums=('2618ca60e028681be9fc476c9501e95a5bcc2d302c7ee770f8433fa96bad0d24'
            '342c92fcbc685349d843811ea336983307205f680f43362bef7dc3cfaed31d4d')

package() {
    cd "${pkgname}-${pkgver}"/
    install -Dm 755 "${pkgname}" -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/${pkgname}@.service -t "${pkgdir}"/usr/lib/systemd/system/
    install -Dm 644 examples/"${pkgname}rc" -t "${pkgdir}"/usr/share/doc/betterlockscreen/examples/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
}
