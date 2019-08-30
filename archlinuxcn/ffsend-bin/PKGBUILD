# Maintainer: Tim Visee <tim@visee.me>
# Contributor: Ariel AxionL <i at axionl dot me>
#
# This PKGBUILD is managed externally, and is automatically updated here:
# - https://gitlab.com/timvisee/ffsend/blob/master/pkg/aur/ffsend-bin/PKGBUILD
# - Mirror: https://github.com/timvisee/ffsend/blob/master/pkg/aur/ffsend-bin/PKGBUILD

pkgname=ffsend-bin
pkgver=0.2.51
pkgrel=1
pkgdesc="Easily and securely share files from the command line. A Firefox Send client."
url="https://gitlab.com/timvisee/ffsend"
license=('GPL3')
source=("ffsend-v$pkgver::https://github.com/timvisee/ffsend/releases/download/v0.2.51/ffsend-v0.2.51-linux-x64-static"
        "ffsend-v$pkgver.bash::https://gitlab.com/timvisee/ffsend/raw/v0.2.51/contrib/completions/ffsend.bash"
        "ffsend-v$pkgver.zsh::https://gitlab.com/timvisee/ffsend/raw/v0.2.51/contrib/completions/_ffsend"
        "ffsend-v$pkgver.fish::https://gitlab.com/timvisee/ffsend/raw/v0.2.51/contrib/completions/ffsend.fish"
        "LICENSE-v$pkgver::https://gitlab.com/timvisee/ffsend/raw/v0.2.51/LICENSE") # automatically set in CI, see: /.gitlab-ci.yml
sha256sums=('06874d1e854365ad52b6723d2a18cd5d62be1c34b1a982cb89e1f4132877d829' '5d07864cc50626f663d4e0c87edc3e45605f66857633ab373a5f4b2a8d81d433' '75a5d1ef0baf7d5711137655aad145140021c8c64584baab95e9faaab765218a' 'd68f1327b93a4b030ce6d3d0bc11a8d04dd8a3ff7cabe159d1bdaa5df86fffa9' '8ceb4b9ee5adedde47b31e975c1d90c73ad27b6b165a1dcd80c7c545eb65b903')
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

    # Install shell completions and LICENSE file
    install -Dm644 "ffsend-v$pkgver.bash" "$pkgdir/usr/share/bash-completion/completions/ffsend"
    install -Dm644 "ffsend-v$pkgver.zsh" "$pkgdir/usr/share/zsh/site-functions/_ffsend"
    install -Dm644 "ffsend-v$pkgver.fish" "$pkgdir/usr/share/fish/vendor_completions.d/ffsend.fish"
    install -Dm644 "LICENSE-v$pkgver" "$pkgdir/usr/share/licenses/ffsend/LICENSE"
}
