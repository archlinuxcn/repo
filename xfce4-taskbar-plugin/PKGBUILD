# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: fand <fandrieu@gmail.com>

pkgname=xfce4-taskbar-plugin
pkgver=20130504
pkgrel=2
pkgdesc='Taskbar plugin which mimicks the Windows 7 taskbar (pinning applications, etc)'
arch=('i686' 'x86_64')
url='http://git.xfce.org/panel-plugins/xfce4-taskbar-plugin/'
depends=('xfce4-panel>=4.4' 'libwnck' 'gtkhotkey')
makedepends=('git')
options=()
license=('LGPL')
install="${pkgname}.install"
source=("git://git.xfce.org/panel-plugins/${pkgname}")
md5sums=('SKIP')

pkgver() {
  cd ${srcdir}/${pkgname}
  git log -1 --format="%cd" --date=short | sed 's|-||g'
}

build() {
  cd ${srcdir}/${pkgname}
  make
}

package() {
  cd ${srcdir}/${pkgname}
  mkdir -p ${pkgdir}/usr/lib/xfce4/panel-plugins
  mkdir -p ${pkgdir}/usr/share/xfce4/panel/plugins

  cp -f libtaskbar.so   ${pkgdir}/usr/lib/xfce4/panel-plugins/
  cp -f taskbar.desktop ${pkgdir}/usr/share/xfce4/panel/plugins/
}