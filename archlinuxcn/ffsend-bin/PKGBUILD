# Maintainer: Tim Visee <tim@visee.me>
# Contributor: Ariel AxionL <i at axionl dot me>
#
# This PKGBUILD is managed externally, and is automatically updated here:
# - https://gitlab.com/timvisee/ffsend/blob/master/pkg/aur/ffsend-bin/PKGBUILD
# - Mirror: https://github.com/timvisee/ffsend/blob/master/pkg/aur/ffsend-bin/PKGBUILD

pkgname=ffsend-bin
pkgver=0.2.50
pkgrel=1
pkgdesc="Easily and securely share files from the command line. A Firefox Send client."
url="https://gitlab.com/timvisee/ffsend"
license=('GPL3')
source=("ffsend-v$pkgver::https://github.com/timvisee/ffsend/releases/download/v0.2.50/ffsend-v0.2.50-linux-x64-static"
        "ffsend-v$pkgver.bash::https://gitlab.com/timvisee/ffsend/raw/v0.2.50/contrib/completions/ffsend.bash"
        "ffsend-v$pkgver.fish::https://gitlab.com/timvisee/ffsend/raw/v0.2.50/contrib/completions/ffsend.fish") # automatically set in CI, see: /.gitlab-ci.yml
sha256sums=('cc9604991a6502d57d96a0e5616cff83f2ee3f92397720e2b9e88be6a8f1d0c5' 'bd0f63d4acaed87da9bc80725ec2242c273463cf64ac56c858c46164a6a8a3ab' '15d9a3e79265615a73af4de0e20dd662ad96470aac7fc5dfeff7d26d90bdc667')
arch=('x86_64')
provides=('ffsend')
conflicts=('ffsend')
depends=('ca-certificates')
optdepends=('xclip: clipboard support'
            'bash-completion: support auto completion for bash')

package() {
    cd "$srcdir"

    # Install Binary
    install -Dm755 "ffsend-v$pkgver" "$pkgdir/usr/bin/ffsend"

    # Install completions
    install -Dm644 "ffsend-v$pkgver.bash" "$pkgver/usr/share/bash-completion/completions/ffsend"
    install -Dm644 "ffsend-v$pkgver.fish" "$pkgver/usr/share/fish/vendor_completions.d/ffsend.fish"
}
