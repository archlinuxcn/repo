# Maintainer: XavierCLL <xavier.corredor.llano (a) gmail.com>

pkgname=pycharm-professional
pkgver=2020.2.0
_pkgver=2020.2
pkgrel=1
pkgdesc="Python IDE for Professional Developers. Professional Edition"
arch=('x86_64')
url='https://www.jetbrains.com/pycharm/'
conflicts=('pycharm' 'pycharm-community-edition')
provides=('pycharm')
license=('custom')
backup=(
    "opt/$pkgname/bin/pycharm.vmoptions"
    "opt/$pkgname/bin/pycharm64.vmoptions"
    "opt/$pkgname/bin/idea.properties"
)
depends=('giflib' 'glibc' 'sh' 'libxtst' 'libxslt' 'python' 'libdbusmenu-glib')
source=("https://download.jetbrains.com/python/$pkgname-$_pkgver.tar.gz"
        "pycharm-professional.desktop"
        "charm.desktop"
        "charm")
# https://download.jetbrains.com/python/pycharm-professional-${_pkgver}.tar.gz.sha256
sha256sums=('5301e54af750d45bd53456c8330b76e5ce92977b75be45436587f930d4b20077'
            'aaf7113e8c56e4d977eca204d57350d9493eda2710abefd2488a2b5d47c53344'
            'b026ef96831448be743f86e7e44bfa676629e8c3eb418c893fd87515c06263a7'
            '36068b05bebafa9aad6f043745f7764ed108c99f7b8f74cea2163da56bd2bc0c')
makedepends=('python-setuptools')
optdepends=('python2: Python 2 support'
            'ipython2: For enhanced interactive Python shell v2 inside Pycharm'
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
            'python-tox: Python environments for testing tool with Python 3'
            'jupyter: For support Jupyter Notebook'
            'python-docutils-stubs: For build documentation with sphynx')
            
build() {
  cd "pycharm-$_pkgver"

  # compile PyDev debugger used by PyCharm to speedup debugging
  python plugins/python/helpers/pydev/setup_cython.py build_ext --build-temp build --build-lib .
  
  rm -r bin/fsnotifier lib/pty4j-native/linux/{x86,ppc64le}
}

package() {
  # workaround FS#40934
  sed -i "s/lcd/on/" "pycharm-$_pkgver/bin/"*.vmoptions

  # base
  install -dm 755 "$pkgdir/opt/$pkgname"
  cp -dr --no-preserve=ownership "pycharm-$_pkgver/"* "$pkgdir/opt/$pkgname/"
  install -dm 755 "$pkgdir/usr/share/"{applications,pixmaps}
  install -Dm 644 "$pkgdir/opt/$pkgname/bin/pycharm.png" "$pkgdir/usr/share/pixmaps/pycharm.png"
  install -Dm 644 pycharm-professional.desktop "$pkgdir/usr/share/applications/"
  
  # exec
  install -dm 755 "$pkgdir/usr/bin/"
  ln -s /opt/pycharm-professional/bin/pycharm.sh "$pkgdir/usr/bin/pycharm"
  
  # licenses
  install -dm 755 "$pkgdir/usr/share/licenses/$pkgname/"
  cp -dr --no-preserve=ownership "pycharm-$_pkgver/license/"* "$pkgdir/usr/share/licenses/$pkgname/"
  
  # install charm application - for edit a single file in Pycharm
  install -Dm 755 charm "$pkgdir/usr/bin/"
  install -Dm 644 charm.desktop "$pkgdir/usr/share/applications/"
}
