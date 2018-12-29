# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Alexander 'z33ky' Hirsch <1zeeky@gmail.com>
# The following contributors are from the vim-youcompleteme-git AUR package
# Contributor: Babken Vardanyan <483ken 4tgma1l
# Contributor: stykr
# Contributor: Svenstaro
# Contributor: KaiSforza
# Contributor: Simon Gomizelj <simongmzlj@gmail.com>
# Contributor: Daniel Micay <danielmicay@gmail.com>

pkgname=neovim-youcompleteme-core-git
pkgver=r2459.c209cdbb
pkgrel=1
pkgdesc='A code-completion engine for Vim'
arch=(i686 x86_64)
url='https://valloric.github.io/YouCompleteMe/'
license=('GPL3')
depends=('neovim' 'boost-libs' 'python>=3.2' 'clang>=6.0'
         'python-bottle' 'python-waitress' 'python-frozendict'
         'python-requests-futures' 'python-future' 'python-neovim'
         'python-regex')
makedepends=('git' 'cmake' 'boost')
optdepends=(
  'gocode-git: Go semantic completion'
  'godef-git: Go semantic completion'
  'nodejs-tern: JavaScript semantic completion'
  'racerd-git: Rust semantic completion'
  'typescript: Typescript semantic completion'
  'python-jedi: Python semantic completion')
# https://github.com/Valloric/ycmd/pull/885
#'omnisharp-roslyn: C# semantic completion'

source=(git+https://github.com/Valloric/YouCompleteMe.git
        git+https://github.com/Valloric/ycmd)
sha256sums=('SKIP'
            'SKIP')

pkgver() {
  cd YouCompleteMe
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}


prepare() {
  mkdir -p ycmd_build

  cd YouCompleteMe

  git submodule init third_party/ycmd
  git config submodule.third_party/ycmd.url "$srcdir/ycmd"
  git submodule update

  git -C third_party/ycmd checkout master
}

build() {
  cd ycmd_build

  cmake \
    -DUSE_PYTHON2=OFF \
    -DUSE_SYSTEM_BOOST=ON \
    -DUSE_CLANG_COMPLETER=ON \
    -DUSE_SYSTEM_LIBCLANG=ON \
    ../YouCompleteMe/third_party/ycmd/cpp

  make ycm_core
}

package() {
  pkg_ycmd_dir="$pkgdir/usr/share/nvim/runtime/third_party/ycmd"

  cd YouCompleteMe
  install -Ddm755 "$pkg_ycmd_dir"

  cp -r autoload doc plugin python "$pkgdir/usr/share/nvim/runtime"
  cp -r third_party/ycmd/{ycmd,ycm_core.so,CORE_VERSION} "$pkg_ycmd_dir"
  clang_version="$(clang --version|sed -n 's/clang version \([0-9.]\+\) .*/\1/p')"
  ln -s "/usr/lib/clang/$clang_version/include/" "$pkg_ycmd_dir/clang_includes"
  unset clang_version

  install -Ddm755 "$pkg_ycmd_dir/third_party/tern_runtime/node_modules/"
  install -Ddm755 "$pkg_ycmd_dir/third_party/gocode/"
  install -Ddm755 "$pkg_ycmd_dir/third_party/godef/"
  ln -s /usr/lib/node_modules/tern "$pkg_ycmd_dir/third_party/tern_runtime/node_modules/"
  ln -s /usr/bin/gocode "$pkg_ycmd_dir/third_party/gocode/"
  ln -s /usr/bin/godef "$pkg_ycmd_dir/third_party/godef/"

  find "$pkgdir" \( -name .git -or -name 'test*' -or -name 'run_tests.py' -or -name 'CMakeFiles' \) -exec rm -fr {} +

  python -m compileall -d /usr/share/nvim/runtime "$pkgdir/usr/share/nvim/runtime"
  python -O -m compileall -d /usr/share/nvim/runtime "$pkgdir/usr/share/nvim/runtime"
}
