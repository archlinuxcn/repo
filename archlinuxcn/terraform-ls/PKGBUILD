# Maintainer: Thorben Günther <echo YWRtaW5AeGVucm94Lm5ldAo= | base64 -d>

pkgname=terraform-ls
pkgver=0.34.1
pkgrel=1
pkgdesc='Terraform Language Server'
arch=('x86_64' 'aarch64')
url='https://github.com/hashicorp/terraform-ls'
license=('MPL-2.0')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('7d677141fdcc20675d6c5fa7666a463d881424bd1c7bc346549f61e33bdc94f1')

build() {
    cd "$pkgname-$pkgver"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
    go build -ldflags "-X main.rawVersion=$pkgver -X main.prerelease="
}

package() {
    cd "$pkgname-$pkgver"
    install -Dm755 "$pkgname" "$pkgdir"/usr/bin/"$pkgname"
}
