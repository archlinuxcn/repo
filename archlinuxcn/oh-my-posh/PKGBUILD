# Maintainer: wszqkzqk <wszqkzqk@qq.com>
pkgname=oh-my-posh
pkgver=29.3.0
pkgrel=1
pkgdesc="A prompt theme engine for any shell."
arch=('x86_64' 'armv7h' 'aarch64' 'riscv64' 'loong64')
url="https://github.com/JanDeDobbeleer/oh-my-posh"
license=('MIT')
makedepends=('go' 'gcc')
depends=('glibc')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('ff39f6ef2b4ca2d7d766f2802520b023986a5d6dbcd59fba685a9e5bacf41993')

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
