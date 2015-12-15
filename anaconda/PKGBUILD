# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>

pkgname=anaconda
pkgver=2.4.1
pkgrel=3
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
sha256sums=('0735e69199fc37135930ea2fd4fb6ad0adef215a2a7ba9fd6b0a0a4daaadb1cf'
            '30859478b4974d61077f921c00020f2e2d5340a262302de8a0bee8369cec3014'
            '386b289912d4e2a6d0cf9d436922de09b5a801d95d3acc421f1638380b3628d4'
            '906f21f96c5d5d086a03761824cb8f2043d0491604d8abc5481412495b912cc5')
_pythonver='3.5.1-0'
_condaver='3.18.8'

_pkgarch=`uname -m`
if [ "$CARCH" == "x86" ]; then
    _pkgarch="x86"
    sha256sums[0]='00d13413f5b8129e863dabcc2296a181c697056c5ed210739a0aa06454ab7038'
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
    $prefix/pkgs/python-${_pythonver}/bin/python -E $CONDA_INSTALL --prefix=$prefix --instdir=/opt/${pkgname} --pkgs-dir=$prefix/pkgs --link-all || exit 1
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
