# Maintainer: Poscat <poscat@mail.poscat.moe>
# Contributor: Alex Whitt <alex.joseph.whitt@gmail.com>

pkgname=emacs-projectile
pkgver=2.1.0
pkgrel=1
pkgdesc="Project Interaction Library for Emacs"
arch=(any)
url="https://github.com/bbatsov/projectile"
license=('GPL3')
depends=('emacs' 'emacs-pkg-info')
source=("https://github.com/bbatsov/projectile/archive/v${pkgver}.tar.gz")
sha256sums=('c74fc6f062ea16af9ffcec67f8ce379e56819f1a359ac86b670cf7cfe2415f7a')

build() {
  cd "${srcdir}/projectile-${pkgver}"
  emacs -q --no-splash -batch -L . -f batch-byte-compile *.el
}

package() {
  cd "${srcdir}/projectile-${pkgver}"
  mkdir -p "${pkgdir}/usr/share/emacs/site-lisp/projectile/"
  install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/projectile/"
}
