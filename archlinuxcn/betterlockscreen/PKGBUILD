# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: AUTplayed <fips.hem@gmail.com>
# Contributor: pavanjadhaw <pavanjadhaw96@gmail.com>

pkgname=betterlockscreen
pkgver=4.0.3
pkgrel=1
pkgdesc="A simple, minimal lockscreen"
arch=('any')
url="https://github.com/pavanjadhaw/${pkgname}"
license=('MIT')
depends=('bc' 'feh' 'i3lock-color' 'imagemagick' 'xorg-xdpyinfo' 'xorg-xrandr')
conflicts=('betterlockscreen-git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "betterlockscreen@.service")
sha256sums=('d96fd64f1c94c91fec5d26b9665ba68f7f130c8a8612978ad9edbfa859710671'
            '3db1f3775abd6c5333631e3f729625285da0b33ab807ad6888db3923f37ab885')

package() {
    cd "${pkgname}-${pkgver}"/
    install -Dm 755 "${pkgname}" -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/${pkgname}@.service -t "${pkgdir}"/usr/lib/systemd/system/
    install -Dm 644 examples/"${pkgname}rc" -t "${pkgdir}"/usr/share/doc/betterlockscreen/examples/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
}
