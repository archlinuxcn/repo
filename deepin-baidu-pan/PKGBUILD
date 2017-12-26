# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=deepin-baidu-pan
pkgver=5.5.4deepin8
pkgrel=1
pkgdesc="Baidu net disk client on Deepin Wine"
arch=("x86_64")
url="http://www.deepin.com/"
license=('custom')
depends=('p7zip' 'wine' 'xorg-xwininfo' 'xdotool')
_mirror="https://mirrors.tuna.tsinghua.edu.cn/deepin"
source=("$_mirror/pool/non-free/d/deepin.com.baidu.pan/deepin.com.baidu.pan_${pkgver}_i386.deb")
md5sums=('20383bc9574c979199cd86e85b6f5871')

package() {
  cd ${srcdir}
  tar -xvf data.tar.xz -C ${pkgdir}
  cd ${pkgdir}
  mv usr/local/share usr/share
  rmdir usr/local
  chmod -x usr/share/applications/deepin.com.baidu.pan.desktop
  sed '30a\sed -i "s/deepin-wine/wine/" $1/drive_c/deepin/EnvInit.sh' -i opt/deepinwine/apps/Deepin-BaiduNetDisk/run.sh
}
