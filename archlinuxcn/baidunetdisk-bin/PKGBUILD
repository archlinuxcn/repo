# Maintainer: Ariel AxionL <i at axionl dot me>
# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: lilydjwg <lilydjwg at gmail dot com>
_pkgname=baidunetdisk
pkgname=baidunetdisk-bin
pkgver=3.0.1.2
pkgrel=10
_mainver=${pkgver%.*}
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

source_x86_64=("${pkgname}-${pkgver}.deb::https://issuecdn.baidupcs.com/issue/netdisk/LinuxGuanjia/${_mainver}/${_pkgname}_linux_${pkgver}.deb")

sha256sums=('d72eb6fa07abc0e7c2298fcecbe4a4e6849c63a6a31c39706e0dfea870e85aff'
            'c0035e038344a154421301b7855c274049ad432a5b06b52efc74831daa73e02e')
sha256sums_x86_64=('40eb1950af62a8b9b75da8ffb9a74416ae0d3fc886b07f6de7d63673683b1ef3')

prepare() {
    bsdtar -xpf "data.tar.xz"

    # # modify the HOME environment variable for the application's desktop file
    patch -d "usr" -p1 <"0001-baidunetdisk-bin-desktop-file.patch"
}

package() {
    cd "${srcdir}"

    # install application data
    mv "usr" "${pkgdir}"
    install -dm755 "${pkgdir}/usr/bin" "${pkgdir}/usr/lib" "${pkgdir}/usr/share/licenses/${_pkgname}"
    mv "opt/${_pkgname}" "${pkgdir}/usr/lib/${_pkgname}"
    install -Dm755 "${srcdir}/baidunetdisk-wrapper.sh" "${pkgdir}/usr/bin/baidunetdisk"

    # fix promission
    chmod 644 "${pkgdir}/usr/lib/${_pkgname}/"*.so
    find ${pkgdir} -type d -exec chmod 755 {} \;

    # install license
    ln -s "/usr/lib/${_pkgname}/LICENSE.electron.txt" \
        "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE.electron.txt"
    ln -s "/usr/lib/${_pkgname}/LICENSES.chromium.html" \
        "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSES.chromium.html"
}
