# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>

pkgname=anaconda
pkgver=2.2.0
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
sha256sums=('4aac68743e7706adb93f042f970373a6e7e087dbf4b02ac467c94ca4ce33d2d1'
            'e304a2cbf3f6cddd80abc1a21488e6e20798ccdc714e999e68c24f937704ed4c'
            'e5f90b6210926704f110cbab0e57c8dd06ca05cbdf5e697a97ffbb184d35ea26'
            'de91d0b08d24f632c7d282ed6457ffe2e3d5ecab5967b8e3c000fcf5091e3711')
_pythonver='3.4.3-0'
_condaver='3.10.0'

_pkgarch=`uname -m`
if [ "$CARCH" == "i686" ]; then
    _pkgarch="x86"
    sha256sums[0]='223655cd256aa912dfc83ab24570e47bb3808bc3b0c6bd21b5db0fcf2750883e'
    source[0]="https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-${pkgver}-Linux-x86.sh"
fi

prepare() {
    cd ${srcdir}
    patch --follow-symlinks -p1 < installer_sh_${_pkgarch}.patch
}

package() {
    prefix=${pkgdir}/opt/${pkgname}
    bash ${srcdir}/Anaconda3-${pkgver}-Linux-${_pkgarch}.sh -b -p $prefix
    cd $prefix
    patch -p1 < $srcdir/conda_install.patch
    CONDA_INSTALL="$prefix/pkgs/conda-${_condaver}-py34_0/lib/python3.4/site-packages/conda/install.py"
    $prefix/pkgs/python-${_pythonver}/bin/python -E $CONDA_INSTALL --prefix=$prefix --instdir=/opt/${pkgname} --pkgs-dir=$prefix/pkgs --link-all || exit 1
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
