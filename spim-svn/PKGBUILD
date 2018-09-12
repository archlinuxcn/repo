# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=spim-svn
pkgver=715
pkgrel=2
pkgdesc="A MIPS32 simulator (SVN version)"
arch=('i686' 'x86_64')
url="https://sourceforge.net/projects/spimsimulator/"
license=('custom:BSD')
groups=('emulators')
depends=('glibc')
makedepends=('subversion')
conflicts=('spim')
provides=("spim=$pkgver")

_svntrunk='svn+https://svn.code.sf.net/p/spimsimulator/code'
source=("$_svntrunk/spim"
        "$_svntrunk/CPU"
        "$_svntrunk/Tests"
        fix-install.patch)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            '36db36d77c49ae082c0cdf9c7dc46a3dd7a144747cecb60c2b149daa59a20af1')

pkgver() {
  cd spim

  local ver="$(svnversion)"
  printf "${ver//[[:alpha:]]}"
}

prepare() {
  cd spim

  patch -Np0 -i ../fix-install.patch
}

build() {
  cd spim

  make
}

check() {
  cd spim

  make test
}

package() {
  cd spim

  make DESTDIR="$pkgdir" install

  install -Dm644 README "$pkgdir"/usr/share/licenses/$pkgname/README
}
