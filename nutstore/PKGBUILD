#Maintainer: Bhoppi Chaw <bhoppi#outlook,com>

pkgname=nutstore
pkgver=3.3.2
pkgrel=2
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
md5sums=(be61391e4752490bdf8a402413d79814 3d2b5207cb2f8faeb22625976953151d)
md5sums_x86_64=(36dd79961502afaef2d5d82f7909400e)
md5sums_i686=(f9a180369f6ceef58cf4f2cc20355ad4)

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
    rm license *.tar.gz
    mkdir -p $pkgdir/opt/$pkgname && cp -aR ./ $pkgdir/opt/$pkgname
    install -D -m644 gnome-config/menu/nutstore-menu.desktop $pkgdir/usr/share/applications/nutstore.desktop
    install -D -m644 app-icon/nutstore.png $pkgdir/usr/share/icons/hicolor/64x64/apps/nutstore.png
}
