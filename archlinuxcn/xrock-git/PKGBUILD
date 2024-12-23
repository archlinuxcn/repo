# Maintainer: taotieren <admin@taotieren.com>

pkgname=xrock-git
pkgver=1.1.2.r5.g95089f5
pkgrel=1
epoch=
pkgdesc="The low level tools for rockchip SOC with maskrom and loader mode support."
arch=('x86_64')
url="https://github.com/xboot/xrock"
license=('MIT')
depends=('libusb')
makedepends=('git' 'gcc')
optdepends=()
provides=(${pkgname%-git})
conflicts=(${pkgname%-git})
source=("${pkgname%-git}::git+${url}.git")
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname%-git}"
    git describe --long --tags | sed 's/^v//g' | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${pkgname%-git}"
    make
}

package() {
    install -Dm0755 "${srcdir}/${pkgname%-git}/${pkgname%-git}" "${pkgdir}/usr/bin/${pkgname%-git}"
    install -Dm0644 "${srcdir}/${pkgname%-git}/99-xrock.rules" "${pkgdir}/etc/udev/rules.d/99-xrock.rules"
    install -Dm0644 "${srcdir}/${pkgname%-git}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
