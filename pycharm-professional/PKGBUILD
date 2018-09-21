# Maintainer: XavierCLL <xavier.corredor.llano (a) gmail.com>

pkgname=pycharm-professional
pkgver=2018.2.4
_pkgver=2018.2.4
pkgrel=1
pkgdesc="Powerful Python and Django IDE. Professional Edition."
arch=('x86_64')
url='http://www.jetbrains.com/pycharm/'
conflicts=('pycharm' 'pycharm-community')
provides=('pycharm')
license=('custom')
install=${pkgname}.install
backup=(opt/$pkgname/bin/pycharm.vmoptions opt/$pkgname/bin/pycharm64.vmoptions)
depends=('giflib' 'glibc' 'sh' 'ttf-font' 'libxtst' 'libxslt' 'python')
source=(https://download.jetbrains.com/python/$pkgname-$_pkgver.tar.gz
        'pycharm-professional.desktop'
        'pycharm-professional.install'
        'pycharm'
        'charm.desktop'
        'charm')
# https://download.jetbrains.com/python/pycharm-professional-${_pkgver}.tar.gz.sha256
sha256sums=('450d29fd039a8c93e895a6a0f45453255559d3ee54e08a76ee2cdc7b85b10493'
            'aaf7113e8c56e4d977eca204d57350d9493eda2710abefd2488a2b5d47c53344'
            '40b297ac1d883583ed5d7aae75fb09497a2af5bda9dd4aff83bd6d2892ab6c95'
            '818ed42f4200ae13315587abf6f247f93e68c658a94794f73924c985cdc145d0'
            '21e77b6b18e14636f9827e1f8d45bbc8dba8fb14ea5f4cde285c1ef4bb01c85e'
            '7e9bc3873f6c8039b4d7c181806ce4363632ff5811e966142749396cd849d86f')
makedepends=('python2-setuptools' 'python-setuptools')
optdepends=('ipython2: For enhanced interactive Python shell v2 inside Pycharm'
            'ipython: For enhanced interactive Python shell v3 inside Pycharm'
            'openssh: For deployment and remote connections'
            'python2-setuptools: Packages manager for Python 2, for project interpreter'
            'python-setuptools: Packages manager for Python 3, for project interpreter'
            'python2-coverage: For support code coverage measurement for Python 2'
            'python-coverage: For support code coverage measurement for Python 3'
            'cython2: For performance debugger in Python 2'
            'cython: For performance debugger in Python 3'
            'docker-machine: For support docker inside Pycharm'
            'docker-compose: For support docker inside Pycharm'
            'vagrant: For support virtualized development environments'
            'python2-pytest: For support testing inside Pycharm with Python 2'
            'python-pytest: For support testing inside Pycharm with Python 3'
            'python2-tox: Python environments for testing tool with Python 2'
            'python-tox: Python environments for testing tool with Python 3', 
            'jupyter: For support Jupyter Notebook')
            
build() {
  cd pycharm-$_pkgver

  # compile PyDev debugger used by PyCharm to speedup debugging
  python2 helpers/pydev/setup_cython.py build_ext --build-temp build --build-lib .
  python3 helpers/pydev/setup_cython.py build_ext --build-temp build --build-lib .
  
  rm -rf bin/fsnotifier{,-arm} lib/libpty/linux/x86
}

package() {
  # workaround FS#40934
  sed -i 's/lcd/on/' pycharm-$_pkgver/bin/*.vmoptions

  # base
  install -dm 755 $pkgdir/opt/$pkgname
  cp -dr --no-preserve=ownership pycharm-$_pkgver/* $pkgdir/opt/$pkgname
  install -dm 755 $pkgdir/usr/share/{applications,pixmaps}
  install -dm 755 $pkgdir/usr/bin/
  install -Dm 644 $pkgdir/opt/$pkgname/bin/pycharm.png $pkgdir/usr/share/pixmaps/pycharm.png
  
  # licenses
  install -dm 755 $pkgdir/usr/share/licenses/$pkgname/
  cp -dr --no-preserve=ownership pycharm-$_pkgver/license/* $pkgdir/usr/share/licenses/$pkgname
  
  # exec
  install -Dm 755 pycharm $pkgdir/usr/bin/
  
  # app file desktop
  install -Dm 644 pycharm-professional.desktop $pkgdir/usr/share/applications/
  
  # install charm application - for edit a single file in Pycharm
  install -Dm 755 charm $pkgdir/opt/pycharm-professional/bin/
  install -Dm 644 charm.desktop $pkgdir/usr/share/applications/
}
