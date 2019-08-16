#Maintainer: laomocode <3344907598@qq.com>
pkgname=firefox-china-extra
_firefoxname=firefox
pkgver=68.0.2
_downpkgver=68.0
pkgrel=1
pkgdesc="Firefox Chinese extensions pack,provides Firefox China sync services.火狐浏览器的中文包，提供中国版同步。"
license=('MPL')
depends=('firefox')
arch=('any')
source=(
    "https://download-ssl.firefox.com.cn/releases/firefox/${_downpkgver}/zh-CN/Firefox-latest-x86_64.tar.bz2")
md5sums=('0f002a1530874ae443cfb826735aa447')
package(){
    install -d ${pkgdir}/usr/lib/${_firefoxname}/distribution/
    cp -r ${srcdir}/firefox/distribution/extensions/ ${pkgdir}/usr/lib/${_firefoxname}/distribution/
    cp -r ${srcdir}/firefox/distribution/searchplugins ${pkgdir}/usr/lib/${_firefoxname}/distribution/
}
