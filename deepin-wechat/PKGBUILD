# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=deepin-wechat
pkgver=2.4.5.48deepin0
pkgrel=2
pkgdesc="Tencent WeChat Client on Deepin Wine"
arch=("x86_64")
url="http://www.deepin.com/"
license=('custom')
depends=('p7zip' 'wine' 'wine-mono' 'xdotool' 'xorg-xwininfo')
_mirror="https://mirrors.tuna.tsinghua.edu.cn/deepin"
source=("$_mirror/pool/non-free/d/deepin.com.wechat/deepin.com.wechat_${pkgver}_i386.deb")
md5sums=('92198b30edd3a0f1f0faa694320fe14c')

package() {
  cd ${srcdir}
  tar -xvf data.tar.xz -C ${pkgdir}
  cd ${pkgdir}
  mv usr/local/share usr/share
  rmdir usr/local
  chmod -x usr/share/applications/deepin.com.wechat.desktop
  sed '30a\sed -i "s/deepin-wine/wine/" $1/drive_c/deepin/EnvInit.sh' -i opt/deepinwine/apps/Deepin-WeChat/run.sh
}
