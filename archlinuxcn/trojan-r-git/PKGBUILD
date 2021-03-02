# Maintainer: DuckSoft <realducksoft at gmail dot com>
pkgname=trojan-r-git
pkgver=0.1.0.r15
pkgrel=1
pkgdesc="Lightweight and blazing fast Trojan-GFW/Trojan-Go implementation"
arch=(aarch64 x86_64)
url=https://github.com/p4gefau1t/trojan-r
license=(GPL)
depends=(gcc-libs)
makedepends=(cargo git)
provides=(trojan-r)
conflicts=(trojan-r)
source=("${pkgname%-git}::git+$url" trojan-r@.service)
b2sums=('SKIP'
        '2760c08b1049d2813e9c649c67ead4366583015b04f13fd9f67987d537e6d526801ec5555056a49398a17be4e031ff525f76cffe8de76c215371848263ba7cda')

pkgver() {
    cd "$srcdir"/"${pkgname%-git}"
    printf "%s.r%s" $(cargo pkgid | cut -d# -f2 | cut -d: -f2) $(git rev-list --count HEAD)
}

build() {
    cd "$srcdir"/"${pkgname%-git}"
    cargo build --release --locked --all-features --target-dir=.
}

package() {
    cd "$srcdir"/"${pkgname%-git}"
    install -Dm755 release/trojan-r -t "$pkgdir"/usr/bin/
    install -Dm644 config/*.toml -t "$pkgdir"/etc/trojan-r/examples
    install -Dm644 ../trojan-r@.service -t "$pkgdir"/usr/lib/systemd/system/
}
