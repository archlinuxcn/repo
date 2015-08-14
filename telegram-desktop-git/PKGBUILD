_qtver=5.5.0
pkgname=telegram-desktop-git
pkgver=r654.e193a86
pkgrel=1
pkgdesc='Official desktop version of Telegram messaging app.'
arch=('i686' 'x86_64')
url="https://desktop.telegram.org/"
license=('GPL3')
depends=(ffmpeg icu jasper libexif libmng libwebp libxkbcommon-x11 mtdev openal)
makedepends=(git libunity libappindicator-gtk2 xorg-server-xvfb)
source=("http://download.qt-project.org/official_releases/qt/${_qtver%.*}/$_qtver/single/qt-everywhere-opensource-src-$_qtver.tar.gz"
        'tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#branch=dev')

pkgver() {
  cd "tdesktop"
  ( set -o pipefail
    git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

prepare() {
  if ! [ -d Libraries ]; then
    mkdir Libraries
    mv qt-everywhere-opensource-src-$_qtver Libraries/QtStatic
    cp tdesktop/Telegram/_qt_${_qtver//./_}_patch.diff Libraries/QtStatic
    cd Libraries/QtStatic
    git apply _qt_${_qtver//./_}_patch.diff
  fi

  sed -i 's/CUSTOM_API_ID//g' "$srcdir"/tdesktop/Telegram/Telegram.pro

  (
    echo 'INCLUDEPATH += "/usr/lib/glib-2.0/include"'
    echo 'INCLUDEPATH += "/usr/lib/gtk-2.0/include"'
    echo 'INCLUDEPATH += "/usr/include/opus"'
  ) >> "$srcdir"/tdesktop/Telegram/Telegram.pro

  # FIXME qmake (for Telegram.pro) does not generate the correct paths if the files does not exists
  #mkdir -p "$srcdir"/tdesktop/Telegram/GeneratedFiles
  #awk -v srcdir="$srcdir" '$1 == "PRE_TARGETDEPS" { for (i=3; i <= NF; i++) print "touch -t 197001010000", srcdir "/tdesktop/Telegram/" $i }' "$srcdir"/tdesktop/Telegram/Telegram.pro | sh -s
}

build() {
  local x _type
  # Building patched Qt
  cd Libraries/QtStatic
  ./configure -prefix "$srcdir/qt" -release -opensource -confirm-license -qt-xcb -no-opengl -static -nomake examples -nomake tests -skip qtquick1 -skip qtdeclarative
  make module-qtbase module-qtimageformats
  make module-qtbase-install_subtargets module-qtimageformats-install_subtargets

  export PATH="$srcdir/qt/bin:$PATH"

  mkdir -p "$srcdir"/tdesktop/Linux/{Debug,Release}Intermediate{Style,Emoji,Lang,Updater,}

  for _type in debug release; do
    for x in Style Lang; do
      cd "$srcdir"/tdesktop/Linux/${_type^}Intermediate$x
      qmake CONFIG+=${_type} ../../Telegram/Meta$x.pro
      make
    done
    cd "$srcdir"/tdesktop/Linux/${_type^}Intermediate
    # FIXME upstream likes broken things
    if ! [ -d "$srcdir"/tdesktop/Telegram/GeneratedFiles ]; then
      qmake CONFIG+=${_type} ../../Telegram/Telegram.pro
      awk '$1 == "PRE_TARGETDEPS" { $1=$2="" ; print }' "$srcdir"/tdesktop/Telegram/Telegram.pro | xargs xvfb-run -a make
    fi
    qmake CONFIG+=${_type} ../../Telegram/Telegram.pro
    xvfb-run -a make
  done
}

package() {
  install -dm755 "$pkgdir"/usr/bin
  install -Dm755 "$srcdir"/tdesktop/Linux/Release/Telegram "$pkgdir"/usr/bin/telegram
}
md5sums=('828594c91ba736ce2cd3e1e8a6146452'
         'SKIP')
