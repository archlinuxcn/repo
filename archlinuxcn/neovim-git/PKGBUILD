# Maintainer: Florian Walch <florian+aur@fwalch.com>
# Contributor: Florian Hahn <flo@fhahn.com>
# Contributor: Sven-Hendrik Haase <svenstaro@gmail.com>

pkgname=neovim-git
pkgver=0.4.0.r1426.g4ab7bbf3ea
pkgrel=1
pkgdesc='Fork of Vim aiming to improve user experience, plugins, and GUIs.'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url='https://neovim.io'
backup=('etc/xdg/nvim/sysinit.vim')
license=('custom:neovim')
depends=('libluv' 'libtermkey' 'libutf8proc' 'libuv' 'libvterm>=0.1.git5' 'luajit' 'msgpack-c' 'unibilium')
makedepends=('cmake' 'git' 'gperf' 'lua51-mpack' 'lua51-lpeg')
optdepends=('python2-neovim: for Python 2 plugin support (see :help provider-python)'
            'python-neovim: for Python 3 plugin support (see :help provider-python)'
            'ruby-neovim: for Ruby plugin support (see :help provider-ruby)'
            'xclip: for clipboard support (or xsel) (see :help provider-clipboard)'
            'xsel: for clipboard support (or xclip) (see :help provider-clipboard)'
            'wl-clipboard: for clipboard support on wayland (see :help clipboard)')
source=("${pkgname}::git+https://github.com/neovim/neovim.git")
sha256sums=('SKIP')
provides=("neovim=${pkgver}")
conflicts=('neovim')
install=neovim-git.install
options=(!strip)

pkgver() {
  cd "${pkgname}"
  git describe --long | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cmake -S"${pkgname}" -Bbuild \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

check() {
  cd "${srcdir}/build"
  ./bin/nvim --version
  ./bin/nvim --headless -u NONE -i NONE -c ':quit'
}

package() {
  cd "${srcdir}/build"
  DESTDIR="${pkgdir}" cmake --build . --target install

  cd "${srcdir}/${pkgname}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm644 runtime/nvim.desktop "${pkgdir}/usr/share/applications/nvim.desktop"
  install -Dm644 runtime/nvim.png "${pkgdir}/usr/share/pixmaps/nvim.png"

  # Make Arch vim packages work
  mkdir -p "${pkgdir}"/etc/xdg/nvim
  echo "\" This line makes pacman-installed global Arch Linux vim packages work." > "${pkgdir}"/etc/xdg/nvim/sysinit.vim
  echo "source /usr/share/nvim/archlinux.vim" >> "${pkgdir}"/etc/xdg/nvim/sysinit.vim

  mkdir -p "${pkgdir}"/usr/share/vim
  echo "set runtimepath+=/usr/share/vim/vimfiles" > "${pkgdir}"/usr/share/nvim/archlinux.vim
}

# vim:set sw=2 sts=2 et:
