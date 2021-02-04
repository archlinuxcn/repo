# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgbase=vmessping
pkgname=('vmessconv' 'vmessping' 'vmessspeed')
pkgver=0.3.4
pkgrel=2
pkgdesc="A ping prober for vmess:// links in common seen formats"
arch=('x86_64')
url="https://github.com/v2fly/vmessping"
license=('MIT')
depends=('glibc')
makedepends=('go')
source=("${pkgbase}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "vmessping-0.3.4.patch")
sha256sums=('1f3f1759039f83e32d3b8a824b9f7518e22ee07e515069a35d1dc22f36cd5f64'
            'd0a736017cf46485144a84fc389be1de3699da386ad1ef1e05ff32a098ba60d5')

prepare() {
    cd "$srcdir"/"$pkgbase-$pkgver"/
    patch -p1 -i ../vmessping-0.3.4.patch
}

build() {
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    for VMESSPING in vmessconv vmessping vmessspeed; do
        cd "$srcdir"/"$pkgbase-$pkgver"/
        cd cmd/"${VMESSPING}"/
        go build -ldflags="-X=main.MAINVER=${pkgver} -linkmode=external"
    done
}

package_vmessconv() {
    cd "$srcdir"/"$pkgbase-$pkgver"/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/vmessconv/
    cd cmd/vmessconv/
    install -Dm 755 vmessconv -t "${pkgdir}"/usr/bin/
}

package_vmessping() {
    cd "$srcdir"/"$pkgbase-$pkgver"/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/vmessping/
    cd cmd/vmessping/
    install -Dm 755 vmessping -t "${pkgdir}"/usr/bin/
}

package_vmessspeed() {
    cd "$srcdir"/"$pkgbase-$pkgver"/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/vmessspeed/
    cd cmd/vmessspeed/
    install -Dm 755 vmessspeed -t "${pkgdir}"/usr/bin/
}
