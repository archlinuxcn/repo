#Maintainer: Bhoppi Chaw <bhoppi#outlook,com>

pkgname=nutstore
pkgver=3.4.5
pkgrel=1
pkgdesc='a cloud service that lets you sync and share files anywhere.'
arch=(x86_64)
url='https://jianguoyun.com/'
license=(custom)
depends=(gtk2 java-runtime)
optdepends=(
    'nautilus-nutstore: Nautilus plugin'
    'python2-notify: desktop notification'
)
source=(nutstore license)
source_x86_64=('https://www.jianguoyun.com/static/exe/installer/nutstore_linux_dist_x64.tar.gz')
#source_i686=('https://www.jianguoyun.com/static/exe/installer/nutstore_linux_dist_x86.tar.gz')
sha256sums=('3091740b20ddd31ba4407b8daba1077c4677040cdc47bccfab2f7f3947676384'
            'f3d2861ff48f2d193a4eced23a02b4eba9fab4c1d3f727e934ed7c59f38f0f7e')
sha256sums_x86_64=('fac9773875a5391a047f342414e988dd0df7f7938f14833f4b1352d3e4c64a00')
#sha256sums_i686=('48de3e2f062f47ff48980422115102e4460f5be38643d14e91e4e7e82cabf64e')

build()
{
    cd $srcdir
    sed -i '1s/python/python2/' bin/nutstore-pydaemon.py
    cd gnome-config
    sed -i '/Exec=/s|~/\.nutstore/dist/bin/nutstore-pydaemon.py|/usr/bin/nutstore|' menu/nutstore-menu.desktop
    sed -i '/Exec=/s|~/\.nutstore/dist|/opt/nutstore|' autostart/nutstore-daemon.desktop
}

package()
{
    cd $srcdir
    install -D -m755 nutstore $pkgdir/usr/bin/nutstore
    install -D -m644 license $pkgdir/usr/share/licenses/$pkgname/license
    rm nutstore license *.tar.gz
    mkdir -p $pkgdir/opt/$pkgname && cp -aR ./ $pkgdir/opt/$pkgname
    install -D -m644 gnome-config/menu/nutstore-menu.desktop $pkgdir/usr/share/applications/nutstore.desktop
    install -D -m644 app-icon/nutstore.png $pkgdir/usr/share/icons/hicolor/64x64/apps/nutstore.png
}
