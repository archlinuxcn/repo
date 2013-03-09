# Maintainer: phoenixlzx <phoenixlzx[at]archlinuxcn[dot]org>

pkgname=libwebqq-git
pkgver=20121116
pkgrel=1
pkgdesc="This Project aims at implementation of web qq protocol with C++ back end and other language extended which used boost-python and swig for high level wrapping."
url="https://github.com/wxjeacen/libwebqqboost"
arch=('x86_64' 'i686')
license=('GPL')
depends=('curl' 'boost' 'python2' 'python2-simplejson')
options=(!strip)
source=()
md5sums=()

_gitroot=git://github.com/wxjeacen/libwebqqboost.git
_gitname=libwebqq

build()
{
  cd ${srcdir}
  msg "Connecting to the GIT server...."

  if [[ -d "$srcdir"/$_gitname ]] ; then
    cd $_gitname
    git pull origin
    msg "The local files are updated."
  else
    git clone $_gitroot $_gitname
    cd $_gitname
  fi

  git checkout $_BRANCH

  cmake -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package()
{
  cd "$srcdir/$_gitname/build"
  ##make DESTDIR="${pkgdir}" install
  mkdir -p ${pkgdir}/usr/lib/python2.7/
  install -Dm644 $srcdir/$_gitname/build/libwebqqboost.so "$pkgdir/usr/lib/python2.7/libwebqqboost.so"
}
