# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=deepin-qq-im
pkgver=8.9.19983deepin18
pkgrel=2
pkgdesc="Tencent QQ Client on Deepin Wine"
arch=("x86_64")
url="http://www.deepin.com/"
license=('custom')
depends=('p7zip' 'wine' 'xorg-xwininfo' 'xdotool' 'wine-mono')
_mirror="https://mirrors.tuna.tsinghua.edu.cn/deepin"
source=("$_mirror/pool/non-free/d/deepin.com.qq.im/deepin.com.qq.im_${pkgver}_i386.deb")
md5sums=('8ca84426078fd973c336ef6d68bf05cb')

package() {
  cd ${srcdir}
  tar -xvf data.tar.xz -C ${pkgdir}
  cd ${pkgdir}
  mv usr/local/share usr/share
  rmdir usr/local
  chmod -x usr/share/applications/deepin.com.qq.im.desktop
  sed '30a\sed -i "s/deepin-wine/wine/" $1/drive_c/deepin/EnvInit.sh' -i opt/deepinwine/apps/Deepin-QQ/run.sh
}
