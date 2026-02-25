# Maintainer: everyx <lunt.luo#gmail.com>

pkgname=cronet-go
pkgver=0.0.1_143.0.7499.109_1
_ver=${pkgver//_/-}
pkgrel=2
pkgdesc='Go bindings for naiveproxy.'
arch=('i686' 'x86_64' 'armv7h' 'aarch64' 'loongarch64')
url='https://github.com/SagerNet/cronet-go'
license=("LicenseRef-${pkgname}")
depends=('libgcc' 'glibc')
provides=("libcronet.so")
source=("${pkgname}::git+https://github.com/SagerNet/cronet-go.git#tag=v$_ver")
sha256sums=('6b17788e13f4a8444881a13754fdff4dc100f098491d3537d096c876c92d808c')
makedepends=('go>=1.25' 'git' 'python' 'python-requests' 'dpkg' 'unzip' 'ninja')
options=(!debug)

prepare() {
    cd "${pkgname}"

    git submodule update --init --depth 1

    export GOPATH="${srcdir}"
    go mod download -modcacherw
}

build(){
    cd "${pkgname}"

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

    go run ./cmd/build-naive build
}

package() {
    cd "$pkgname"

    declare -A cpu_map=(
        [i686]="x86"
        [x86_64]="x64"
        [armv7h]="arm"
        [aarch64]="arm64"
        [loongarch64]="loong64"
    )

    local cpu=${cpu_map[$CARCH]:-$CARCH}

    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
    install -Dm644 naiveproxy/src/out/cronet-$(go env GOOS)-${cpu}/libcronet.so -t "$pkgdir/usr/lib/"
}
