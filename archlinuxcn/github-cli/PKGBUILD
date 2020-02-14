# Source build of the official GitHub CLI
# Maintainer: Richard Bradfield <bradfier@fstab.me>

pkgname=github-cli
pkgver=0.5.5
pkgrel=3
pkgdesc="The GitHub CLI"
arch=("x86_64")
url="https://github.com/cli/cli"
license=("MIT")
depends=("glibc")
makedepends=("glibc" "go-pie")
optdepends=("git: To interact with repositories")
source=("$pkgname-$pkgver.tar.gz::https://github.com/cli/cli/archive/v${pkgver}.tar.gz")
sha256sums=('7c2cfdafe765a598b70b3e6de839590e8fa30a89bedc85799a43bdbc6fd3277e')

build() {
	cd "cli-$pkgver"
    go build \
        -trimpath \
        -ldflags "-extldflags ${LDFLAGS} -X github.com/cli/cli/command.Version=v${pkgver} -X github.com/cli/cli/command.BuildDate=$(date +%Y-%m-%d)" -o "bin/gh" ./cmd/gh
}

package() {
	cd "cli-$pkgver"
    install -Dm755 "${srcdir}/cli-${pkgver}/bin/gh" "${pkgdir}/usr/bin/gh"
    install -Dm644 "${srcdir}/cli-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/github-cli"
    install -Dm644 "${srcdir}/cli-${pkgver}/README.md" "${pkgdir}/usr/share/doc/github-cli/README.md"
}
