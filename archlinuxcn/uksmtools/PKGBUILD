# Maintainer: FadeMind <fademind@gmail.com>
# Contributor: Leonardo Dagnino <leodag dot sch at gmail dot com>

_gitcommit='cc76f9f5496d5b5afc1377cce7cc029a3d72e7e9' # lastest commit
pkgname=uksmtools
pkgver=20140911 # date of lastest commit
pkgrel=1
pkgdesc="Small set of tools to control UKSM"
arch=('i686' 'x86_64')
url="https://github.com/pfactum/${pkgname}"
license=('GPL')
makedepends=('make' 'gcc')
optdepends=("linux-pf: Linux kernel and modules with the pf-kernel patch [-ck patchset (BFS included), TuxOnIce, BFQ] and aufs3"
            "linux-uksm: Linux Kernel and modules with the UKSM patchset featuring the v1.2.4 and BFQ scheduler"
            "linux-uksm-ck: Linux Kernel and modules with the UKSM patchset featuring the v1.2.4. and the ck1 patchset featuring the Brain Fuck Scheduler")
replaces=('uksmstat')
conflicts=('uksmstat')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${_gitcommit}.tar.gz")
sha256sums=('2d2d59f2aacbe8d873d924b1ee3c83342be22bab0bf3663d5ae56f9757010e54')

build() {
    cd ${srcdir}/${pkgname}-${_gitcommit}
    make
}

package() {
    cd ${srcdir}/${pkgname}-${_gitcommit}
    make install DESTDIR="$pkgdir"  
    mv ${pkgdir}/usr/local/* ${pkgdir}/usr
    rm -r ${pkgdir}/usr/local
}
