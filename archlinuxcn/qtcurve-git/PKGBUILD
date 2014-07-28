# Maintainer: Yichao Yu <yyc1992@gmail.com>

pkgname=qtcurve-git
_realver=1.8.18
pkgver=1.8.18.26.g9af8b72
pkgrel=1
pkgdesc='A configurable set of widget styles for KDE and Gtk.'
arch=('i686' 'x86_64')
url="https://github.com/QtCurve/qtcurve"
license=('GPL')
groups=('qtcurve')
depends=('qt5-base' 'qt5-svg' 'libxcb' 'qt5-x11extras'
  'kdebase-workspace' 'gtk2' 'libx11' 'gcc-libs')
makedepends=('cmake' 'automoc4' 'git')
provides=(
  "qtcurve-utils=${_realver}"
  "qtcurve-gtk2=${_realver}"
  "qtcurve-kde4=${_realver}"
  "qtcurve-qt4=${_realver}"
  "qtcurve-qt5=${_realver}"
  "qtcurve-utils-git"
  "qtcurve-gtk2-git"
  "qtcurve-kde4-git"
  "qtcurve-qt4-git"
  "qtcurve-qt5-git")
conflicts=("qtcurve-kde4" "qtcurve-qt4"
  "qtcurve-qt5" "qtcurve-gtk2" "qtcurve-utils")
options=('debug' 'strip')

_gitname="qtcurve"

_gitroot="git://anongit.kde.org/qtcurve.git"
_gitref=master

_fetch_git() {
  cd "$srcdir"

  if [ -d "$srcdir/$_gitname/.git" ]; then
    cd "$_gitname"
    msg "Reset current branch"
    git reset --hard HEAD
    git clean -fdx
    msg "Fetching branch $_gitref from $_gitroot..."
    git fetch --force --update-head-ok \
      "$_gitroot" "$_gitref:$_gitref" --
    msg "Checking out branch $_gitref..."
    git checkout "$_gitref" --
    git reset --hard "$_gitref"
    git clean -fdx
    msg "The local files are updated."
  else
    msg "Cloning branch $_gitref from $_gitroot to $_gitname..."
    git clone --single-branch --branch "$_gitref" \
      "$_gitroot" "$_gitname"
    cd "$_gitname"
  fi
  msg "GIT checkout done or server timeout"
}

pkgver() {
  local outfile=/dev/null
  [[ -e /dev/tty ]] && outfile=/dev/tty
  (_fetch_git &> ${outfile})
  cd "$srcdir/$_gitname"

  git describe | sed -e 's/-/./g'
}

build() {
  (_fetch_git)
  cd "$srcdir/$_gitname"

  mkdir -p build
  cd build

  cmake .. \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DQT_QMAKE_EXECUTABLE=qmake-qt4 \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DQTC_KDE4_PREFIX=/usr
  make
}

package() {
  cd "$srcdir/$_gitname/build"

  make DESTDIR="$pkgdir/" install
}
