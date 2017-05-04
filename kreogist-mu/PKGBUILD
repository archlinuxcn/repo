# Maintainer: Frantic1048 <archer@frantic1048.com>

pkgname=kreogist-mu
pkgver='1.0.0beta'
_git_tag='1.0-beta'
pkgrel=1
epoch=1
pkgdesc="Fantastic cross-platform music manager.based on Qt5"
arch=('x86_64')
url="https://kreogist.github.io/Mu/"
license=('GPL')
changelog="$pkgname.changelog"
depends=(
  'pulseaudio'
  'ffmpeg'
  'phonon-qt5'
  'gst-libav'
  'ffmpeg'
  'desktop-file-utils'
  'hicolor-icon-theme'
)

optdepends=(
  'gst-plugins-good: good plugin libraries'
  'gst-plugins-bad: bad plugin libraries'
  'gst-plugins-ugly: ugly plugin libraries'
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

sha224sums=('9e13147a2cd7cf8a65f19153e13d1b3d6fe7add31df6c7b70d0f3227'
            '2f35e3f154fed55638827811b7ea3d0a34e3f7c39107bb7257a8a5f8')

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
