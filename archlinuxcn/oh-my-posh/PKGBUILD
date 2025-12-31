# Maintainer: wszqkzqk <wszqkzqk@qq.com>
pkgname=oh-my-posh
pkgver=28.9.0
pkgrel=1
pkgdesc="A prompt theme engine for any shell."
arch=('x86_64' 'armv7h' 'aarch64' 'riscv64' 'loong64')
url="https://github.com/JanDeDobbeleer/oh-my-posh"
license=('MIT')
makedepends=('go' 'gcc')
depends=('glibc')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('4b15555fa62fad4a025300f96200a1ef112a0dff2c22fcf21b0fc72486652e4c')

build() {
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

    cd "$pkgname-$pkgver/src"
    go build -ldflags="-linkmode=external -X github.com/jandedobbeleer/oh-my-posh/src/build.Version=$pkgver -X github.com/jandedobbeleer/oh-my-posh/src/build.Date=$(date +%F)" -o "$pkgname"
}

package() {
    cd "$pkgname-$pkgver/src"
    install -Dm 755 ./"${pkgname}" "${pkgdir}/usr/bin/oh-my-posh"
    install -Dm 644 "../COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -d "${pkgdir}/usr/share/oh-my-posh/themes"
    install -m 644 ../themes/* -t "${pkgdir}/usr/share/oh-my-posh/themes"
}
