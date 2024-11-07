# Maintainer: Roald Clark <roaldclark@gmail.com>
# Contributor: Jun Ouyang <ouyangjun1999@gmail.com>
# Contributor: Takase <takase1121@proton.me>

_pkgname=tailscale
pkgname=derper-ipcert
pkgver=1.76.6
pkgrel=1
pkgdesc="A tool that runs a custom Tailscale DERP server (IP certs version)"
arch=('x86_64' 'aarch64')
url="https://github.com/tailscale/tailscale"
license=('BSD-3-Clause')
depends=(
    'bash'
    'glibc'
    'openssl'
)
makedepends=('go')
provides=("derper=${pkgver}")
conflicts=('derper')
backup=(
    'etc/conf.d/derper'
    'etc/derper/openssl.cnf'
)
options=(!lto)
install=derper-ipcert.install
source=("${pkgname}-v${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "derper.conf"
        "derper.service"
        "openssl-cert-gen.sh"
        "openssl.cnf"
        "0001-allow-usage-of-ip-certificates-by-bypassing-hostname.patch")
sha256sums=('1603c78a6a5e9f83b278d305e1196fbfdeeb841be10ac2ddb7ea433c2701234b'
            '8593d6c048f4174206cbac5d82810903eab8f0afef36c50be66a2c6018c9f988'
            'cda0c4e9b6e3be7ca4950ae43bd29588447eba7233e52ea067eb0215ee8eed18'
            '8473e7dde4617d2899f97e0f1716e2bfa780837486b3c8fe1f5a9f57c9c440d9'
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
