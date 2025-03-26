# Maintainer: marmis <tiagodepalves@gmail.com>
# Contributor: vitor_hideyoshi <vitor.h.n.batista@gmail.com>
# Contributor: katt <magunasu.b97@gmail.com>
# Contributor: Yangtse Su <i@yangtse.me>

_pkgname=xpadneo
_dkmsname=hid-${_pkgname}
pkgname=${_pkgname}-dkms
pkgver=0.9.7
_pkgver=v${pkgver}
pkgrel=1
pkgdesc="Advanced Linux Driver for Xbox One Wireless Gamepad"
arch=(any)
url='https://github.com/atar-axis/xpadneo'
license=(GPL-3.0-or-later)
depends=('dkms' 'bluez' 'bluez-utils')
source=("${_pkgname}-${_pkgver}.tar.gz::${url}/archive/${_pkgver}.tar.gz"
        01-drop-etc-files.patch)
b2sums=('6715e684d046ad3162db65196896d23f0c70046d02adbf5886d849818120fb731acb86da0a9e18e54b56b31220911ea25c296f1b8473eb0f0fca4fe96b98712b'
        'a11c9f312a1355407b749766640ad8097a9608c11ae521b1a32f0a9c7c02d39fabca22960528f5e06926b1a7690679cba83f07e9c8f033745119b89732b0fe6b')

prepare() {
    cd "${_pkgname}-${pkgver}/${_dkmsname}"

    # Upstream uses dkms.post_install to create modprobe and udev files in
    # /etc. In Arch, it makes more sense to create these files in /usr/lib
    # and let pacman take care of them.
    patch -p1 -i "${srcdir}/01-drop-etc-files.patch"

    # Set the current version in DKMS config file.
    sed "s/@DO_NOT_CHANGE@/${_pkgver}/" dkms.conf.in > dkms.conf
}

check() {
    # Warning if missing linux-headers for current `uname -r` kernel
    if [ ! -f "/usr/lib/modules/$(uname -r)/build/Makefile" ]
    then
        _BOLDRED='\033[1;31m'
        _RED='\033[0;31m'
        _RESET='\033[0m'
        echo -e "${_BOLDRED}WARNING:${_RED} You may be missing headers for your current kernel, DKMS packages requires them."
        echo -e "Please refer to https://wiki.archlinux.org/title/Dynamic_Kernel_Module_Support for details.${_RESET}"
    fi
}

package() {
    cd "${_pkgname}-${pkgver}/${_dkmsname}"

    # Module source
    install -Dm0644 -t "${pkgdir}/usr/src/${_dkmsname}-${_pkgver}/src" src/*

    # DKMS files
    install -Dm0644 -t "${pkgdir}/usr/src/${_dkmsname}-${_pkgver}" Makefile dkms.conf
    install -Dm0755 -t "${pkgdir}/usr/src/${_dkmsname}-${_pkgver}" dkms.post_install dkms.post_remove

    # Module dependencies
    install -Dm0644 -t "${pkgdir}/usr/lib/modprobe.d" etc-modprobe.d/*
    install -Dm0644 -t "${pkgdir}/usr/lib/udev/rules.d" etc-udev-rules.d/*
}
