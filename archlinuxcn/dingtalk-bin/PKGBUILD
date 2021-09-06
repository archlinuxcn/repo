# Maintainer: zhullyb <zhullyb [at] outlook dot com>
# Maintainer: yjun <jerrysteve1101 at gmail dot com>
# Contributor: Bruce Zhang <zttt183525594@gmail.com>

pkgname=dingtalk-bin
_pkgname=com.alibabainc.dingtalk
pkgver=1.0.0.285
pkgrel=1
pkgdesc="钉钉"
arch=("x86_64")
url="https://gov.dingtalk.com"
license=("custom")
depends=("glu")
provides=('com.alibabainc.dingtalk' 'dingtalk')
conflicts=('com.alibabainc.dingtalk')
replaces=('com.alibabainc.dingtalk')
# https://tms.dingtalk.com/markets/dingtalk/service-terms-zh md5 will change per download
source=("https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Release/${_pkgname}_${pkgver}_amd64.deb"
        "service-terms-zh"
        "${_pkgname}.desktop"
        "dingtalk.sh")

# DebSource & pkgvere can be get here: https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Update/other/linux_dingtalk_update.json

md5sums=('c55d666652ad08c3a2bd0e10b469426f'
         '55c7432e36da19b45102376dad9ebdf7'
         'e1b984a024700a9ef5f77a1018a41f8e'
         '0e255cd61852162548db96e46f1dda00')

prepare(){
    cd ${srcdir}
    tar -Jxvf data.tar.xz -C "${srcdir}"
}

package(){
    cd ${srcdir}

    mkdir -p ${pkgdir}/opt/apps/${_pkgname}/files
    mv opt/apps/${_pkgname}/files/* ${pkgdir}/opt/apps/${_pkgname}/files

    # binary wrapper
    install -Dm755 ${srcdir}/dingtalk.sh ${pkgdir}/usr/bin/dingtalk

    # desktop enrty
    install -Dm644 ${_pkgname}.desktop -t ${pkgdir}/usr/share/applications/

    # license
    install -Dm644 service-terms-zh ${pkgdir}/usr/share/licenses/${pkgname}/service-terms-zh

    rm ${pkgdir}/opt/apps/${_pkgname}/files/*/libm.so.6
}
