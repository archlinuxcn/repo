# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>

pkgname=anaconda
pkgver=2.4.0
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
sha256sums=('fb4e480059e991f2fa632b5a9bcdd284c7f0677814cd719c11d524453f96a40d'
            'e5110519a6977fc0636fb94148d1b7bc070167cda3402d4a2cdecd7dbb4eca08'
            'fe62ec395b9346f721a8ad7f73bb1c98cb8ce65de06e9aeef3be99c5e040364b'
            '2cc1cfc80f8255dd4b350a6645ebf23c445cb0e82bee40e5a3bf8d0812e39e44')
_pythonver='3.5.0-1'
_condaver='3.18.3'

_pkgarch=`uname -m`
if [ "$CARCH" == "x86" ]; then
    _pkgarch="x86"
    sha256sums[0]='f6080c6493cefc603cfeb67aaf6c3c4c6b80a66788f03db48ffd3cfa52017c0a'
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
