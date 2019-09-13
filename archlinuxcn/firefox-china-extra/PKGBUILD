#Maintainer: laomocode <3344907598@qq.com>
pkgname=firefox-china-extra
_firefoxname=firefox
pkgver=69.0
_downpkgver=69.0
pkgrel=1
pkgdesc="Firefox Chinese extensions pack,provides Firefox China sync services,China search,screenshot,tab optimised,address bar QR Code and drag gesture.火狐浏览器的中文包，提供中国版同步、中国的搜索引擎
截图、标签页优化、地址栏里的二维码和拖拽手势"
license=('MPL')
depends=('firefox')
arch=('any')
source=("https://download-ssl.firefox.com.cn/releases/firefox/${_downpkgver}/zh-CN/Firefox-latest-x86_64.tar.bz2")
md5sums=('83893414ec679c36b78613633c13d979')
package(){
    install -d ${pkgdir}/usr/lib/${_firefoxname}/distribution/
    cp -r ${srcdir}/firefox/distribution/extensions/ ${pkgdir}/usr/lib/${_firefoxname}/distribution/
    cp -r ${srcdir}/firefox/distribution/searchplugins ${pkgdir}/usr/lib/${_firefoxname}/distribution/
}
