# Maintainer: Matthew McGinn <mamcgi@gmail.com>
# Contributor: Jeff Henson <jeff@henson.io>
# Contributor: Daniel Greve <greve.daniel.l@gmail.com>

pkgname=zsh-pure-prompt
pkgver=1.17.0
pkgrel=1
pkgdesc='Pretty, minimal and fast ZSH prompt'
arch=('any')
url='https://github.com/sindresorhus/pure'
_github_url='https://github.com/sindresorhus/pure'
license=('MIT')
depends=('git' 'zsh')
source=("https://github.com/sindresorhus/pure/archive/v${pkgver}.tar.gz")
sha256sums=('7a3dfec47b23a5e849a907b83dac4fb057beb9e0638b71f061b0fabea6a83c70')

package() {
  cd "${srcdir}/pure-${pkgver}"
  install -Dm644 pure.zsh "${pkgdir}/usr/share/zsh/functions/Prompts/prompt_pure_setup"
  install -Dm644 async.zsh "${pkgdir}/usr/share/zsh/functions/Prompts/async"
  install -Dm644 license "${pkgdir}/usr/share/licenses/zsh-pure-prompt/license"
}
