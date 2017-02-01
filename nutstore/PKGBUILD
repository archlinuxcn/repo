#Maintainer: Bhoppi Chaw <bhoppi#outlook,com>

pkgname=nutstore
pkgver=3.3.2
pkgrel=4
pkgdesc='a cloud service that lets you sync and share files anywhere.'
arch=(x86_64 i686)
url='https://jianguoyun.com/'
license=(custom)
depends=(gtk2
         java-runtime
         python2-notify)
optdepends=('nautilus-nutstore: Nautilus plugin')
source=(nutstore license)
source_x86_64=("https://jianguoyun.com/static/exe/st/$pkgver/nutstore_client-$pkgver-linux-x64.tar.gz")
source_i686=("https://jianguoyun.com/static/exe/st/$pkgver/nutstore_client-$pkgver-linux-x86.tar.gz")
sha256sums=('3091740b20ddd31ba4407b8daba1077c4677040cdc47bccfab2f7f3947676384'
            'f3d2861ff48f2d193a4eced23a02b4eba9fab4c1d3f727e934ed7c59f38f0f7e')
sha256sums_x86_64=('709ed269bc407da17e2988af21209d4168b4666e4eed67ab9892a28d74edc44d')
sha256sums_i686=('0badda9abe88fc6095d99df97f908027fd7c9ef54368743d98a9580e7ca5f2c9')

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
