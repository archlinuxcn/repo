# Maintainer: twa022 <twa022 at gmail dot com>
# Contributor: rayman2200 

pkgname=dockbarx
pkgver=0.93
pkgrel=1
pkgdesc="TaskBar with groupping and group manipulation"
arch=('i686' 'x86_64')
url="https://github.com/M7S/dockbarx"
license=('GPL3')
depends=('python2-wnck' 'pygtk' 'python2-xdg' 'python2-dbus' 'python2-numpy' 
         'python2-pillow' 'python2-keybinder2' 'hicolor-icon-theme' 'python2-xlib'
         'python2-gconf' 'python2-six')
optdepends=('avant-window-navigator: AWN DockBarX Plugin'
            'xfce4-dockbarx-plugin: Xfce4 Panel Plugin'
            'zeitgeist: recently used file list'
            'compiz-fusion-plugins-main: opacify plugin'
            'dockmanager: dockmanager plugins'
            'cardapio-bzr: required to run menu applet for dockx (standalone dock)')
conflicts=('dockbarx-git')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/M7S/dockbarx/archive/${pkgver}.tar.gz")
sha256sums=('3f81b39d051c8b961df32e883069276dca10d84bae997b18f7938b004a3577e2')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  python2 setup.py install --root "${pkgdir}"

  mkdir -p "${pkgdir}"/usr/share/avant-window-navigator/applets
  cp -r AWN/* "${pkgdir}"/usr/share/avant-window-navigator/applets
  
  mkdir -p "${pkgdir}"/usr/share/pixmaps
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}"/icons/hicolor/128x128/apps/dockbarx.png "${pkgdir}"/usr/share/pixmaps/dockbarx.png

  sed -i 's:^Categories=.*:Categories=GTK;GNOME;Settings;X-GNOME-PersonalSettings;:' "${pkgdir}"/usr/share/applications/dbx_preference.desktop
  sed -i 's:\(/usr/bin/python\)\([^2]\):\12\2:' "${pkgdir}"/usr/bin/{dockbarx_factory,dbx_preference,dockx}

}
