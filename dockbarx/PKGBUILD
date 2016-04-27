# Maintainer: twa022 <twa022 at gmail dot com>
# Contributor: rayman2200 

pkgname=dockbarx
pkgver=0.92
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
sha256sums=('eb7630c0cebeb84ba9f66c60d77ec082afe56b264db4139436913ebdf2b1b7ea')

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
