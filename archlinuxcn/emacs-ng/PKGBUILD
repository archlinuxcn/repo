# Contributor: Sainnhe Park <sainnhe@gmail.com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=emacs-ng
pkgver=30.0.50
_fix_commit=0e134f2
pkgrel=11
pkgdesc="A new approach to Emacs - Including TypeScript, Threading, Async I/O, and WebRender"
arch=('x86_64')
url="https://emacs-ng.github.io/emacs-ng"
license=('GPL3')
provides=('emacs')
conflicts=('emacs')
depends=('jansson' 'ncurses' 'libgccjit' 'librsvg' 'libxcb' 'libxml2' 'gpm'
	 'dune' 'dbus' 'lcms2' 'hicolor-icon-theme' 'desktop-file-utils'
	 'alsa-lib' 'gnutls' 'zlib' 'tree-sitter' 'mailutils' 'sqlite'
	 'gtk3' 'libsm' 'xcb-util' 'libxcb' 'libwebp')
makedepends=('cargo' 'rustup' 'git' 'python' 'texlive-core')
source=("$pkgname-$pkgver_${_fix_commit}.tar.gz::https://github.com/emacs-ng/emacs-ng/archive/refs/tags/v0.0.${_fix_commit}.tar.gz")
sha256sums=('7b02d9a71ad2dd0288c7ef0deda62c5a68697c92486ba2ea3c8d8e4e1e78c006')

prepare() {
  cd ${pkgname}-0.0.${_fix_commit}
  rustup install "$(cat rust-toolchain)"
}

build() {
  cd ${pkgname}-0.0.${_fix_commit}
  RUSTUP_TOOLCHAIN=$(cat rust-toolchain)
  ./autogen.sh
  ./configure CFLAGS="-Wl,-rpath,shared -Wl,--disable-new-dtags" \
              --prefix=/usr \
	      --sysconfdir=/etc \
	      --libexecdir=/usr/lib \
	      --localstatedir=/var \
              --with-json \
	      --with-modules \
	      --with-compress-install \
	      --with-threads \
	      --with-included-regex \
	      --with-zlib \
	      --with-libsystemd \
	      --with-rsvg \
	      --without-imagemagick \
	      --with-gpm \
	      --without-xaw3d \
	      --with-dbus \
	      --without-pop \
	      --with-mailutils \
	      --with-gsettings \
	      --with-webrender \
	      --with-pgtk \
	      --disable-build-details 
        
  make V=1 PATH="$HOME/.rustup/toolchains/${RUSTUP_TOOLCHAIN}-$(uname -m)-unknown-linux-gnu/bin:$PATH" bootstrap
  make pdf
}

package() {
  cd ${pkgname}-0.0.${_fix_commit}
  make DESTDIR="$pkgdir" install
  make DESTDIR="$pkgdir" install-pdf
  
  # remove conflict with ctags package
  
  mv "$pkgdir"/usr/bin/{ctags,ctags.emacs}
  mv "$pkgdir"/usr/share/man/man1/{ctags.1.gz,ctags.emacs.1}
  
  # fix user/root permissions on usr/share files
  find "$pkgdir"/usr/share/emacs/$pkgver -exec chown root:root {} \;
}
