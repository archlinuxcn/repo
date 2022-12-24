# Maintainer: Tom Wadley <tom@tomwadley.net>

pkgname=nvm
pkgver=0.39.3
pkgrel=1
pkgdesc="Node Version Manager - Simple bash script to manage multiple active node.js versions"
url="https://github.com/nvm-sh/nvm"
arch=('any')
license=('MIT')
optdepends=('bash: bash completion')
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/nvm-sh/nvm/archive/v${pkgver}.tar.gz"
        "init-nvm.sh"
        "install-nvm-exec")
sha256sums=('2ab9ef6659ebce9686e82728f1eb857a3c2e91af2a631490ddb89eeb283aa540'
            '692317bfd036557f59543fef9b67ff38de68208d30361fe385291f58d3ac0425'
            '795d3f6ad3076aa4b0bb9cc48a2e6e79331d121278a887667fb707181a54a10b')

package() {
  cd "${srcdir}"

  # convenience script
  install -Dm644 init-nvm.sh "$pkgdir/usr/share/$pkgname/init-nvm.sh"

  # companion script which installs symlinks in NVM_DIR (see comment in script)
  install -Dm644 install-nvm-exec "$pkgdir/usr/share/$pkgname/install-nvm-exec"

  cd "${pkgname}-${pkgver}"

  # nvm itself
  install -Dm644 nvm.sh "$pkgdir/usr/share/$pkgname/nvm.sh"

  # nvm-exec script for 'nvm exec' command
  install -Dm755 nvm-exec "$pkgdir/usr/share/$pkgname/nvm-exec"

  # bash completion
  install -Dm644 bash_completion "$pkgdir/usr/share/$pkgname/bash_completion"

  # license
  install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}

# vim:set ts=2 sw=2 et:
