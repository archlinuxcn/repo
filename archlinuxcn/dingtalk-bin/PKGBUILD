# Maintainer: zhullyb <zhullyb [at] outlook dot com>
# Maintainer: yjun <jerrysteve1101 at gmail dot com>
# Contributor: Bruce Zhang <zttt183525594@gmail.com>

pkgname=dingtalk-bin
_pkgname=dingtalk
_pkgname2=com.alibabainc.dingtalk
pkgver=1.4.0.20408
pkgrel=1
pkgdesc="钉钉"
arch=("x86_64")
url="https://www.dingtalk.com/"
license=("custom")
depends=("glu" 'gtk2')
#makedepends=("icoutils")
optdepends=('zenity: fix crashes when downloading files, not required on kde.')
provides=('com.alibabainc.dingtalk' 'dingtalk')
conflicts=('com.alibabainc.dingtalk')
replaces=('com.alibabainc.dingtalk')
# https://tms.dingtalk.com/markets/dingtalk/service-terms-zh md5 will change per download
source=("${_pkgname}_${pkgver}-${arch}.deb::https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Release/${_pkgname2}_${pkgver}_amd64.deb"
        "service-terms-zh"
        "${_pkgname2}.desktop"
        "dingtalk.sh"
        "${_pkgname2}.svg"
        "https://archive.archlinux.org/packages/c/cairo/cairo-1.17.4-5-x86_64.pkg.tar.zst"
        )


# DebSource & pkgver can be get here: https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Update/other/linux_dingtalk_update.json

sha512sums=('d5413c16b5ab19766c4f90043193d51282b57a0f80af9b22dcb107494b925a321063538eee217b223d5fb4bb10e8e7bb319950a18d6b027780722f5b95b0b7e8'
            'b83d493ed68be0f5a6b851fd93d819bb3a6e62feeb71a5bef10bad24b5ea8f3cf09deea4f31ed727449888a6eae1be99fa9cf263bc921cb8bb2958e2f37a7d64'
            'c8570ec4cd978e26ac622a83db053a0555324752f5000dc5b3cd680d782138e8ef856f09ec9b7850e04e1faa1e39de94dabeb16fbfbe0fd44af43247b30e8b2f'
            '5fbd54206362186a6f3a77f07005dbe76682ddafa38e16ed71c52881406e4f5b9f466397c3bb290614c6e0e3bd016ef94081c0a1b84559de8406339859e69264'
            '5f05f90704526fbd16371f6f9deaa171a3cac25a103b21daba72a3028ab7cdf9b566a3ac7842c6ce88d30cc29fe0c8b989c77aa36daab73793a827a1a0d6c775'
            '94a108a3f3f88bc7ede370d5e3f84afaedd78d892f7352926091881c066cbe0da55bebb5fc83978ca83c6420ed0c94fbba1f3454c5ff8d33a38669a0a11a80ac')

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
    
    install -Dm644 ${srcdir}/${_pkgname2}.svg ${pkgdir}/usr/share/icons/hicolor/scalable/apps/${_pkgname}.svg

    # license
    install -Dm644 service-terms-zh ${pkgdir}/usr/share/licenses/${_pkgname}/service-terms-zh.html
    
    # fix chinese input in workbench
    rm -rf ${pkgdir}/opt/${_pkgname}/release/libgtk-x11-2.0.so.*
    
    # fix cairo
    cd $srcdir/usr/lib
    install -Dm755 libcairo.so.2 -t ${pkgdir}/usr/lib/dingtalk

    rm -rf ${pkgdir}/opt/${_pkgname}/release/{libm.so.6,Resources/{i18n/tool/*.exe,qss/mac}}
}
