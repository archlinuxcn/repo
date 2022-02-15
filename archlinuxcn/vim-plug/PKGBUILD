# Maintainer: noblehelm <noblehlem at gmail dot com>
# Contributor: oozyslug <oozyslug at gmail dot com>
# Submitter: oozyslug <oozyslug at gmail dot com>

pkgname=vim-plug
pkgver=0.11.0
pkgrel=1
pkgdesc="A vim plugin manager"
arch=('any')
url="http://github.com/junegunn/vim-plug"
license=('MIT')
depends=('vim')
conflicts=('vim-plug-git')
provides=('vim-plug')
source=("https://github.com/junegunn/vim-plug/archive/${pkgver}.tar.gz"
	'LICENSE-MIT.txt'
	'plug.vimrc'
	)
sha512sums=('79ff462790dad8e517a60f698d18e7038bc14f3f018c75a45d840d6f47c9987ee12cd84b44acb3b2fbc0d0e10ce9449aad51656c67d8b3ba675225e3c58459a2'
            'aef00f3c6c9e529f40180f5e05a0c06dc614df3419969469baf574ed85611321c34415c3c731ffd5f6dfcf4ec9a34698b7851e2d9b5a46efa8de2410aa626fa8'
            '8e15c2074d0ce36daa0568167bcbcaf1038b8f65edcab661c9d41a9a18714b27accab28f5065408852329827ff4c84c03102c17bd542962cde1f057e88c4044c')
install=${pkgname}.install

package() {
  install -Dm 644 ${pkgname}-${pkgver}/plug.vim ${pkgdir}/usr/share/vim/vimfiles/autoload/plug.vim
  install -Dm 644 LICENSE-MIT.txt ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
  install -Dm 644 plug.vimrc ${pkgdir}/usr/share/vim-plug/vimrc.sample
}
