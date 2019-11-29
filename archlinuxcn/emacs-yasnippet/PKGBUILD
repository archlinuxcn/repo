# Maintainer: Jon Eyolfson <jon@eyl.io>
# Contributor: Gianmarco Brocchi <brocchi@poisson.phc.unipi.it>
# Contributor: Hauke Wesselmann <hauke@h-dawg.de>
pkgname=emacs-yasnippet
pkgver=0.13.0
pkgrel=1
pkgdesc="Yet another snippet extension for Emacs"
arch=('any')
url="https://github.com/joaotavora/yasnippet"
license=('MIT')
depends=('emacs')
source=("https://github.com/joaotavora/yasnippet/archive/${pkgver}.tar.gz")
sha256sums=('8cde904564de987c9dd98e484854ecf8c51094ab4b5adf83cceb3f7542179a8a')

package() {
  cd "${srcdir}/yasnippet-${pkgver}"
  install -d  "${pkgdir}/usr/share/emacs/site-lisp/yas"
  cp -a * "${pkgdir}/usr/share/emacs/site-lisp/yas"
}
