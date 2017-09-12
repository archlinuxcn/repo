# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=deepin-wechat
pkgver=2.4.5.48deepin2
pkgrel=2
pkgdesc="Tencent WeChat Client on Deepin Wine"
arch=("x86_64")
url="http://www.deepin.com/"
license=('custom')
depends=('p7zip' 'wine' 'xdotool' 'xorg-xwininfo')
_mirror="https://mirrors.tuna.tsinghua.edu.cn/deepin"
source=("$_mirror/pool/non-free/d/deepin.com.wechat/deepin.com.wechat_${pkgver}_i386.deb")
md5sums=('65a297ea7ec081cb43b68e1b32ab63b3')

package() {
  cd ${srcdir}
  tar -xvf data.tar.xz -C ${pkgdir}
  cd ${pkgdir}
  mv usr/local/share usr/share
  rmdir usr/local
  chmod -x usr/share/applications/deepin.com.wechat.desktop
  sed '30a\sed -i "s/deepin-wine/LANG=zh_CN.UTF-8 wine/" $1/drive_c/deepin/EnvInit.sh' -i opt/deepinwine/apps/Deepin-WeChat/run.sh
}
