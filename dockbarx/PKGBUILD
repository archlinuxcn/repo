# Maintainer: twa022 <twa022 at gmail dot com>
# Contributor: rayman2200 

pkgname=dockbarx
pkgver=0.91.4
pkgrel=1
pkgdesc="TaskBar with groupping and group manipulation"
arch=('i686' 'x86_64')
url="https://github.com/M7S/dockbarx"
license=('GPL3')
depends=('python2-wnck' 'pygtk' 'python2-xdg' 'python2-dbus' 'python2-numpy' 
         'python2-pillow' 'python2-keybinder2' 'hicolor-icon-theme' 'python2-xlib'
         'python2-gconf')
optdepends=('avant-window-navigator: AWN DockBarX Plugin'
            'xfce4-dockbarx-plugin: Xfce4 Panel Plugin'
            'zeitgeist: recently used file list'
            'compiz-fusion-plugins-main: opacify plugin'
            'dockmanager: dockmanager plugins'
            'cardapio-bzr: required to run menu applet for dockx (standalone dock)')
conflicts=('dockbarx-bzr')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/M7S/dockbarx/archive/${pkgver}.tar.gz )
sha256sums=('81579ba37a693c4b50efeaa3c41d74a8d2c62d1b4691844742acb2ab8bb66eef')

package() {
  cd ${srcdir}/${pkgname}-${pkgver}

  python2 setup.py install --root ${pkgdir}

  mkdir -p ${pkgdir}/usr/share/avant-window-navigator/applets
  cp -r AWN/* ${pkgdir}/usr/share/avant-window-navigator/applets
  
  mkdir -p ${pkgdir}/usr/share/pixmaps
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/icons/hicolor/128x128/apps/dockbarx.png ${pkgdir}/usr/share/pixmaps/dockbarx.png

  sed -i 's:^Categories=.*:Categories=GTK;GNOME;Settings;X-GNOME-PersonalSettings;:' ${pkgdir}/usr/share/applications/dbx_preference.desktop
  sed -i 's:\(/usr/bin/python\)\([^2]\):\12\2:' ${pkgdir}/usr/bin/{dockbarx_factory,dbx_preference,dockx}
}

