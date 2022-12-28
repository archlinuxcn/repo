# Maintainer: Jason Papakostas <vithos@gmail.com>
# Contributor: Sean Enck <enckse@gmail.com>

pkgname=ergochat
_upstream_pkgname=ergo
pkgver=2.11.0
pkgrel=1
pkgdesc="A modern IRC server written in Go"
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/ergochat/ergo"
license=('MIT')
install=install
depends=('glibc')
makedepends=('go' 'git')
source=("git+$url#tag=v$pkgver"
    "config.patch"
    "systemd-service-unit.patch"
    "ergochat.sysusers"
    "ergochat.tmpfiles")
sha256sums=('SKIP'
    '94ea647a7557002817d077d280e69a95ebce8a94d0806d84e623e44572edf0d2'
    'cba63567bbd989c22242d25c8c9dd23a82caded310fbddc1532e551d5adea708'
    '1912d91aff30318dfafedbdf6c786f096ff897962736bd960acf7130859cdff2'
    '3fbd033a9a7c92859f6e26005db2ddeddda3816b0e735f7772f10c4da4df0266')
backup=("etc/oragono.conf" "etc/$pkgname.conf" "etc/$pkgname/ircd.yaml")
replaces=("oragono")
conflicts=("oragono")
provides=("oragono")

prepare() {
    cd "$srcdir/$_upstream_pkgname" || exit
    patch --backup <../config.patch

    cd "$srcdir/$_upstream_pkgname/distrib/systemd" || exit
    patch --backup <../../../systemd-service-unit.patch
}

build() {
    GOPATH=$(pwd)/..
    export GOPATH
    cd "${srcdir}/$_upstream_pkgname" || exit

    GIT_COMMIT="$(git rev-parse HEAD 2>/dev/null)"

    # flags from https://wiki.archlinux.org/index.php/Go_package_guidelines
    # to address issues namcap warns about:
    #   ergo W: ELF file ('usr/bin/ergo') lacks FULL RELRO, check LDFLAGS.
    #   ergo W: ELF file ('usr/bin/ergo') lacks PIE.
    # related: https://bugs.archlinux.org/task/60928
    go build \
        -trimpath \
        -buildmode=pie \
        -ldflags "-X main.commit=${GIT_COMMIT} -linkmode external -extldflags \"${LDFLAGS}\"" \
        -v \
        .

    rm languages/README.md
    rm -rf languages/example
}

check() {
    GOPATH=$(pwd)/..
    export GOPATH
    cd "${srcdir}/$_upstream_pkgname" || exit

    go test ./...
}

package() {
    install -Dm644 "$srcdir/$pkgname.sysusers" "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
    install -Dm644 "$srcdir/$pkgname.tmpfiles" "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"

    cd "$srcdir/$_upstream_pkgname" || exit
    install -Dm644 "distrib/systemd/$_upstream_pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"
    install -Dm755 -d "$pkgdir/usr/share/$pkgname/i18n"
    cp languages/* "$pkgdir/usr/share/$pkgname/i18n/"
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
    install -Dm755 $_upstream_pkgname "$pkgdir/usr/bin/$pkgname"
    install -Dm644 default.yaml "$pkgdir/etc/$pkgname/ircd.yaml"
    install -Dm644 $_upstream_pkgname.motd "$pkgdir/usr/share/$pkgname/default.motd"
}
