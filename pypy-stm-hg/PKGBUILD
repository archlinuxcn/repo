# $Id: PKGBUILD 95035 2013-08-04 09:44:24Z svenstaro $
# Maintainer: Sven-Hendrik Haase <sh@lutzhaase.com>

#_hgrev=63547

pkgname=pypy-stm-hg
#pkgver=2.1beta1
#_pkgver=2.1-beta1
#[[ -n $_hgrev ]] && pkgver=2.0beta2.$_hgrev
pkgrel=1
pkgver=r77701.905ab5c077a5
pkgdesc="A Python implementation written in Python, STM branch, hg version"
url="http://pypy.org/tmdonate2.html"
arch=('i686' 'x86_64')
depends=('libffi')
provides=('pypy-stm')
conflicts=('pypy-stm')
options=(!buildflags)
makedepends=('python' 'mercurial' 'pypy' 'tk' 'clang-pypy-stm' 'llvm-pypy-stm')
optdepends=('openssl: openssl module'
            'expat: pyexpat module'
            'ncurses: ncurses module'
            'zlib: zlib module'
            'bzip2: bz2 module'
            'tk: tk module')
license=('custom:MIT')
source=("hg+https://bitbucket.org/pypy/pypy#branch=stmgc-c7")
md5sums=('SKIP')

pkgver() {
  #set -xv
  cd "$srcdir/pypy"
  printf "r%s.%s" "$(hg identify -n)" "$(hg identify -i)"
}

build() {
  cd "${srcdir}"/pypy/pypy/goal

  pypy ../../rpython/bin/rpython -Ojit --stm targetpypystandalone
}

package() {
  cd "${srcdir}"/pypy/pypy/tool/release

  LD_LIBRARY_PATH=../../goal/ python2 package.py ../../../ pypy-stm pypy-c "${srcdir}"/${pkgname}.tar.bz2

  mkdir -p "${pkgdir}"/opt
  tar x -C "${pkgdir}"/opt -f "${srcdir}"/${pkgname}.tar.bz2

  #mkdir -p "${pkgdir}"/opt/pypy-stm/lib
  #cp ../../goal/libpypy-c.so "${pkgdir}"/opt/pypy-stm/lib/

  mkdir -p "${pkgdir}"/usr/bin
  ln -s /opt/pypy-stm/bin/pypy-c "${pkgdir}"/usr/bin/pypy-stm

  install -Dm644 "${pkgdir}"/opt/pypy-stm/LICENSE "${pkgdir}"/usr/share/licenses/pypy-stm/LICENSE
}

