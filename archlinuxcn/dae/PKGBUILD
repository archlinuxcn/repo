# Maintainer: cubercsl <2014cais01 at gmail dot com>
pkgname=dae
pkgver=0.2.4
pkgrel=1
pkgdesc="A Linux lightweight and high-performance transparent proxy solution based on eBPF."
arch=(x86_64 aarch64)
url="https://github.com/daeuniverse/dae"
license=('AGPL')
makedepends=(clang go)
source=(
    "$_pkgname-$pkgver.zip::https://github.com/daeuniverse/dae/releases/download/v$pkgver/dae-full-src.zip"
)
sha256sums=('54ca53b0a0b1253934fbe98e7c1d18e74fc0033be4a664ab5ccc9f3748187dac')

build() {
    export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
    export CFLAGS="-fno-stack-protector"
    cd "$srcdir"
    make VERSION="$pkgver"
}

package() {
    depends=(
        glibc
        v2ray-geoip
        v2ray-domain-list-community
    )
    backup=("etc/dae/config.dae")

    cd "$srcdir"
    install -Dm755 "dae" "$pkgdir/usr/bin/dae"
    install -Dm644 "install/dae.service" "$pkgdir/usr/lib/systemd/system/dae.service"
    install -Dm640 "install/empty.dae" "$pkgdir/etc/dae/config.dae"
    install -Dm644 "example.dae" "$pkgdir/etc/dae/config.dae.example"

    mkdir -p "$pkgdir/usr/share/dae"
    ln -vs /usr/share/v2ray/geoip.dat $pkgdir/usr/share/dae/geoip.dat
    ln -vs /usr/share/v2ray/geosite.dat $pkgdir/usr/share/dae/geosite.dat 
}
