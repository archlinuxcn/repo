# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>

pkgname=anaconda
pkgver=4.0.0
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
sha256sums=('36a558a1109868661a5735f5f32607643f6dc05cf581fefb1c10fb8abbe22f39'
            'dd816d1f60de23111e7ab7a276ea957268738464acfe25c474b37ef0cfe330e9'
            '155b7fc7f8e70b49ee44dee55f3b79543b99d4def4244d2d18da18f359a9dfef'
            '06dacb8460f32af0a057dfccd9c2349d6eb4c9d4e04b84e12ddc07c85eb561fd')
_pythonver='3.5.1-0'
_condaver='4.0.5'

_pkgarch=`uname -m`
if [ "$CARCH" == "x86" ]; then
    _pkgarch="x86"
    sha256sums[0]='e1469fa0d24de12f33661ce3d7a06d77968be8822f366a61a0018a3850ab56b0'
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
