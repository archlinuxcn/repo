# Maintainer: XavierCLL <xavier.corredor.llano (a) gmail.com>

pkgname=pycharm-professional
pkgver=2016.2.1
pkgrel=1
pkgdesc="Powerful Python and Django IDE. Professional edition."
arch=('any')
options=('!strip')
url="http://www.jetbrains.com/pycharm/"
conflicts=('pycharm' 'pycharm-community')
provides=('pycharm')
license=('custom')
install=${pkgname}.install
depends=('java-runtime-common' 'java-runtime>=8' 'ttf-font' 'libxtst' 'libxslt')
source=(https://download.jetbrains.com/python/$pkgname-$pkgver-no-jdk.tar.gz
        'pycharm-professional.desktop'
        'pycharm-professional.install'
        'pycharm'
        'charm.desktop'
        'charm')
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
            'python-tox: Python environments for testing tool with Python 3')
sha256sums=('670679b1f08ec12cab35195a3a4faa22347188e032e4d76378936899b5368604'
            '016db1860a8b36d408c827f90aeb04b9d55cf21ea36788a9d8510cc54fae1c49'
            'c1a74303d9e870918bd8068f761c8251b996694b1b96b3537fbca317679c4958'
            '43e79e5a786fc76385634dc0a9f1c3489b25031745b840b0822b059fc91d1060'
            'a90a2b645e733627fefe568ae82fc96716772c13b4431760a822c0c64b0596e9'
            'dbe4055a0e4980dba5c5104b6a9ec30a3e429e4e3ef5ef92efef2627403e7ac5')

package() {
  # base
  cd $srcdir
  install -dm 755 $pkgdir/opt/$pkgname
  cp -dr --no-preserve=ownership $srcdir/pycharm-$pkgver/* $pkgdir/opt/$pkgname
  install -dm 755 $pkgdir/usr/share/{applications,pixmaps}
  install -dm 755 $pkgdir/usr/bin/
  install -Dm 644 $pkgdir/opt/$pkgname/bin/pycharm.png $pkgdir/usr/share/pixmaps/pycharm.png
  
  # licenses
  install -dm 755 $pkgdir/usr/share/licenses/$pkgname/
  cp -dr --no-preserve=ownership $srcdir/pycharm-$pkgver/license/* $pkgdir/usr/share/licenses/$pkgname
  
  # exec
  install -Dm 755 pycharm $pkgdir/usr/bin/
  
  # app file desktop
  install -Dm 644 pycharm-professional.desktop $pkgdir/usr/share/applications/
  
  # install charm application - for edit a single file in Pycharm
  install -Dm 755 charm $pkgdir/opt/pycharm-professional/bin/
  install -Dm 644 charm.desktop $pkgdir/usr/share/applications/
  
  # delete some conflicts files for i686 
  if [[ $CARCH = 'i686' ]]; then
    rm -f $pkgdir/opt/$pkgname/bin/libyjpagent-linux64.so
    rm -f $pkgdir/opt/$pkgname/bin/fsnotifier64
  fi
  
}
