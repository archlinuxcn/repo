#
# Maintainer: Iacopo Isimbaldi <isiachi@rhye.it>
#

pkgbase="spl-dkms-git"
pkgname=("spl-dkms-git" "spl-utils-dkms-git")
pkgver=0.6.5_r52_gea2633a
pkgrel=1
license=('GPL')
makedepends=("git")
arch=("i686" "x86_64")
url="http://zfsonlinux.org/"
source=("git+https://github.com/zfsonlinux/spl.git"
        "spl-utils.hostid")
sha256sums=('SKIP'
            'ad95131bc0b799c0b1af477fb14fcf26a6a9f76079e48bf090acb7e8367bfd0e')

pkgver() {
    cd "${srcdir}/spl"
    git describe --match "spl-*" --long --tags | sed -e 's|spl-||' -e 's|-\([0-9]*-g\)|-r\1|' -e 's|[-: ]|_|g'
}

build() {
    cd "${srcdir}/spl"
    ./autogen.sh

    _at_enable=""
    [ "${CARCH}" == "i686"  ] && _at_enable="--enable-atomic-spinlocks"

    ./configure --prefix=/usr \
                --libdir=/usr/lib \
                --sbindir=/usr/bin \
                --with-config=user \
                ${_at_enable}

    make
}

package_spl-dkms-git() {
    pkgdesc="Solaris Porting Layer kernel modules."
    depends=("dkms" "spl-utils-dkms-git=${pkgver}-${pkgrel}")
    provides=("spl")
    conflicts=("spl-git" "spl-lts" "spl-dkms")
    install=spl.install

    dkmsdir="${pkgdir}/usr/src/spl-${pkgver%%_*}"
    install -d "${dkmsdir}"
    cp -a ${srcdir}/spl/. ${dkmsdir}

    cd "${dkmsdir}"
    make clean distclean
    find . -name ".git*" -print0 | xargs -0 rm -fr --
    scripts/dkms.mkconf -v ${pkgver%%_*} -f dkms.conf -n spl
    chmod g-w,o-w -R .
}

package_spl-utils-dkms-git() {
    pkgdesc="Solaris Porting Layer kernel module support files."
    provides=("spl-utils")
    conflicts=("spl-utils-git" "spl-utils-lts" "spl-utils")

    cd "${srcdir}/spl"
    make DESTDIR="${pkgdir}" install

    install -D -m644 "${srcdir}"/spl-utils.hostid "${pkgdir}"/etc/hostid
}
