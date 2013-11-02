# Maintainer: Simon Gomizelj <simongmzlj@gmail.com>
# Contributor: Daniel Micay <danielmicay@gmail.com>

pkgname=vim-youcompleteme-git
pkgver=951.b288dce
pkgver() {
  cd "YouCompleteMe"
  echo $(git rev-list --count master).$(git rev-parse --short master)
}
pkgrel=1
pkgdesc='A code-completion engine for Vim'

arch=(i686 x86_64)
url='http://valloric.github.com/YouCompleteMe/'
license=('GPL3')
groups=('vim-plugins')
depends=('vim' 'clang' 'python2')
makedepends=('git' 'cmake')
provides=('vim-youcompleteme')
conflicts=('vim-youcompleteme')
source=('git+git://github.com/Valloric/YouCompleteMe.git'
        'git+git://github.com/bewest/argparse.git'
        'git+git://github.com/defnull/bottle.git'
        'git+git://github.com/slezica/python-frozendict.git'
        'git+git://github.com/davidhalter/jedi.git'
        'git+git://github.com/kennethreitz/requests.git'
        'git+git://github.com/ross/requests-futures.git'
        'git+git://github.com/Pylons/waitress.git')
sha1sums=('SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP')
install=install

build() {
  cd "YouCompleteMe/cpp"
  cmake -G "Unix Makefiles" -DUSE_SYSTEM_LIBCLANG=ON
  make ycm_core
  make ycm_support_libs
}

package() {
  mkdir -p "$pkgdir/usr/share/vim/vimfiles"

  cd "$srcdir/YouCompleteMe"
  cp -a autoload doc plugin python third_party "$pkgdir/usr/share/vim/vimfiles"
  ln -sf /usr/lib/llvm/libclang.so "$pkgdir/usr/share/vim/vimfiles/python/"

  cd "$srcdir"
  cp -a argparse bottle python-frozendict jedi requests requests-futures waitress \
    "$pkgdir/usr/share/vim/vimfiles/third_party/"
}
