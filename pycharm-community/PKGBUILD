# Contributor: David Keogh <davekeogh@archlinux.us>

pkgname=pycharm-community
pkgver=2017.2.3
pkgrel=1
pkgdesc="Powerful Python and Django IDE. Community edition."
arch=('i686' 'x86_64')
options=('!strip')
url="http://www.jetbrains.com/pycharm/"
license=('Apache')
depends=('giflib' 'ttf-font')
optdepends=('ipython2: IPython integration for Python 2'
            'ipython: IPython integration for Python 3')
makedepends=('python2-setuptools' 'python-setuptools')
conflicts=('pycharm' 'pycharm-professional')
provides=('pycharm')
source=(https://download.jetbrains.com/python/$pkgname-$pkgver.tar.gz
        'pycharm-community.desktop' )
sha256sums=('4eacc9bf512406bebf71546ccb4b6c14ea8e06748fd76be6ca409ea1955e1f53'
            '5ce44b5bee632258749ee7d0df0fd08af446d43715f9ef50cb6889b88232de41')

build() {
  # compile PyDev debugger used by PyCharm to speedup debugging
  python2 $srcdir/$pkgname-$pkgver/helpers/pydev/setup_cython.py build_ext --inplace
  python3 $srcdir/$pkgname-$pkgver/helpers/pydev/setup_cython.py build_ext --inplace
}

package() {
  cd $srcdir
  mkdir -p $pkgdir/opt/$pkgname
  cp -R $srcdir/$pkgname-$pkgver/* $pkgdir/opt/$pkgname

  if [[ $CARCH = 'i686' ]]; then
    rm -f $pkgdir/opt/$pkgname/bin/libyjpagent-linux64.so
    rm -f $pkgdir/opt/$pkgname/bin/fsnotifier64
  fi

  mkdir -p $pkgdir/usr/share/{applications,pixmaps}
  install -Dm644 $srcdir/pycharm-community.desktop $pkgdir/usr/share/applications/
  install -Dm644 $pkgdir/opt/$pkgname/bin/pycharm.png $pkgdir/usr/share/pixmaps/pycharm.png

  mkdir -p $pkgdir/usr/bin
  ln -s /opt/pycharm-community/bin/pycharm.sh $pkgdir/usr/bin/pycharm
}

# vim:set ts=2 sw=2 et:
sha256sums=('e8562938c2ede32a1c1036391942190144cd9f0927bd49b6b3ddf5f7a01c33aa'
            '5ce44b5bee632258749ee7d0df0fd08af446d43715f9ef50cb6889b88232de41')
