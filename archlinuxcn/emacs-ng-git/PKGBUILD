# Maintainer:
# Contributor: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Sainnhe Park <sainnhe@gmail.com>
# Contributor: Juergen Hoetzel <juergen@archlinux.org>
# Contributor: alienzj <alienchuj@gmail.com>
# Contributor: Steven Tang <xosdy.t@gmail.com>
# Contributor: Renchi Raju <renchi@green.tam.uiuc.edu>

pkgname=emacs-ng-git
pkgver=r166435.gb944567a113
pkgrel=2
epoch=1
pkgdesc="A new approach to Emacs - Including TypeScript, Threading, Async I/O, and WebRender"
arch=(x86_64)
url="https://emacs-ng.github.io/emacs-ng/"
license=(GPL3)
depends=(texinfo libjpeg-turbo libtiff librsvg gpm giflib libxpm libotf m17n-lib gtk3 gnutls
         jansson cairo harfbuzz ncurses libxml2 libxt zlib libgccjit)
makedepends=(git rustup python texlive-core clang)
provides=(emacs emacs-ng)
conflicts=(emacs emacs-ng)
source=("git+https://github.com/emacs-ng/emacs-ng.git")
sha256sums=('SKIP')

pkgver() {
  cd emacs-ng
  printf "r%s.g%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd emacs-ng
  rustup install "$(cat rust-toolchain)"
  ./autogen.sh
}

build() {
  cd emacs-ng
  RUSTUP_TOOLCHAIN=$(cat rust-toolchain)
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
    --disable-build-details

  make V=1 PATH="$HOME/.rustup/toolchains/${RUSTUP_TOOLCHAIN}-$(uname -m)-unknown-linux-gnu/bin:$PATH" bootstrap
  make pdf
}

package() {
  cd emacs-ng
  make DESTDIR="$pkgdir" install
  make DESTDIR="$pkgdir" install-pdf

  # remove conflict with ctags package
  mv "$pkgdir"/usr/bin/{ctags,ctags.emacs}
  mv "$pkgdir"/usr/share/man/man1/{ctags.1.gz,ctags.emacs.1}

  # fix user/root permissions on usr/share files
  find "$pkgdir"/usr/share/emacs -exec chown root:root {} \;
}
