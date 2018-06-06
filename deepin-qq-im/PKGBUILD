# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=deepin-qq-im
_qqver=8.9
_qqbuild=19983
_deepinver=22
pkgver=${_qqver}.${_qqbuild}deepin${_deepinver}
pkgrel=2
pkgdesc="Tencent QQ Client on Deepin Wine"
arch=("x86_64")
url="http://www.deepin.com/"
license=('custom')
depends=('p7zip' 'wine' 'xorg-xwininfo' 'xdotool' 'wine-mono')
_mirror="https://mirrors.tuna.tsinghua.edu.cn/deepin"
source=("$_mirror/pool/non-free/d/deepin.com.qq.im/deepin.com.qq.im_${pkgver}_i386.deb"
	"http://dldir1.qq.com/qqfile/qq/QQ${_qqver}/${_qqbuild}/QQ${_qqver}.exe"
	"run.sh")
md5sums=('8cc202749ac759c1a6d3f387e6b83387'
         'a60127de3c7c11342f644ad87f4c7b7d'
         '2946b58e28067f84186fc27c3e7a6dc0')

package() {
	cd ${srcdir}
	tar -xvf data.tar.xz -C ${pkgdir}
	cd ${pkgdir}
	chmod -x usr/share/applications/deepin.com.qq.im.desktop
	rm opt/deepinwine/apps/Deepin-QQ/run.sh
	cp ${srcdir}/{run.sh,QQ$_qqver.exe} -i opt/deepinwine/apps/Deepin-QQ/
}
