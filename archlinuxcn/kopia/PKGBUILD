# Maintainer: Christian Heusel <christian@heusel.eu>
# Contributor: Jens Jäschke <arch [at] jensjaeschke [dot] de>

pkgname=kopia
pkgdesc='A cross-platform backup-tool with encryption, deduplication, compression and cloud support.'
pkgver=0.20.0
pkgrel=1
arch=('x86_64')
url='https://kopia.io'
license=('Apache-2.0')
depends=('glibc')
makedepends=('go')
checkdepends=('openssh' 'inetutils')
source=("$pkgname-$pkgver.tar.gz::https://github.com/kopia/kopia/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('267fa37983ffac6502bcf244b4f79822f442e1b0d67cb20ac2fc0db590c426de')

build() {
    cd $pkgname-$pkgver
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    go build -ldflags "-linkmode=external -X github.com/kopia/kopia/repo.BuildVersion=$pkgver-$pkgrel -X github.com/kopia/kopia/repo.BuildInfo=unofficial -X github.com/kopia/kopia/repo.BuildGitHubRepo=ARCH_USER_REPOSITORY"
}

check() {
    make -C $pkgname-$pkgver test
}

package() {
    install -Dm755 "$pkgname-$pkgver/kopia" "$pkgdir/usr/bin/kopia"
}
