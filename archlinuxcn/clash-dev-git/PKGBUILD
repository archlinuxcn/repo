# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Luke Yue <lukedyue@gmail.com>
# Contributor: asdf12303116 <a675750333@gmail.com>

pkgname=clash-dev-git
_pkgname=clash
pkgver=1.3.5.r14.gd48cfec
pkgrel=1
pkgdesc="A rule-based tunnel in Go"
arch=('x86_64')
url="https://github.com/Dreamacro/clash"
license=('GPL3')
depends=('clash-geoip' 'glibc')
makedepends=('git' 'go')
provides=('clash' 'clash-dev')
conflicts=('clash' 'clash-dev')
backup=("etc/clash/config.yaml")
source=("git+${url}.git#branch=dev"
        "clash-1.3.5.patch"
        "config.yaml"
        "clash.sysusers"
        "clash.tmpfiles"
        "clash.service"
        "clash@.service")
sha256sums=('SKIP'
            '511abd285aedc6dda651b1bf3d7fd84f51060fa313a12beb3ce68d916c2fc173'
            '62ed4460cd2ed4b400193ad04b0cccb76d7558f87c377a0033041841a73f7945'
            '149c6448a5630af1065ea230707331ac12663128568d6cf0e9d5480e94d1d104'
            '006bea79c75de78dcd4f3991bb9c4e6f706443131aeeccf8db076f8738f24ccd'
            '090e1598e9e9736c951b1e2488df7e573c4d29d2fd0e0da8cfc0edd998f8c8fb'
            'd22cc741edf783c6fc83bb62f67b5381a0421d2ea49959469c1b8da48488a827')

prepare() {
    cd "${srcdir}"/"${_pkgname}"/
    patch -p1 -i ../clash-1.3.5.patch
}

pkgver() {
    cd "${srcdir}"/"${_pkgname}"/
    git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    cd "${srcdir}"/"${_pkgname}"/
    sed "s/unknown version/${pkgver}/" -i constant/version.go
    sed "s/unknown time/$(LANG=C date -u)/" -i constant/version.go
    go build -ldflags="-linkmode=external"
}

check() {
    cd "${srcdir}"/"${_pkgname}"/
    go test github.com/Dreamacro/clash/...
}

package() {
    cd "${srcdir}"/"${_pkgname}"/
    install -Dm 755 clash -t "${pkgdir}"/usr/bin/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/clash-dev-git/
    install -Dm 644 "${srcdir}"/config.yaml -t "${pkgdir}"/etc/clash/
    install -Dm 644 "${srcdir}"/clash.sysusers "${pkgdir}"/usr/lib/sysusers.d/clash.conf
    install -Dm 644 "${srcdir}"/clash.tmpfiles "${pkgdir}"/usr/lib/tmpfiles.d/clash.conf
    install -Dm 644 "${srcdir}"/clash.service -t "${pkgdir}"/usr/lib/systemd/system/
    install -Dm 644 "${srcdir}"/clash@.service -t "${pkgdir}"/usr/lib/systemd/system/
}
