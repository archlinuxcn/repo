# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>

pkgname=anaconda
pkgver=4.1.0
pkgrel=1
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=('x86' 'x86_64')
url="https://store.continuum.io/cshop/anaconda/"
license=("custom")
makedepends=('patch')
source=("http://repo.continuum.io/archive/Anaconda3-${pkgver}-Linux-x86_64.sh"
        "installer_sh_x86.patch"
        "installer_sh_x86_64.patch"
        "conda_install.patch")
options=(!strip libtool)
sha256sums=('11d32cf4026603d3b327dc4299863be6b815905ff51a80329085e1bb9f96c8bd'
            '426112c7adc263420b5a4419a11c455e93df23033d6a700f56142eae9108eb2d'
            '153769574abc0bad758a1eeb8efb215fec0afa40bd0fe303af52f894984b2c77'
            '7f6f9736f74b42dc0086b05f55898b56746bbd122a113496d2475c646a8ace9c')
_pythonver='3.5.1-5'
_condaver='4.1.4'

_pkgarch=`uname -m`
if [ "$CARCH" == "x86" ]; then
    _pkgarch="x86"
    sha256sums[0]='7764093f337a43e4962b12d01508c1a385f0f62c1ddc006b69af95ae763fc4c2'
    source[0]="http://repo.continuum.io/archive/Anaconda3-${pkgver}-Linux-x86.sh"
fi

prepare() {
    cd ${srcdir}
    patch --follow-symlinks -p1 < installer_sh_${_pkgarch}.patch
}

package() {
    prefix=${pkgdir}/opt/${pkgname}
    bash ${srcdir}/Anaconda3-${pkgver}-Linux-${_pkgarch}.sh -b -p $prefix
    [ "$BREAK_EARLY" = 1 ] && exit 1
    cd $prefix
    patch -p1 < $srcdir/conda_install.patch
    CONDA_INSTALL="$prefix/pkgs/conda-${_condaver}-py35_0/lib/python3.5/site-packages/conda/install.py"
    $prefix/pkgs/python-${_pythonver}/bin/python -E -s $CONDA_INSTALL --prefix=$prefix --instdir=/opt/${pkgname} --file=conda-meta/.ilan || exit 1
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
