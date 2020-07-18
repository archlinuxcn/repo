# Maintainer: Ariel AxionL <i at axionl dot me>
# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: lilydjwg <lilydjwg at gmail dot com>
_pkgname=baidunetdisk
pkgname=baidunetdisk-bin
pkgver=3.3.2
pkgrel=1
#_mainver=${pkgver%.*}
pkgdesc="Baidu Net Disk - a cloud storage client (Linux Version)."
arch=('x86_64')
depends=('libxss' 'gtk3' 'nss')
provides=("baidunetdisk")
conflicts=("baidunetdisk")
url="https://pan.baidu.com"
license=("custom")
options=('!strip')

source=("0001-baidunetdisk-bin-desktop-file.patch"
        "baidunetdisk-wrapper.sh")

#source_x86_64=("${pkgname}-${pkgver}.deb::https://issuecdn.baidupcs.com/issue/netdisk/LinuxGuanjia/${_mainver}/${_pkgname}_linux_${pkgver}.deb")
source_x86_64=("${pkgname}-${pkgver}.deb::http://wppkg.baidupcs.com/issue/netdisk/Linuxguanjia/${pkgver}/baidunetdisk_${pkgver}_amd64.deb")

sha256sums=('1e0d9616c58d3b772b42d4790625cf2c34ab671f586b8534a2c544c2117bb5d0'
            'c0035e038344a154421301b7855c274049ad432a5b06b52efc74831daa73e02e')
sha256sums_x86_64=('b14989965e6eb30bb06e4c67cbd4288826b6914ed8ba9efe05cb83cc06487b7d')

prepare() {
    bsdtar -xpf "data.tar.xz"

    patch -d "usr" -p1 <"0001-baidunetdisk-bin-desktop-file.patch"
}

package() {
    cd "${srcdir}"

    # install application data
    mv "usr" "${pkgdir}"
    install -dm755 "${pkgdir}/usr/lib" "${pkgdir}/usr/share/licenses/${_pkgname}"
    mv "opt/${_pkgname}" "${pkgdir}/usr/lib/${_pkgname}"
#   install -Dm755 "${srcdir}/baidunetdisk-wrapper.sh" "${pkgdir}/usr/bin/baidunetdisk"

    # fix promission
    chmod 644 "${pkgdir}/usr/lib/${_pkgname}/"*.so
    find ${pkgdir} -type d -exec chmod 755 {} \;

    # install license
    ln -s "/usr/lib/${_pkgname}/LICENSE.electron.txt" \
        "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE.electron.txt"
    ln -s "/usr/lib/${_pkgname}/LICENSES.chromium.html" \
        "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSES.chromium.html"
}
