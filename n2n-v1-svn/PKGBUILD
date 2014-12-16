# Contributor: Martin Lukeš <martin.meridius@gmail.com>
pkgname=n2n-v1-svn
pkgver=7144
pkgrel=3
pkgdesc='This is n2n v1! n2n is a layer-two peer-to-peer virtual private network (VPN) which allows users to exploit features typical of P2P applications at network instead of application level.'
arch=('i686' 'x86_64')
url="http://www.ntop.org/products/n2n/"
license=('GPL3')
makedepends=('subversion')
provides=('n2n-v1')
conflicts=('n2n-v1')
install='n2n-v1.install'
_svntrunk=https://svn.ntop.org/svn/ntop/trunk/n2n
_svnmod=n2n

build() {
  cd "$srcdir"

  if [ -d $_svnmod/.svn ]; then
    (cd $_svnmod && svn up -r $pkgver)
  else
    svn co $_svntrunk --config-dir ./ $_svnmod
  fi

  msg "SVN checkout done or server timeout"

  rm -rf "$srcdir/$_svnmod-build"
  cp -r "$srcdir/$_svnmod" "$srcdir/$_svnmod-build"
  cd "$srcdir/$_svnmod-build/n2n_v1"

  msg "Altering program names..."
  find . -type f -print0 | xargs -0 sed -i 's/supernode/supernodev1/g'
  find . -type f -print0 | xargs -0 sed -i 's/edge/edgev1/g'

  mv ./edge.8 ./edgev1.8
  mv ./supernode.1 ./supernodev1.1
  mv ./supernode.c ./supernodev1.c
  mv ./edge.c ./edgev1.c
  mv ./win32/DotNet/supernode ./win32/DotNet/supernodev1
  mv ./win32/DotNet/supernodev1/supernode.vcproj ./win32/DotNet/supernodev1/supernodev1.vcproj

  #
  # BUILD
  #

  msg "Starting make..."
  make
}

package() {
  cd "$srcdir/$_svnmod-build/n2n_v1"
  make PREFIX="$pkgdir/usr/" install
}

