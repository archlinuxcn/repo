# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>

pkgname=anaconda
pkgver=2.5.0
pkgrel=1
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=('x86' 'x86_64')
url="https://store.continuum.io/cshop/anaconda/"
license=("custom")
makedepends=('patch')
source=("https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-${pkgver}-Linux-x86_64.sh"
        "installer_sh_x86.patch"
        "installer_sh_x86_64.patch"
        "conda_install.patch")
options=(!strip libtool)
sha256sums=('addadcb927f15cb0b5b6e36890563d3352a8ff6a901ea753d389047d274a29a9'
            'eca56a7f01e418ae7f12634ffc288a1387a6ae93873ed4b669e4aaf59a2a0cd8'
            'e10e50ce51c88547f14a96c401ddde6bd4a9d9ea4a9aa863014e1248557e967a'
            'b7d1662b2ec3de934171df0216527324135e89932b12cd8949695322fbd5ba42')
_pythonver='3.5.1-0'
_condaver='3.19.1'

_pkgarch=`uname -m`
if [ "$CARCH" == "x86" ]; then
    _pkgarch="x86"
    sha256sums[0]='22ac26c8bde7c4153ea859f6f6d8aca93bbf1e213d800167ad5ea530c62959af'
    source[0]="https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-${pkgver}-Linux-x86.sh"
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
