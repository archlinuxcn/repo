# Maintainer: Tim Visee <tim@visee.me>
# Contributor: Ariel AxionL <i at axionl dot me>
#
# This PKGBUILD is managed externally, and is automatically updated here:
# - https://gitlab.com/timvisee/ffsend/blob/master/pkg/aur/ffsend-bin/PKGBUILD
# - Mirror: https://github.com/timvisee/ffsend/blob/master/pkg/aur/ffsend-bin/PKGBUILD

pkgname=ffsend-bin
pkgver=0.2.61
pkgrel=1
pkgdesc="Easily and securely share files from the command line. A Firefox Send client."
url="https://gitlab.com/timvisee/ffsend"
license=('GPL3')
source=("ffsend-v$pkgver::https://github.com/timvisee/ffsend/releases/download/v0.2.61/ffsend-v0.2.61-linux-x64-static"
        "ffsend-v$pkgver.bash::https://gitlab.com/timvisee/ffsend/raw/v0.2.61/contrib/completions/ffsend.bash"
        "ffsend-v$pkgver.zsh::https://gitlab.com/timvisee/ffsend/raw/v0.2.61/contrib/completions/_ffsend"
        "ffsend-v$pkgver.fish::https://gitlab.com/timvisee/ffsend/raw/v0.2.61/contrib/completions/ffsend.fish"
        "LICENSE-v$pkgver::https://gitlab.com/timvisee/ffsend/raw/v0.2.61/LICENSE") # automatically set in CI, see: /.gitlab-ci.yml
sha256sums=('a37d407bbe5db63259828b724c0c98c831a1fb1e0695992e80f54886b5ca3311' '6d07b7c7cf241016687a486512ef0e0894e2dec2c2aa502f8646be230f33ab79' '8a8bc20a418a12eb87ffaf5c7905355fde7199d606eff00ef48a011d8ab0d08f' '0b4f6d36d9122fd9aa99028778a096b65d9270077a0743b226bef0306bf9bf14' '8ceb4b9ee5adedde47b31e975c1d90c73ad27b6b165a1dcd80c7c545eb65b903')
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
