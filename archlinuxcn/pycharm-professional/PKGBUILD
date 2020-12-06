# Maintainer: XavierCLL <xavier.corredor.llano (a) gmail.com>

pkgname=pycharm-professional
pkgver=2020.3
pkgrel=4
pkgdesc="Python IDE for Professional Developers. Professional Edition"
arch=('x86_64')
url='https://www.jetbrains.com/pycharm/'
conflicts=('pycharm' 'pycharm-community-edition')
provides=('pycharm')
license=('custom')
backup=("opt/$pkgname/bin/pycharm.vmoptions"
        "opt/$pkgname/bin/pycharm64.vmoptions"
        "opt/$pkgname/bin/idea.properties")
depends=('giflib' 'glibc' 'sh' 'libxtst' 'libxslt' 'python' 'libdbusmenu-glib')
source=("https://download.jetbrains.com/python/$pkgname-$pkgver.tar.gz"
        "pycharm-professional.desktop"
        "charm.desktop"
        "charm")
sha256sums=('a099d0aefa9e6a2e8507e0f89feb48f5839f529f21649393e22f52f641f2efcf'
            '4547368ae3af428bb6c18edad0cb11e2578b28512b7bf1ab9513c154dd24a0a3'
            'f8b5390d334de089ee6d1d87a0cfd8e502aa897f10361ba31a7ebc3f3cac3270'
            'e3b2e7996a7571d659b9477f950ea935e8088c302f6d1e1f6cb5d803f1d10113')
makedepends=('python-setuptools' 'cython')
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
            'jupyter: For support Jupyter Notebook')
            
build() {
    # compile PyDev debugger used by PyCharm to speedup debugging
    find pycharm-${pkgver}/plugins/python/helpers/pydev/ \( -name *.c -o -name *.so -o -name *.pyd \) -delete
    sed -i '1s/^/# cython: language_level=3\n/' pycharm-${pkgver}/plugins/python/helpers/pydev/_pydevd_bundle/pydevd_cython.pxd
    python pycharm-${pkgver}/plugins/python/helpers/pydev/setup_cython.py build_ext --inplace --force-cython
    rm -rf pycharm-${pkgver}/plugins/python/helpers/pydev/build/
    find pycharm-${pkgver}/plugins/python/helpers/pydev/ -name __pycache__ -exec rm -rf {} \;
    
    rm -r pycharm-${pkgver}/lib/pty4j-native/linux/{mips64el,ppc64le,aarch64}
}

package() {
    # workaround FS#40934
    sed -i "s/lcd/on/" "pycharm-$pkgver/bin/"*.vmoptions
    
    # licenses
    install -dm 755 "$pkgdir/usr/share/licenses/$pkgname/"
    mv "pycharm-$pkgver/license/"* "$pkgdir/usr/share/licenses/$pkgname/"
    
    # base
    install -dm 755 "$pkgdir/opt/$pkgname"
    mv "pycharm-$pkgver/"* "$pkgdir/opt/$pkgname/"
    install -dm 755 "$pkgdir/usr/share/"{applications,pixmaps}
    install -Dm 644 "$pkgname.desktop" "$pkgdir/usr/share/applications/"
    ln -s "/opt/$pkgname/bin/pycharm.svg" "$pkgdir/usr/share/pixmaps/pycharm.svg"

    # exec
    install -dm 755 "$pkgdir/usr/bin/"
    ln -s "/opt/$pkgname/bin/pycharm.sh" "$pkgdir/usr/bin/pycharm"

    # install charm application - for edit a single file in Pycharm
    install -Dm 755 charm "$pkgdir/usr/bin/"
    install -Dm 644 charm.desktop "$pkgdir/usr/share/applications/"
}
