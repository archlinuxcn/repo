# Maintainer: Christopher Arndt <aur -at- chrisarndt -dot- de>
# Contributor: Lukas Jirkovsky <l.jirkovsky@gmail.com>

_pkgname=makehuman
pkgname="${_pkgname}-hg"
pkgver=1.2.0.r2134.deca8874422d
pkgrel=1
pkgdesc="Parametrical modeling program for creating human bodies"
arch=('any')
url="http://www.makehuman.org/"
depends=('python2-numpy' 'python2-pyqt4' 'python2-opengl')
makedepends=('mercurial')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
license=('AGPL3')
source=("${_pkgname}::hg+https://bitbucket.org/MakeHuman/makehuman" \
        "${_pkgname}.desktop"
        "${_pkgname}.sh")
md5sums=('SKIP'
         'f54fdfbc6c783effc4624808d2547563'
         '4170c53c5ca07baf0ef0e423fbef6f74')


pkgver() {
  cd "$srcdir/${_pkgname}"

  local ver="$(grep '^__version__' makehuman/makehuman.py | cut -d \" -f 2 )"
  local rev=$(hg identify -n | sed 's/\+$//')
  local hash=$(hg identify -i | sed 's/\+$//')
  echo "${ver}.r${rev}.${hash}"
}

prepare() {
  cd "$srcdir/${_pkgname}"

  # make sure that we are using python2
  find . -type f -name "*.py" -exec sed -i 's/^#!.*python$/&2/' '{}' ';'
  sed -i 's|python"|python2"|' buildscripts/build_prepare.py

  rm -rf "$srcdir/build"
}

build() {
  cd "$srcdir/${_pkgname}/buildscripts"
  python2 build_prepare.py "$srcdir/${_pkgname}" "$srcdir/build"

  cd "$srcdir/build/${_pkgname}"
  # make sure that we are using python2 once again, because the build_prepare.py may have donwloaded some new files
  find . -type f -name "*.py" -exec sed -i 's/^#!.*python$/&2/' '{}' ';'
  # compile all modules so that they can be tracked by pacman
  python2 -m compileall .
  # and also optimize them
  python2 -OO -m compileall .
}

package() {
  install -d -m755 "$pkgdir/usr/share"
  cp -a "$srcdir/build/${_pkgname}" "$pkgdir/usr/share"

  install -D -m644 "$srcdir/build/${_pkgname}/icons/makehuman.png" \
    "$pkgdir/usr/share/pixmaps/makehuman.png"
  install -D -m755 "$srcdir/${_pkgname}.sh" "$pkgdir/usr/bin/${_pkgname}"
  install -D -m644 "$srcdir/${_pkgname}.desktop" \
    "$pkgdir/usr/share/applications/${_pkgname}.desktop"
}
