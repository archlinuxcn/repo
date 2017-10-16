# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>
# Contributor : Jingbei Li <i@jingbei.li>

pkgname=anaconda
pkgver=5.0.0
pkgrel=2
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=('x86' 'x86_64')
url="https://store.continuum.io/cshop/anaconda/"
license=("custom")
source=("http://repo.continuum.io/archive/Anaconda3-${pkgver}-Linux-x86_64.sh"
        "$pkgname.install")
options=(!strip libtool staticlibs)
sha256sums=('67f5c20232a3e493ea3f19a8e273e0618ab678fa14b03b59b1783613062143e9'
            '72e3066ba033c8e59684331f2d9ea8ea2dc1855d51a7a4ea2fa5565b7dd6cc60')
install="$pkgname.install"

_pkgarch=`uname -m`
if [ "$CARCH" == "x86" ]; then
    _pkgarch="x86"
    sha256sums[0]='7764093f337a43e4962b12d01508c1a385f0f62c1ddc006b69af95ae763fc4c2'
    source[0]="http://repo.continuum.io/archive/Anaconda3-${pkgver}-Linux-x86.sh"
fi

package() {
    prefix=${pkgdir}/opt/${pkgname}
    LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

    msg2 "Installing anaconda to /opt/${pkgname}"
    bash ${srcdir}/Anaconda3-${pkgver}-Linux-${_pkgarch}.sh -b -p $prefix -f

    cd $prefix

    msg2 "Correcting permissions"
    chmod a+r -R $prefix/pkgs

    msg2 "Stripping \$pkgdir"
    sed "s|${pkgdir}||g" -i $(grep "$pkgdir" . -rIl)

    msg2 "Installing license"
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
