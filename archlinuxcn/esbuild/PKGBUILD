# Maintainer: Daniel Milde <daniel@milde.cz>
# Contributor: George Rawlinson <george@rawlinson.net.nz>

_name=esbuild
pkgname=${_name}
pkgver=0.16.10
pkgrel=1
pkgdesc="An extremely fast JavaScript and CSS bundler and minifier."
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
url="https://${_name}.github.io/"
license=('MIT')
makedepends=('go')
_snapshot="${_name}-${pkgver}"
source=("${_snapshot}.tar.gz::https://github.com/evanw/${_name}/archive/v${pkgver}.tar.gz")
b2sums=('fe281f8166cd5021cbba60586e0451745f84f5993b6fb096372fff6b488709f856b01c6216f2679531ba2e363bc3d98012f21f3e033e3a4420d25fe6d665d9a9')

build() {
    set -a
    CGO_CPPFLAGS="${CPPFLAGS}"
    CGO_CFLAGS="${CFLAGS}"
    CGO_CXXFLAGS="${CXXFLAGS}"
    CGO_LDFLAGS="${LDFLAGS}"
    GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
    set +a

    cd "${_snapshot}"
    go build -o "${srcdir}/build/" "./cmd/..."
}

package() {
    local bin="/usr/bin/${_name}"
    install -Dm755 "build/${_name}" "${pkgdir}${bin}"

    local profile="/etc/profile.d"
    install -dm755 "${pkgdir}${profile}"
    echo "export ESBUILD_BINARY_PATH='${bin}'" > "${pkgdir}${profile}/${_name}.sh"

    cd "${_snapshot}"
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" "LICENSE.md"
}
