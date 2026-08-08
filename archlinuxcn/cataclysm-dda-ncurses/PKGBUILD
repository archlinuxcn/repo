# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Reihar <reihar@necronomicon.fr>
# Contributor: Nick Hu <nickhu00@gmail.com>
# Contributor: Fernando Carmona Varo <ferkiwi @t gmail dot com>
pkgname=cataclysm-dda-ncurses
pkgver=0.I
pkgrel=1
pkgdesc="A post-apocalyptic roguelike (ncurses only)"
arch=('x86_64')
url="https://cataclysmdda.org/"
license=('CC-BY-NC-SA-3.0')
depends=('ncurses' 'libbacktrace' 'gettext' 'zlib' 'glibc' 'libgcc' 'libstdc++')
makedepends=('astyle')
conflicts=('cataclysm-dda' 'cataclysm-dda-git' 'cataclysm-dda-ncurses-bin')
provides=('cataclysm-dda')
source=("$pkgname-$pkgver.tar.gz::https://github.com/CleverRaven/Cataclysm-DDA/archive/$pkgver.tar.gz")
sha256sums=('1e4a6e1f70d805d01c97c71294eb45aad47f56f1e895fa783127e20298ee3249')

build() {
  cd "Cataclysm-DDA-$pkgver"

  export LDFLAGS=${LDFLAGS/-Wl,-z,pack-relative-relocs}
  export CXXFLAGS+=" -Wno-error=maybe-uninitialized"
  export CXXFLAGS+=" -Wno-error=sfinae-incomplete"
  export CXXFLAGS="${CXXFLAGS/-Wp,-D_GLIBCXX_ASSERTIONS}"
  export CXXFLAGS="${CXXFLAGS/-fcf-protection}"
  export CXXFLAGS="${CXXFLAGS/-fstack-clash-protection}"

  make PREFIX=/usr PCH=0 RELEASE=1 USE_XDG_DIR=1 LTO=1 RUNTESTS=0 TESTS=0 LOCALIZE=1 LANGUAGES=all BACKTRACE=1 LIBBACKTRACE=1 ASTYLE=0
  ./lang/compile_mo.sh
}

package() {
  cd "Cataclysm-DDA-$pkgver"

  make DESTDIR="$pkgdir" PREFIX=/usr PCH=0 RELEASE=1 USE_XDG_DIR=1 LTO=1 RUNTESTS=0 TESTS=0 LOCALIZE=1 LANGUAGES=all ASTYLE=0 install

  install -d "$pkgdir/usr/share/doc/cataclysm-dda"
  cp -r doc/* "$pkgdir/usr/share/doc/cataclysm-dda"

  find "$pkgdir/usr/share/doc/cataclysm-dda" -xtype l -delete
  rm -f "$pkgdir/usr/share/doc/cataclysm-dda/"*.6
  install -Dm644 -t "$pkgdir/usr/share/man/man6" "doc/cataclysm.6"

  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  cd lang/mo
  for i in *; do
    install -d "${pkgdir}/usr/share/locale/${i}/LC_MESSAGES"
    cp "${i}/LC_MESSAGES/cataclysm-dda.mo" "${pkgdir}/usr/share/locale/${i}/LC_MESSAGES"
  done
}
