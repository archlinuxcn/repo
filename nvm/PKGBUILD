# Maintainer: Tom Wadley <tom@tomwadley.net>

pkgname=nvm
pkgver=0.33.2
pkgrel=1
pkgdesc="Node Version Manager - Simple bash script to manage multiple active node.js versions"
url="https://github.com/creationix/nvm"
arch=('any')
license=('MIT')
optdepends=('bash: bash completion')
install="${pkgname}.install"
source=("https://github.com/creationix/nvm/archive/v${pkgver}.zip"
        "init-nvm.sh"
        "install-nvm-exec")
md5sums=('044c54a968b55154daa08a6e24a5299a'
         'b75a15a2cbe04e6203ebaf6103e90926'
         '8f3c5b82f09636e9cf82d45d68c39cc6')

build() {
  cd "${pkgname}-${pkgver}"
}

package() {
  cd "${srcdir}"

  # convenience script
  install -Dm644 init-nvm.sh "$pkgdir/usr/share/$pkgname/init-nvm.sh"

  # companion script which installs nvm-exec in NVM_DIR where upstream expects it
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
