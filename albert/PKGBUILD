# Maintainer: Manuel Schneider  <manuelschneid3r at googles mail>
pkgname=albert
pkgver=0.16.0
pkgrel=1
pkgdesc="A sophisticated standalone keyboard launcher."
arch=('i686' 'x86_64' 'armv7h')
url="https://github.com/albertlauncher"
license=('GPL')
depends=(
  'qt5-charts'
  'qt5-graphicaleffects'
  'qt5-quickcontrols'
  'qt5-svg'
  'qt5-x11extras'
  'libx11'
)
makedepends=(
  'cmake'
  'gcc'
  'git'
  'muparser'
  'python'
  'qt5-declarative'
  'qt5-svg'
  'virtualbox'
  'virtualbox-sdk'
)
optdepends=(
  'muparser: Calculator plugin'
  'python: Python extension'
  'virtualbox: VirtualBox plugin'
)
#source=("mirrors/albert::git+https://github.com/albertlauncher/albert.git#branch=dev"
source=("mirrors/albert::git+https://github.com/albertlauncher/albert.git#tag=v${pkgver}"
        "mirrors/plugins::git+https://github.com/albertlauncher/plugins.git"
        "mirrors/python::git+https://github.com/albertlauncher/python.git"
        "mirrors/pybind11::git+https://github.com/pybind/pybind11.git")
md5sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')


prepare() {

  cd "$srcdir/albert"
  git submodule init
  git config submodule.plugins.url "$srcdir/plugins"
  git submodule update plugins

  cd "$srcdir/albert/plugins"
  git submodule init
  git config submodule.python/pybind11.url $srcdir/pybind11
  git config submodule.python/share/modules.url $srcdir/python
  git submodule update python/pybind11 python/share/modules

}


build() {
  echo -e "

   ╭──────────────────────────────────────────────╮
   │                                              │
   │      \e[31mThis is a plugin based application\e[0m      │
   │       \e[31mCheck the optional dependencies\e[0m        │
   │                                              │
   │   If you plan to report bugs please modify   │
   │   the PKGBUILD to build the debug version.   │
   │                                              │
   ╰──────────────────────────────────────────────╯
"

  [[ -d "build" ]] || mkdir -p "build"
  cd "build"

  # https://ptpb.pw/_dFp
  cmake \
    "../${pkgname}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_BUILD_TYPE="RelWithDebInfo  " \
    -Wno-dev

    # Maybe you want to add some of those
    # but remember to adjust the dependencies

    #-DCMAKE_BUILD_TYPE="Debug"
    #-DBUILD_WIDGETBOXMODEL=ON
    #-DBUILD_QMLBOXMODEL=ON
    #-DBUILD_APPLICATIONS=ON
    #-DBUILD_CALCULATOR=ON
    #-DBUILD_CHROMEBOOKMARKS=ON
    #-DBUILD_EXTERNALEXTENSIONS=ON
    #-DBUILD_DEBUG=OFF
    #-DBUILD_FILES=ON
    #-DBUILD_FIREFOXBOOKMARKS=ON
    #-DBUILD_HASHGENERATOR=ON
    #-DBUILD_KVSTORE=ON
    #-DBUILD_MPRIS=ON
    #-DBUILD_PYTHON=ON
    #-DBUILD_SSH=ON
    #-DBUILD_SYSTEM=ON
    #-DBUILD_TEMPLATE=OFF
    #-DBUILD_TERMINAL=ON
    #-DBUILD_VIRTUALBOX=ON

  #VERBOSE=1 make
  make
}


package() {
  cd "${srcdir}/build"
  make DESTDIR="$pkgdir/" install
}

# vim:set ts=2 sw=2 et:
