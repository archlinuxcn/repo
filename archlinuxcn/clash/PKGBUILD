# Maintainer: Luke Yue <lukedyue@gmail.com>

pkgname=clash
pkgver=0.12.0
pkgrel=1
pkgdesc="A rule based proxy in Go."
arch=('x86_64')
url="https://github.com/Dreamacro/clash"
license=('MIT')
provides=("clash")
conflicts=("clash-git" "clash-bin")
makedepends=('go' 'git')
depends=('glibc')

source=("clash@.service"
        "clash_user.service"
        "https://codeload.github.com/Dreamacro/clash/tar.gz/v${pkgver}"
        "https://raw.githubusercontent.com/Dreamacro/clash/master/LICENSE")

sha512sums=('e9e215e0a06d0d1072467342dd72e777725b94634714c5bd5fdee31f48897d9b8ab7e83830d836533d6862fa6ebfda56dbf138edd873140de61d8ccdf2a54572'
            '338c3a5904623bec48c03b2ef8cf452979c229fc5b89b2e0447664b40cd6e29c83cae47a19145be76d3ee2f0b6a54184a0cff69b834ba6107b444caacc02decf'
            '48f0f8ae5e7630edaafabed9ea017b40afeba7d51006750032a84b07d9af25747ccbc0b9b6f2090729b29d95f5fa9d65ba0e20e32fa42e05391af4f63bd09227'
            '46478b083104014b881ad546b89cfb16f040588f38e8c04ca664078061ba0e0653a394365d128410a9646f9159c9d9c7644a3ea42b22e4a4f240dfd6bea666c5')

prepare() {
    cd ${pkgname}-${pkgver}
    mkdir -p .gopath/src/github.com/Dreamacro/
    ln -sf ${PWD} .gopath/src/github.com/Dreamacro/clash
    export GOPATH="${PWD}/.gopath"

    go mod download
}

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    go build -o clash
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -Dm755 "clash" "${pkgdir}/usr/bin/clash"
    install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/clash/LICENSE"
    install -Dm644 "${srcdir}/clash@.service" "${pkgdir}/usr/lib/systemd/system/clash@.service"
    install -Dm644 "${srcdir}/clash_user.service" "${pkgdir}/usr/lib/systemd/user/clash.service"
}

