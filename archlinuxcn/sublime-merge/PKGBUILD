# Maintainer: Honghao Li <im@rasphino.cn>

pkgname=sublime-merge
pkgver=1119
pkgrel=1
pkgdesc="Meet a new Git Client, from the makers of Sublime Text"
arch=('x86_64')
url="https://www.sublimemerge.com"
license=('custom')
depends=('gtk3')
optdepends=()
conflicts=('sublime-merge-dev')
#install=${pkgname}.install

source=('smerge'
        https://download.sublimetext.com/sublime_merge_build_${pkgver}_x64.tar.xz
        https://download.sublimetext.com/sublime_merge_build_${pkgver}_x64.tar.xz.asc)

sha256sums=('ddd804f64fa218d053f00ca82b5bb2625f9812d3530c2f2f88049dac9bb41a7d'
            '64b06320c0300923ade0901493cfd78e7f28598324f99d4c3609b3c85c5f1cea'
            'SKIP')

validpgpkeys=('1EDDE2CDFC025D17F6DA9EC0ADAE6AD28A8F901A')

package() {
  cd "${srcdir}"

  install -dm755 "${pkgdir}/opt"
  cp --preserve=mode -r "sublime_merge" "${pkgdir}/opt/sublime_merge"

  for res in 128x128 16x16 256x256 32x32 48x48; do
    install -dm755 "${pkgdir}/usr/share/icons/hicolor/${res}/apps"
    ln -s "/opt/sublime_merge/Icon/${res}/sublime-merge.png" "${pkgdir}/usr/share/icons/hicolor/${res}/apps/sublime-merge.png"
  done

  install -dm755 "${pkgdir}/usr/share/applications"
  mv "${pkgdir}/opt/sublime_merge/sublime_merge.desktop" "${pkgdir}/usr/share/applications/sublime_merge.desktop"

  install -dm755 "${pkgdir}/usr/bin"
  install -Dm755 "smerge" "${pkgdir}/usr/bin/smerge"

}

