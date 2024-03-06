# Maintainer: Rocket Aaron <i at rocka dot me>
# Contributor: Manuel Gugger <mdgdot[at]tutanota[dot]com>

pkgname=act_runner
pkgver=0.2.6
pkgrel=1
pkgdesc="Runner for Gitea based on Gitea fork of act"
arch=('x86_64')
url="https://gitea.com/gitea/act_runner"
license=('MIT')
optdepends=('docker' 'gitea')
makedepends=('go')
source=("act_runner-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        'act_runner.service'
        'act_runner.sysusers')
sha256sums=('8dbc7da07752d7ed8900581963045f3dcbfe02c52cb560acefd88099b8daf136'
            'ffcd415415b68a2902c942eaf0b13b11d184974434e333735e31ce14cdab3b57'
            'f0de2d8076ff59db8f5686addc096fc29e02190bfb7b44329979b3d9e1ad292f')

build() {
    cd "$pkgname"
    # https://wiki.archlinux.org/title/Go_package_guidelines#Supporting_debug_packages
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOPATH="${srcdir}"
    export GOFLAGS="-buildmode=pie -mod=readonly -modcacherw"
    go build -ldflags "-compressdwarf=false -linkmode external -X 'main.version=$pkgver'" .
    ./act_runner generate-config > "$srcdir/act_runner.yaml"
}

package() {
    install -Dm755 "$srcdir/$pkgname/act_runner" "$pkgdir/usr/bin/act_runner"
    install -Dm644 "$srcdir/$pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 "$srcdir/act_runner.service" "$pkgdir/usr/lib/systemd/system/act_runner.service"
    install -Dm644 "$srcdir/act_runner.sysusers" "$pkgdir/usr/lib/sysusers.d/act_runner.conf"
    install -Dm644 "$srcdir/act_runner.tmpfiles" "$pkgdir/usr/lib/tmpfiles.d/act_runner.conf"
    install -Dm644 "$srcdir/act_runner.yaml" "$pkgdir/etc/act_runner/act_runner.yaml"
}
