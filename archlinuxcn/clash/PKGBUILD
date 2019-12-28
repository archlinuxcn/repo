# Maintainer: Ariel AxionL <i@axionl.me>
# Contributor: Luke Yue <lukedyue@gmail.com>

pkgname=clash
pkgver=0.17.0
pkgrel=1
pkgdesc="A rule based proxy in Go"
arch=('x86_64')
url="https://github.com/Dreamacro/clash"
license=('GPL3')
provides=("clash")
conflicts=("clash-git" "clash-bin")
makedepends=('go' 'git')
depends=('glibc')

source=("clash@.service"
        "clash_user.service"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/Dreamacro/clash/archive/v${pkgver}.tar.gz"
        "https://raw.githubusercontent.com/Dreamacro/clash/master/LICENSE")

sha512sums=('e9e215e0a06d0d1072467342dd72e777725b94634714c5bd5fdee31f48897d9b8ab7e83830d836533d6862fa6ebfda56dbf138edd873140de61d8ccdf2a54572'
            '338c3a5904623bec48c03b2ef8cf452979c229fc5b89b2e0447664b40cd6e29c83cae47a19145be76d3ee2f0b6a54184a0cff69b834ba6107b444caacc02decf'
            'e30c6e094f7727e6293547742146935a557a503706c58692ae640d425f4f236bdead2f205d939466f779b1cb3f6ca9011d201a6bfdbb986b74f7afc62377eeb6'
            'd361e5e8201481c6346ee6a886592c51265112be550d5224f1a7a6e116255c2f1ab8788df579d9b8372ed7bfd19bac4b6e70e00b472642966ab5b319b99a2686')

build() {
    cd "${pkgname}-${pkgver}"
    _build_time="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    CGO_ENABLED=0 go build -ldflags "-extldflags ${LDFLAGS} -X github.com/Dreamacro/clash/constant.Version=${pkgver} -X github.com/Dreamacro/clash/constant.BuildTime=${_build_time} -w -s" -mod=readonly
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -Dm755 "clash" "${pkgdir}/usr/bin/clash"
    install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/clash/LICENSE"
    install -Dm644 "${srcdir}/clash@.service" "${pkgdir}/usr/lib/systemd/system/clash@.service"
    install -Dm644 "${srcdir}/clash_user.service" "${pkgdir}/usr/lib/systemd/user/clash.service"
}
