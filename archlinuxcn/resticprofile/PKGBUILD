# Maintainer: Chih-Hsuan Yen <base64_decode("eXUzYWN0eHQydHR0ZmlteEBjaHllbi5jYwo=")>
# Contributor: Matthew Gamble <git@matthewgamble.net>
# Contributor: Kyle Brennan <kyle@metalspork.xyz>

pkgname=resticprofile
pkgver=0.25.0
pkgrel=1
pkgdesc="Configuration profiles manager and scheduler for restic backup"
arch=("x86_64")
url="https://github.com/creativeprojects/resticprofile"
license=("GPL3")
depends=("glibc" "restic")
makedepends=("go" "git")
options=(!lto)
source=("git+https://github.com/creativeprojects/resticprofile.git#tag=v$pkgver")
sha256sums=('SKIP')

build() {
    cd resticprofile

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

    LC_ALL=C _build_date="$(date)"
    _commit_hash=$(git rev-parse HEAD)

    go build -o resticprofile -v -ldflags "-X 'main.commit=${_commit_hash}' -X 'main.date=${_build_date}' -X 'main.builtBy=makepkg'"
}

package() {
    cd resticprofile

    install -Dm755 resticprofile "${pkgdir}/usr/bin/resticprofile"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/resticprofile/LICENSE"
    install -Dm644 README.md "${pkgdir}/usr/share/doc/resticprofile/README.md"

    install -dm755 "${pkgdir}/usr/share/resticprofile/examples/"
    install -Dm644 examples/* "${pkgdir}/usr/share/resticprofile/examples/"
    install -dm755 "${pkgdir}/usr/share/resticprofile/contrib/systemd/"
    install -Dm644 contrib/systemd/* "${pkgdir}/usr/share/resticprofile/contrib/systemd/"

    install -Dm644 contrib/completion/bash-completion.sh "${pkgdir}/usr/share/bash-completion/completions/resticprofile"
    install -Dm644 contrib/completion/zsh-completion.sh "${pkgdir}/usr/share/zsh/site-functions/_resticprofile"
}
