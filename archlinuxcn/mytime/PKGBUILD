# Maintainer: laomocode <3344907598@qq.com>
pkgname=mytime
pkgver=1.02
pkgrel=1
pkgdesc="日程提醒、万年历、黄历和天气"
arch=("x86_64")
url="https://mytime.ruanmei.com/"
license=('custom')
depends=('gtk3' 'libnotify' 'nss' 'libxss' 'libxtst' 'xdg-utils' 'libappindicator-gtk3' 'libsecret')
source=("https://d.ruanmei.com/mytime/linux/mytime_linux_1.02_amd64.deb")
sha256sums=('4ff77e51b922094a6006249d1f41cf1ce5077ba3a1bd415091d05fb50a3acc43')
package(){
    tar -xvf data.tar.xz -C "${pkgdir}"
}