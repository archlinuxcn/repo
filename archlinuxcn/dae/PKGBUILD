# Maintainer: cubercsl <2014cais01 at gmail dot com>
pkgbase=dae
_pkgname=dae
_header_commit=378c3c576e0f4c785a3d5e71400b552725527f30
pkgname=(
    $_pkgname
    $_pkgname-geoip-v2raycompat
    $_pkgname-geosite-v2raycompat

)
pkgver=0.1.1
pkgrel=1
pkgdesc="A Linux lightweight and high-performance transparent proxy solution based on eBPF."
arch=(x86_64)
url="https://github.com/daeuniverse/dae"
license=('AGPL')
makedepends=(clang llvm go)
source=(
    "$_pkgname::https://github.com/daeuniverse/dae/archive/refs/tags/v$pkgver.tar.gz"
    "dae_bpf_headers::https://github.com/daeuniverse/dae_bpf_headers/archive/$_header_commit.tar.gz"
)
sha256sums=('2ce70276c9bf1293ad9d69fe22d53fdd097c1efca5e964424daf400e30e92234'
            '475387ddff6e281ee21a39948d1d90bf728e5bcb16ea678e9038ed6a350b7016')

prepare() {
    rm -rf "$srcdir/$_pkgname-$pkgver/control/kern/headers"
    ln -sf "$srcdir/dae_bpf_headers-$_header_commit" "$srcdir/$_pkgname-$pkgver/control/kern/headers"
}

build() {
    export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
    export CFLAGS=""

    cd "$srcdir/$_pkgname-$pkgver"
    make VERSION="$pkgver"
}

package_dae() {
    provides=($_pkgname)
    conflicts=($_pkgname)
    depends=(
        glibc
        dae-geoip
        dae-geosite
    )
    backup=("etc/dae/config.dae")

    cd "$srcdir/$_pkgname-$pkgver"
    install -Dm755 "dae" "$pkgdir/usr/bin/dae"
    install -Dm644 "install/dae.service" "$pkgdir/usr/lib/systemd/system/dae.service"
    install -Dm640 "install/empty.dae" "$pkgdir/etc/dae/config.dae"
    install -Dm644 "example.dae" "$pkgdir/etc/dae/config.dae.example"
}

package_dae-geoip-v2raycompat() {
    arch=(any)
    pkgdesc="v2ray geoip compat for dae"
    depends=(v2ray-geoip)
    provides=($_pkgname-geoip)

    install -dm755 "$pkgdir/usr/share/dae"
    ln -s /usr/share/v2ray/geoip.dat "$pkgdir/usr/share/dae/geoip.dat"
}

package_dae-geosite-v2raycompat() {
    arch=(any)
    pkgdesc="v2ray geosite compat for dae"
    depends=(v2ray-domain-list-community)
    provides=($_pkgname-geosite)

    install -dm755 "$pkgdir/usr/share/dae"
    ln -s /usr/share/v2ray/geosite.dat "$pkgdir/usr/share/dae/geosite.dat"
}
