# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Gleidson <gleidson.echeli@gmail.com>

pkgname=emacs-haskell-mode-git
pkgver=r2719.f63f315
pkgrel=1
pkgdesc="Haskell mode package for Emacs"
arch=(any)
license=('GPL')
url="https://github.com/haskell/haskell-mode"
install=${pkgname}.install
makedepends=('emacs' 'git')
optdepends=(
    'stylish-haskell: code formatting support'
    'hasktags: tags generation support'
    )
provides=('emacs-haskell-mode')
source=("${pkgname}::git://github.com/haskell/haskell-mode")
md5sums=('SKIP')

pkgver() {
  cd "${srcdir}/${pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd "$srcdir"/${pkgname}
  sed -i 's|haskell-mode-pkg.el,|haskell-mode-pkg.el haskell-mode.el,|' Makefile
}

build() {
  cd "$srcdir"/${pkgname}
  export EMACS=/usr/bin/emacs
  make
}

package() {
  cd "$srcdir"/${pkgname}

  install -dm0755 "$pkgdir"/usr/share/emacs/site-lisp/haskell-mode
  install -m0644 *.el -t "$pkgdir"/usr/share/emacs/site-lisp/haskell-mode
  cp -a build-$(emacs --version | head -n1 | cut -f3 -d' ') -t "$pkgdir"/usr/share/emacs/site-lisp/haskell-mode/

  install -dm0755 "$pkgdir"/usr/share/doc/$pkgname
  install -m0644 NEWS README.md "$pkgdir"/usr/share/doc/$pkgname

  install -Dm0644 haskell-mode.info "$pkgdir"/usr/share/info/haskell-mode.info
}
