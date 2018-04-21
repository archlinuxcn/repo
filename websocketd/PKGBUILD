# Maintainer: wenLiangcan <boxeed at gmail dot com>

pkgname=websocketd
pkgver=0.2.12
pkgrel=1
pkgdesc="Like inetd, but for WebSockets. Turn any application that uses STDIO/STDOUT into a WebSocket server."
arch=('x86_64' 'i686' 'arm')
url="https://github.com/joewalnes/websocketd"
license=('BSD-2-Clause ')
depends=('glibc')

source_x86_64=("https://github.com/joewalnes/websocketd/releases/download/v${pkgver}/websocketd-${pkgver}-linux_amd64.zip")
md5sums_x86_64=('e0ac3172dddd2709c5a5d8fa509e7464')
md5sums_i686=('580cff1818353e74093b3624e8a7e736')

source_i686=("https://github.com/joewalnes/websocketd/releases/download/v${pkgver}/websocketd-${pkgver}-linux_386.zip")

package() {
    cd "${srcdir}"
    install -Dm755 "${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
