# Maintainer: Mort Yao <soi@mort.ninja>

pkgname=fstar-bin
pkgver=0.9.7.0
_subver=-alpha1
pkgrel=1
pkgdesc='A Higher-Order Effectful Language Designed for Program Verification'
url='https://fstar-lang.org/'
license=('Apache')
arch=('x86_64')
depends=()
provides=('fstar')
conflicts=('fstar' 'fstar-git')
source=("https://github.com/FStarLang/FStar/releases/download/V${pkgver}${_subver}/fstar_${pkgver}${_subver}_Linux_x86_64.tar.gz")
md5sums=('31316d6dc26e12e1c69b516bfdeeea3f')

package() {
  cd "fstar"

  install -d -m755 $pkgdir/opt/fstar $pkgdir/usr/bin
  cp -r * $pkgdir/opt/fstar

  # Instead of symlinking, create a wrapper script
  # ln -s /opt/fstar/bin/fstar.exe $pkgdir/usr/bin/fstar
  echo '#!/bin/bash' > $pkgdir/usr/bin/fstar
  echo '/opt/fstar/bin/fstar.exe --smt /opt/fstar/bin/z3 "$@"' >> $pkgdir/usr/bin/fstar
  chmod +x $pkgdir/usr/bin/fstar
}
