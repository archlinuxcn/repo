# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=python-leveldb
pkgver=0.201
pkgrel=4
pkgdesc='Python bindings for leveldb database library'
arch=('x86_64')
url='https://github.com/rjpower/py-leveldb/'
license=('BSD-3-Clause')
depends=('python')
makedepends=('git' 'python-build' 'python-installer' 'python-setuptools' 'python-wheel')
checkdepends=('python-nose')
source=("git+https://github.com/rjpower/py-leveldb.git#tag=${pkgver}"
        'git+https://github.com/google/leveldb.git'
        '010-python-leveldb-replace-deprecated-unicode-api.patch'::'https://github.com/rjpower/py-leveldb/pull/13.patch')
sha256sums=('118c1e275891a41832aebc16a3eb22d946b337e555c8e92b877957df4c153534'
            'SKIP'
            'd65bd3b20e0ea7e637337e07212d828a0438b2b1e9b7c54c9936de13b58dba2c')

prepare() {
    git -C py-leveldb submodule init
    git -C py-leveldb config --local submodule.leveldb.url "${srcdir}/leveldb"
    git -C py-leveldb -c protocol.file.allow='always' submodule update
    
    patch -d py-leveldb -Np1 -i "${srcdir}/010-python-leveldb-replace-deprecated-unicode-api.patch"
}

build() {
    cd py-leveldb
    python -m build --wheel --no-isolation
}

check() {
    local _pyver
    _pyver="$(python -c 'import sys; print("%s.%s" %sys.version_info[0:2])')"
    cd py-leveldb
    PYTHONPATH="$(pwd)/build/lib.linux-${CARCH}-cpython-${_pyver/./}" nosetests
}

package() {
    python -m installer --destdir="$pkgdir" py-leveldb/dist/*.whl
    
    local _sitepkgs
    local _sitepkgs=$(python -c "import site; print(site.getsitepackages()[0])")
    install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "../../../${_sitepkgs/\/usr\//}/leveldb-${pkgver::-1}.dist-info/LICENSE" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
