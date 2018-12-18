#Maintainer: Bhoppi Chaw <bhoppi#outlook,com>

pkgname=nutstore
pkgver=4.1.5
pkgrel=1
pkgdesc='a cloud service that lets you sync and share files anywhere.'
arch=(x86_64)
url='https://www.jianguoyun.com/'
license=(custom)
depends=(libappindicator-gtk3 libnotify python-gobject)
optdepends=('nautilus-nutstore: Nautilus plugin')
source=(nutstore license)
source_x86_64=("https://www.jianguoyun.com/static/exe/st/$pkgver/nutstore_client-$pkgver-linux-x64-public.tar.gz")
#source_i686=("https://www.jianguoyun.com/static/exe/st/$pkgver/nutstore_client-$pkgver-linux-x86-public.tar.gz")
sha256sums=('3091740b20ddd31ba4407b8daba1077c4677040cdc47bccfab2f7f3947676384'
            'f3d2861ff48f2d193a4eced23a02b4eba9fab4c1d3f727e934ed7c59f38f0f7e')
sha256sums_x86_64=('9d41854c2d654085c2004b5da738c3ba9152d5de8c15a9fb9d1df8efd2e021a3')

build() {
    cd $srcdir/gnome-config
    sed -i '/Exec=/s|~/\.nutstore/dist/bin/nutstore-pydaemon.py|/usr/bin/nutstore|' menu/nutstore-menu.desktop
    sed -i '/Exec=/s|~/\.nutstore/dist|/opt/nutstore|' autostart/nutstore-daemon.desktop
    cd $srcdir/bin
    python -m compileall .
}

package() {
    cd $srcdir
    install -D -m755 nutstore $pkgdir/usr/bin/nutstore
    install -D -m644 license $pkgdir/usr/share/licenses/$pkgname/license
    rm nutstore license *.tar.gz
    mkdir -p $pkgdir/opt/$pkgname && cp -aR ./ $pkgdir/opt/$pkgname
    install -D -m644 gnome-config/menu/nutstore-menu.desktop $pkgdir/usr/share/applications/nutstore.desktop
    install -D -m644 app-icon/nutstore.png $pkgdir/usr/share/icons/hicolor/64x64/apps/nutstore.png
}
