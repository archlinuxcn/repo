# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>
# Contributor : Jingbei Li <i@jingbei.li>

pkgname=anaconda
pkgver=4.4.0
pkgrel=2
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=('x86' 'x86_64')
url="https://store.continuum.io/cshop/anaconda/"
license=("custom")
makedepends=('patch')
source=("http://repo.continuum.io/archive/Anaconda3-${pkgver}-Linux-x86_64.sh"
        "install.py.patch"
        "$pkgname.install")
options=(!strip libtool staticlibs)
sha256sums=('3301b37e402f3ff3df216fe0458f1e6a4ccbb7e67b4d626eae9651de5ea3ab63'
            '04b4ea775ba805ff24e93162b6679e65d00b997a46cde11fd76602db4e824dc7'
            '72e3066ba033c8e59684331f2d9ea8ea2dc1855d51a7a4ea2fa5565b7dd6cc60')
_pythonver='3.6.1-2'
install="$pkgname.install"

_pkgarch=`uname -m`
if [ "$CARCH" == "x86" ]; then
    _pkgarch="x86"
    sha256sums[0]='7764093f337a43e4962b12d01508c1a385f0f62c1ddc006b69af95ae763fc4c2'
    source[0]="http://repo.continuum.io/archive/Anaconda3-${pkgver}-Linux-x86.sh"
fi

prepare() {
    cd ${srcdir}
    msg2 "Patching Anaconda3-${pkgver}-Linux-x86_64.sh"
    sed \
        -e '/^wc -c "\$THIS_PATH" | grep/s/^/#/' \
        -e '/^mkdir \$HOME\/\.continuum/s/^/#/' \
        -e '/^echo "creating default environment..."$/s/^/exit 0 || /' \
        -i Anaconda3-${pkgver}-Linux-x86_64.sh
}

package() {
    prefix=${pkgdir}/opt/${pkgname}
    LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

    msg2 "Extracting default libraries"
    bash ${srcdir}/Anaconda3-${pkgver}-Linux-${_pkgarch}.sh -b -p $prefix
    [ "$BREAK_EARLY" = 1 ] && exit 1

    msg2 "Patching .install.py"
    cd $prefix
    CONDA_INSTALL="$prefix/pkgs/.install.py"
    patch -p1 < $srcdir/install.py.patch

    msg2 "Installing anaconda to /opt/${pkgname}"
    $prefix/pkgs/python-${_pythonver}/bin/python -E -s $CONDA_INSTALL --root-prefix=$prefix --instdir=/opt/${pkgname} || exit 1

    msg2 "Correcting permissions"
    chmod a+r -R $prefix/pkgs

    msg2 "Stripping \$pkgdir from default meta"
    find conda-meta -name '*.json' -exec sed -e "s/${pkgdir//\//\\\/}//g" -i {} \;

    msg2 "Installing license"
    install -D -m644 $prefix/LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
