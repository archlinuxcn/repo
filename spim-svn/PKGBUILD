pkgname=spim-svn
pkgver=711
pkgrel=1
pkgdesc="A MIPS32 simulator (SVN version)"
arch=('i686' 'x86_64')
url="https://sourceforge.net/projects/spimsimulator/"
license=('custom:BSD')
groups=('emulators')
depends=('glibc')
makedepends=('subversion')
conflicts=('spim')
provides=('spim')

_svntrunk='svn+https://svn.code.sf.net/p/spimsimulator/code'
source=("${_svntrunk}/spim"
        "${_svntrunk}/CPU")
md5sums=('SKIP'
         'SKIP')

pkgver() {
  cd "${srcdir}/spim"
  local ver="$(svnversion)"
  printf "${ver//[[:alpha:]]}"
}

build() {
  cd ${srcdir}/spim

  make
}

package() {
  install -Dm644 ${srcdir}/spim/README ${pkgdir}/usr/share/licenses/${pkgname}/README

  cd ${srcdir}/spim
  install -dDm755 ${pkgdir}/usr/bin
  make DESTDIR=${pkgdir} install
}
