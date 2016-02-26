# Maintainer: Facundo Tuesca <facutuesca at gmail dot com>

pkgname=vim-pathogen
pkgver=2.3
pkgrel=2
pkgdesc="A vim plugin for managing your runtimepath"
arch=('any')
url="http://github.com/tpope/vim-pathogen"
license=('GPL')
groups=('vim-plugins')
depends=('vim')
conflicts=('vim-pathogen-git')
provides=('vim-pathogen')
install=vimdoc.install
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/tpope/$pkgname/archive/v$pkgver.tar.gz")
md5sums=('8cf56e1d8f5c993bee44d89a003aa943')

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 autoload/pathogen.vim "$pkgdir"/usr/share/vim/vimfiles/autoload/pathogen.vim
}
