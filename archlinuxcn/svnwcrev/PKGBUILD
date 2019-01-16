# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=svnwcrev
pkgdesc='Incorporate Subversion repository information into your source'
pkgver=r18
pkgrel=1
url='http://svnwcrev.tigris.org/'
arch=('i686' 'x86_64')
source=(fix-ldflags.patch)
sha256sums=('91b77d5cc64899382953100fd223d0c23c9f241f7ef41079570372b71a764334')
depends=('subversion')
license=('GPL')

prepare() {
  _svnargs="--username guest --password '' --no-auth-cache -r $pkgver"
  if [ -d $pkgname/.svn ] ; then
    cd $pkgname
    svn up $_svnargs
  else
    svn co http://svnwcrev.tigris.org/svn/svnwcrev/trunk/svnwcrev $_svnargs
    cd $pkgname
  fi

  patch -Np0 -i ../fix-ldflags.patch

  cp config_mk.template config.mk

  sed -i 's#apr-0#apr-1#' config.mk
}

build() {
  cd $pkgname

  touch src/version.h  # due to a Makefile bug
  make src/version.h
  make
}

package() {
  cd $pkgname

  install -Dm755 svnwcrev "$pkgdir"/usr/bin/svnwcrev
}
