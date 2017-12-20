# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=deepin-qq-im
pkgver=8.9.19983deepin19
_qqver=8.9.3
pkgrel=1
pkgdesc="Tencent QQ Client on Deepin Wine"
arch=("x86_64")
url="http://www.deepin.com/"
license=('custom')
depends=('p7zip' 'wine' 'xorg-xwininfo' 'xdotool' 'wine-mono')
_mirror="https://mirrors.tuna.tsinghua.edu.cn/deepin"
source=("$_mirror/pool/non-free/d/deepin.com.qq.im/deepin.com.qq.im_${pkgver}_i386.deb"
	"http://dldir1.qq.com/qqfile/qq/QQ${_qqver}/21149/QQ${_qqver}.exe"
	"run.sh")
md5sums=('e727b3dc87f2533aa36b489f38806060'
         '53cbda2c19734160c75af43a6107b759'
         '1572a7c41ef720f94bfed13e0e002d05')

package() {
	cd ${srcdir}
	tar -xvf data.tar.xz -C ${pkgdir}
	cd ${pkgdir}
	mv usr/local/share usr/share
	rmdir usr/local
	chmod -x usr/share/applications/deepin.com.qq.im.desktop
	rm opt/deepinwine/apps/Deepin-QQ/run.sh
	cp ${srcdir}/{run.sh,QQ$_qqver.exe} -i opt/deepinwine/apps/Deepin-QQ/
}
