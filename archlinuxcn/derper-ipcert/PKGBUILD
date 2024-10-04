# Maintainer: Roald Clark <roaldclark@gmail.com>
# Contributor: Jun Ouyang <ouyangjun1999@gmail.com>
# Contributor: Takase <takase1121@proton.me>

_pkgname=tailscale
pkgname=derper-ipcert
pkgver=1.74.1
pkgrel=2
pkgdesc="A tool that runs a custom Tailscale DERP server (IP certs version)"
arch=('x86_64' 'aarch64')
url="https://github.com/tailscale/tailscale"
license=('BSD-3-Clause')
depends=(
    'bash'
    'glibc'
)
makedepends=('go')
provides=("derper=${pkgver}")
conflicts=('derper')
backup=(
    'etc/conf.d/derper'
    'etc/derper/openssl.cnf'
)
options=(!lto)
source=("${pkgname}-v${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "derper.conf"
        "derper.service"
        "openssl-cert-gen.sh"
        "openssl.cnf"
        "0001-allow-usage-of-ip-certificates-by-bypassing-hostname.patch")
sha256sums=('ef7b8a76ce81133dc10f243d733302c070232cdd6594b685c6adbf32769d4f2c'
            '28f550b84a1873983763f8914d81fb057199d61e6d2781a7232dfb7aae717cda'
            '91a5c52b8aab064d851dde58770c6f0baccd31ea5f5ccca28d1fdaa5f3398640'
            '5c78d28f278240423acf6e7937568034646894bed69908815f213caf4dd95a3d'
            'fd981cea16dae0b6f3008a7009a2faabe1911706d06856d504a2e046fae63cc9'
            '66407bec41131197d2b0133dafe0e04b814b6c458052509515a1284a42046719')

prepare() {
    cd "$srcdir/$_pkgname-$pkgver"
    patch -Np1 -i ../0001-allow-usage-of-ip-certificates-by-bypassing-hostname.patch
}

build() {
    cd "$srcdir/$_pkgname-$pkgver"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    go build -v \
        -ldflags "-linkmode=external \"-extldflags=${LDFLAGS}\" -X tailscale.com/version.longStamp=${pkgver}" \
        ./cmd/derper
}

package() {
    cd "$srcdir/$_pkgname-$pkgver"
    install -Dm644 ../derper.conf "$pkgdir/etc/conf.d/derper"
    install -Dm644 ../derper.service -t "$pkgdir/usr/lib/systemd/system/"
    install -Dm644 ../openssl-cert-gen.sh -t "$pkgdir/etc/derper/"
    install -Dm644 ../openssl.cnf -t "$pkgdir/etc/derper/"
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
    install -Dm755 derper -t "$pkgdir/usr/bin/"
    ln -sfv /var/lib/derper/certs "${pkgdir}/etc/derper/certs"
}
