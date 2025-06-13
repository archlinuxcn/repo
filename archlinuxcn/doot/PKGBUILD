# Maintainer: Pol Rivero <aur at polrivero dot com>
pkgname=doot
pkgver=0.5.0
pkgrel=1
pkgdesc="A fast, simple and intuitive dotfiles manager that just gets the job done"
arch=('x86_64' 'aarch64')
url="https://github.com/pol-rivero/doot"
license=('MIT')
provides=('doot')
conflicts=('doot')

depends=('git' 'git-crypt')
makedepends=('git' 'go' 'sed')
optdepends=('diffutils: To display changes before overwriting a file')

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pol-rivero/doot/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('8d0b29e231dc8df96042aee7d140d6c13d93b70769c476bc315fc3e74c2ba6e4')

build() {
    tar -xzf "${pkgname}-${pkgver}.tar.gz"
    cd "${pkgname}-${pkgver}"

    sed -i "s/\[\[VERSION\]\]/${pkgver}/g" cmd/version.go
    sed -i "s/\[\[COMMIT\]\]/aur/g" cmd/version.go
    
    export CGO_ENABLED=0
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    go build -o doot
}

package() {
    # Install binary
    cd "${pkgname}-${pkgver}"
    install -Dm755 doot "$pkgdir/usr/bin/doot"

    # Generate and install shell completions
    install -d "$pkgdir/usr/share/bash-completion/completions"
    install -d "$pkgdir/usr/share/zsh/site-functions"
    install -d "$pkgdir/usr/share/fish/vendor_completions.d"

    "$pkgdir/usr/bin/doot" completion bash > "$pkgdir/usr/share/bash-completion/completions/doot"
    "$pkgdir/usr/bin/doot" completion zsh > "$pkgdir/usr/share/zsh/site-functions/_doot"
    "$pkgdir/usr/bin/doot" completion fish > "$pkgdir/usr/share/fish/vendor_completions.d/doot.fish"
}
