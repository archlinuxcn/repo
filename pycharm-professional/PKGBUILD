# Maintainer: XavierCLL <xavier.corredor.llano (a) gmail.com>

pkgname=pycharm-professional
pkgver=2018.2.2
_pkgver=2018.2.2
pkgrel=1
pkgdesc="Powerful Python and Django IDE. Professional edition."
arch=('x86_64')
url='http://www.jetbrains.com/pycharm/'
conflicts=('pycharm' 'pycharm-community')
provides=('pycharm')
license=('custom')
install=${pkgname}.install
backup=(opt/$pkgname/bin/pycharm.vmoptions opt/$pkgname/bin/pycharm64.vmoptions)
depends=('gcc-libs' 'giflib' 'glibc' 'sh' 'ttf-font' 'libxtst' 'libxslt')
source=(https://download.jetbrains.com/python/$pkgname-$_pkgver.tar.gz
        'pycharm-professional.desktop'
        'pycharm-professional.install'
        'pycharm'
        'charm.desktop'
        'charm')
# https://download.jetbrains.com/python/pycharm-professional-${_pkgver}.tar.gz.sha256
sha256sums=('e7ce851728c411ff2112b82bfabbcb8d20d0433a8d7ce06887588cb278f8c8b1'
            '016db1860a8b36d408c827f90aeb04b9d55cf21ea36788a9d8510cc54fae1c49'
            'fecb420a4644255cfbb486c1c82644e17e523bb61707108689f4fb702549d0eb'
            '54603a788b4ecad5d0a92e5b7fe37a98979250d2b5fd7d037759b4254b0b1607'
            'e1cf2a280d90a55710131bdf33f4026a427d10131ddd5c776a936ee1ecf5a6fb'
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
