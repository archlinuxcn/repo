# Maintainer: Alex Whitt <alex.joseph.whitt@gmail.com>

_pkgsrcname=pkg-info.el
_pkgmaintainer=lunaryorn
_pkgdestdirname=pkg-info
_versionprefix=
pkgver=0.6
pkgrel=2
pkgdesc="Provide information about Emacs packages"
pkgname=emacs-${_pkgdestdirname}
arch=(any)
url="https://github.com/${_pkgmaintainer}/${_pkgsrcname}"
license=('GPL3')
depends=('emacs' 'emacs-epl')
source=("$pkgname-$pkgver.tar.gz::https://github.com/${_pkgmaintainer}/${_pkgsrcname}/archive/${_versionprefix}${pkgver}.tar.gz")
sha256sums=('29830aa84b049c7fe0c5b68157b283f0e549459592262c5eea605b6194b9f445')

build() {
  cd "${srcdir}/${_pkgdestdirname}-${pkgver}"
  emacs -q --no-splash -batch -L . -f batch-byte-compile *.el
}

package() {
  cd "${srcdir}/${_pkgdestdirname}-${pkgver}"
  mkdir -p "${pkgdir}/usr/share/emacs/site-lisp/${_pkgdestdirname}/"
  install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/${_pkgdestdirname}/"
}
