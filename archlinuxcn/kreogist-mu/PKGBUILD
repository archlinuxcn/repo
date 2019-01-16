# Maintainer: Frantic1048 <archer@frantic1048.com>

pkgname=kreogist-mu
pkgver='1.0.0beta5'
_git_tag='1.0-beta5'
pkgrel=1
epoch=1
pkgdesc="Fantastic cross-platform music manager.based on Qt5"
arch=('x86_64')
url="https://kreogist.github.io/Mu/"
license=('GPL')
changelog="$pkgname.changelog"
depends=(
  'mpv'
  'qt5-base'
)

makedepends=(
  'git'
  'gcc'
  'qt5-tools'
)

source=(
#  "https://github.com/Kreogist/mu-archlinux/releases/download/$pkgver.$pkgrel/$pkgname-resource.tar.gz"
  "https://codeload.github.com/Kreogist/Mu/tar.gz/$_git_tag"
  "kreogist-mu.desktop"
)

sha224sums=('c9a4d9737a1cc989ae63d6d3e49f53807fcb7fa47dce2e864f85cf8e'
            '4faf812fee8623c1f4bbd817397fc5a931f6744cc17ac77ba006980b')

build() {
  mkdir -p $srcdir/Mu-build
  cd $srcdir/Mu-build
  qmake "CONFIG+=release" $srcdir/Mu-$_git_tag/mu.pro
  make
}

package() {
  # rename excecutable to kreogist-mu
  # to avoid conflicting with
  mv $srcdir/Mu-build/bin/mu $srcdir/Mu-build/bin/kreogist-mu

  install -d $pkgdir/usr/bin/
  install -m775 $srcdir/Mu-build/bin/kreogist-mu $pkgdir/usr/bin/

  # i18n files
  # https://github.com/Kreogist/Mu/issues/17#issuecomment-164236195
  install -d $pkgdir/usr/share/Kreogist/mu/Language/
  for f in $srcdir/Mu-build/bin/*.qm
  do
    baseName=$(basename $f)
    languageName="${baseName%.qm}"
    install -d $pkgdir/usr/share/Kreogist/mu/Language/$languageName/
    install -m664 $f $pkgdir/usr/share/Kreogist/mu/Language/$languageName/
  done

  # static resource
  install -d $pkgdir/usr/share/icons/hicolor/512x512/apps/
  install -m664 $srcdir/Mu-$_git_tag/src/resource/icon/mu.png \
                $pkgdir/usr/share/icons/hicolor/512x512/apps/$pkgname.png

  install -d $pkgdir/usr/share/applications/
  install -m664 $srcdir/$pkgname.desktop $pkgdir/usr/share/applications/
}
