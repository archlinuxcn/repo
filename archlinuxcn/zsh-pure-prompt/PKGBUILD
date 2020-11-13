# Maintainer: Matthew McGinn <mamcgi@gmail.com>
# Contributor: Jeff Henson <jeff@henson.io>
# Contributor: Daniel Greve <greve.daniel.l@gmail.com>

pkgname=zsh-pure-prompt
pkgver=1.15.0
pkgrel=1
pkgdesc='Pretty, minimal and fast ZSH prompt'
arch=('any')
url='https://github.com/sindresorhus/pure'
_github_url='https://github.com/sindresorhus/pure'
license=('MIT')
depends=('git' 'zsh')
source=("https://github.com/sindresorhus/pure/archive/v${pkgver}.tar.gz")
sha256sums=('58915e0317763bae87f2c3b5b8e643d761dc64004e1153c8f5ba72f658c7fd74')

package() {
  cd "${srcdir}/pure-${pkgver}"
  install -Dm644 pure.zsh "${pkgdir}/usr/share/zsh/functions/Prompts/prompt_pure_setup"
  install -Dm644 async.zsh "${pkgdir}/usr/share/zsh/functions/Prompts/async"
  install -Dm644 license "${pkgdir}/usr/share/licenses/zsh-pure-prompt/license"
}
