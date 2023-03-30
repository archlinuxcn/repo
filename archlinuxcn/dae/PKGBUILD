# Maintainer: cubercsl <2014cais01 at gmail dot com>
pkgbase=dae
_pkgname=dae
pkgname=(
    $_pkgname
    $_pkgname-geoip-v2raycompat
    $_pkgname-geosite-v2raycompat
)
pkgver=0.1.5
pkgrel=2
pkgdesc="A Linux lightweight and high-performance transparent proxy solution based on eBPF."
arch=(x86_64)
url="https://github.com/daeuniverse/dae"
license=('AGPL')
makedepends=(clang llvm go)
source=(
    "https://github.com/daeuniverse/dae/releases/download/v$pkgver/dae-full-src.zip"
)
sha256sums=('226aa5a8538ebcc009391fbeb7cad56ec60207a64bb43c8cbd89a60412c79b1a')

build() {
    export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
    export CFLAGS=""

    cd "$srcdir"
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

    cd "$srcdir"
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
