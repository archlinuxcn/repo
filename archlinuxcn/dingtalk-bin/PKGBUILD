# Maintainer: zhullyb <zhullyb [at] outlook dot com>
# Maintainer: yjun <jerrysteve1101 at gmail dot com>
# Contributor: Bruce Zhang <zttt183525594@gmail.com>

pkgname=dingtalk-bin
_pkgname=dingtalk
_pkgname2=com.alibabainc.dingtalk
pkgver=1.2.0.132
pkgrel=3
pkgdesc="钉钉"
arch=("x86_64")
url="https://gov.dingtalk.com"
license=("custom")
depends=("glu")
makedepends=("icoutils")
provides=('com.alibabainc.dingtalk' 'dingtalk')
conflicts=('com.alibabainc.dingtalk')
replaces=('com.alibabainc.dingtalk')
# https://tms.dingtalk.com/markets/dingtalk/service-terms-zh md5 will change per download
source=("${_pkgname}_${pkgver}-${arch}.deb::https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Release/${_pkgname2}_${pkgver}_amd64.deb"
        "service-terms-zh"
        "${_pkgname2}.desktop"
        "dingtalk.sh")


# DebSource & pkgvere can be get here: https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Update/other/linux_dingtalk_update.json

sha512sums=('03d0ed86125297de547be4f56e0757c098762a25eb246e72fc98061a244e73096fbc5a59974412b7945f58c733d686dcbccdd0f08492dc6050edff9ab49226e5'
            'b83d493ed68be0f5a6b851fd93d819bb3a6e62feeb71a5bef10bad24b5ea8f3cf09deea4f31ed727449888a6eae1be99fa9cf263bc921cb8bb2958e2f37a7d64'
            'c8570ec4cd978e26ac622a83db053a0555324752f5000dc5b3cd680d782138e8ef856f09ec9b7850e04e1faa1e39de94dabeb16fbfbe0fd44af43247b30e8b2f'
            '50437762c47843fa9040bfb5a723da246d1496e4dc0937028c0f2cb92e0286dc47b7c2a5a0485a4b667cfb30d7c4d23664a2ccb08c5bd3059aad265532c1140e')

prepare(){
    cd ${srcdir}
    tar -Jxvf data.tar.xz -C "${srcdir}"
}

package(){
    cd ${srcdir}

    mkdir -p ${pkgdir}/opt/${_pkgname}/release
    mkdir -p ${pkgdir}/usr/share/doc/
    mv opt/apps/${_pkgname2}/files/*-Release.*/* ${pkgdir}/opt/${_pkgname}/release
    mv opt/apps/${_pkgname2}/files/version ${pkgdir}/opt/${_pkgname}
    mv opt/apps/${_pkgname2}/files/doc/${_pkgname2} ${pkgdir}/usr/share/doc/${_pkgname}

    # binary wrapper
    install -Dm755 ${srcdir}/dingtalk.sh ${pkgdir}/usr/bin/dingtalk

    # desktop enrty
    install -Dm644 ${_pkgname2}.desktop -t ${pkgdir}/usr/share/applications/
    
    # icons
    # extract single image of size 48x48
    icotool -x -i 3 opt/apps/${_pkgname2}/files/logo.ico -o .
    install -Dm644 logo_3_48x48x32.png ${pkgdir}/usr/share/pixmaps/${_pkgname}.png

    # license
    install -Dm644 service-terms-zh ${pkgdir}/usr/share/licenses/${_pkgname}/service-terms-zh.html

#     ## libraries
# 
#     cd ${pkgdir}/opt/${_pkgname}/release
#     mkdir ${pkgdir}/opt/${_pkgname}/tmplib
#     mv {dingtalk*,libcef.so,libgraysdk.so,libahencrypt.so,libpangox-1.0.so.0,libgtkglext-x11-1.0.so.0,libgdkglext-x11-1.0.so.0,libutforpc.so} ${pkgdir}/opt/${_pkgname}/tmplib
#     
#     
#     ## remove unused files
#     rm  -rf ${pkgdir}/opt/${_pkgname}/release/{libQt*,libm.so.6,imageformats,platforminputcontexts,platforms}
#     rm  -rf ${pkgdir}/opt/${_pkgname}/release/lib*
#     mv ${pkgdir}/opt/${_pkgname}/tmplib/* ${pkgdir}/opt/${_pkgname}/release
#     rmdir ${pkgdir}/opt/${_pkgname}/tmplib 
    # dingtalk_updater
    rm -rf ${pkgdir}/opt/${_pkgname}/release/{libm.so.6,Resources/{i18n/tool/*.exe,qss/mac}}
}
