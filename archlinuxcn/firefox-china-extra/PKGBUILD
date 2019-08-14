#Maintainer: laomocode <3344907598@qq.com>
pkgname=firefox-china-extra
_firefoxname=firefox
pkgver=68.0
pkgrel=1
pkgdesc="Firefox Chinese extensions pack,provides Firefox China sync services.火狐浏览器的中文包，提供中国版同步。"
license=('custom')
depends=('firefox')
arch=('any')
source=(
    "https://download-ssl.firefox.com.cn/releases/firefox/${pkgver}/zh-CN/Firefox-latest-x86_64.tar.bz2"
    "https://www.mozilla.org/zh-CN/about/legal/terms/services/index.html"
)
md5sums=('29b14b1e769d11f053f4fff99ac6e836'
    'SKIP')
package(){
    install -d ${pkgdir}/usr/lib/${_firefoxname}/distribution/
    cp -r ${srcdir}/firefox/distribution/extensions/ ${pkgdir}/usr/lib/${_firefoxname}/distribution/
    cp -r ${srcdir}/firefox/distribution/searchplugins ${pkgdir}/usr/lib/${_firefoxname}/distribution/
    install -D -m644 index.html ${pkgdir}/usr/share/licenses/$pkgname/license.html
}
