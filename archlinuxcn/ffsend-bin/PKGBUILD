# Maintainer: Tim Visee <tim@visee.me>
# Contributor: Ariel AxionL <i at axionl dot me>
#
# This PKGBUILD is managed externally, and is automatically updated here:
# - https://gitlab.com/timvisee/ffsend/blob/master/pkg/aur/ffsend-bin/PKGBUILD
# - Mirror: https://github.com/timvisee/ffsend/blob/master/pkg/aur/ffsend-bin/PKGBUILD

pkgname=ffsend-bin
pkgver=0.2.58
pkgrel=1
pkgdesc="Easily and securely share files from the command line. A Firefox Send client."
url="https://gitlab.com/timvisee/ffsend"
license=('GPL3')
source=("ffsend-v$pkgver::https://github.com/timvisee/ffsend/releases/download/v0.2.58/ffsend-v0.2.58-linux-x64-static"
        "ffsend-v$pkgver.bash::https://gitlab.com/timvisee/ffsend/raw/v0.2.58/contrib/completions/ffsend.bash"
        "ffsend-v$pkgver.zsh::https://gitlab.com/timvisee/ffsend/raw/v0.2.58/contrib/completions/_ffsend"
        "ffsend-v$pkgver.fish::https://gitlab.com/timvisee/ffsend/raw/v0.2.58/contrib/completions/ffsend.fish"
        "LICENSE-v$pkgver::https://gitlab.com/timvisee/ffsend/raw/v0.2.58/LICENSE") # automatically set in CI, see: /.gitlab-ci.yml
sha256sums=('fb7c918b583197be3e553af5931816a885c1934a0adc16f2f03dfeed21b8ec0e' '364cf8453d54af876a8ff6874cc7e1323748b0f3b147a0a3ddd3884dba11efdd' 'a1f951aa546bb1fe59f431274f639a1b334fb5c0bd3136b6674a7674dd3af223' '86c12006ba4c8cc957c866b0f5a90cddbea736d9baf8d0f905b384f7c118bc95' '8ceb4b9ee5adedde47b31e975c1d90c73ad27b6b165a1dcd80c7c545eb65b903')
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
