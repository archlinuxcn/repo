# Maintainer: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Honghao Li <im@rasphino.cn>

pkgname=sublime-merge
pkgver=2020
pkgrel=1
pkgdesc='Meet a new Git Client, from the makers of Sublime Text'
arch=('x86_64')
url='https://www.sublimemerge.com'
license=('custom')
depends=('gtk3')
source=("https://download.sublimetext.com/sublime_merge_build_${pkgver}_x64.tar.xz"
        "https://download.sublimetext.com/sublime_merge_build_${pkgver}_x64.tar.xz.asc"
        LICENSE)
b2sums=('e80ddf340afc5ccd199cc9e9b17b71003fa9af96426efa4d9348dd9679a6e035281fe1e8b9c74712e12d937aab30b84458c1cdac06a0e6bf86acb20de8d82969'
        'SKIP'
        'e17f9223fc423b385d20f78fd54bf8bdc0722134cb89e1a12f9105a4d130e9ae12f81997904b52ce6d6db45810d23db53c8f90c8a9bc1ac0ae4a8532d1097396')
validpgpkeys=('1EDDE2CDFC025D17F6DA9EC0ADAE6AD28A8F901A')

package() {
  cd sublime_merge
  install -dm755 "${pkgdir}"/usr/bin

  # Install binaries
  install -Dm755 -t "${pkgdir}"/opt/sublime_merge/ \
    crash_reporter \
    git-credential-sublime \
    ssh-askpass-sublime \
    sublime_merge

  # link executable to /usr/bin/
  ln -s /opt/sublime_merge/sublime_merge "${pkgdir}"/usr/bin/smerge

  # copy misc files
  cp --preserve=mode -r -t "${pkgdir}"/opt/sublime_merge/ \
    changelog.txt \
    Packages \
    Icon

  # link app icons to system folder
  for res in 256x256 128x128 48x48 32x32 16x16; do
    install -dm755 "${pkgdir}"/usr/share/icons/hicolor/${res}/apps
    ln -s /opt/sublime_merge/Icon/${res}/sublime-merge.png "${pkgdir}"/usr/share/icons/hicolor/${res}/apps/sublime-merge.png
  done

  # install desktop file and license
  install -Dm644 -t "${pkgdir}"/usr/share/applications/ "${srcdir}"/sublime_merge/sublime_merge.desktop
  install -Dm644 -t "${pkgdir}"/usr/share/licenses/${pkgname}/ "${srcdir}"/LICENSE
}
