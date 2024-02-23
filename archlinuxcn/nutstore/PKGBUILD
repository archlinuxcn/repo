#Maintainer: Bhoppi Chaw <bhoppi#outlook,com>

pkgname=nutstore
pkgver=6.2.8
pkgrel=1
pkgdesc='a cloud service that lets you sync and share files anywhere.'
arch=(x86_64)
url='https://www.jianguoyun.com/'
license=(custom)
depends=(
    libappindicator-gtk3
    libnotify
    python-gobject
    webkit2gtk
)
optdepends=('nautilus-nutstore: Nautilus plugin')
source=(nutstore license)
source_x86_64=("https://pkg-cdn.jianguoyun.com/static/exe/st/$pkgver/nutstore_client-$pkgver-linux-x86_64-public.tar.gz")
sha256sums=('a4aa358d45b306cbeac449f2256f00a5b81a95197394eba7efa96eaae820cf5b'
            'd320e071403cdad44881beb880f5ccfa8ec0a625718a9f572dce0cc9fff81ade')
sha256sums_x86_64=('532503ed97ff4eb8e4bcfeba10ba652d9674efd9b3bc067da407b75191016f1a')

build() {
    cd $srcdir/gnome-config
    sed -i '/Exec=/s|~/\.nutstore/dist/bin/nutstore-pydaemon.py|/usr/bin/nutstore|' menu/nutstore-menu.desktop
    sed -i '/Exec=/s|~/\.nutstore/dist|/opt/nutstore|' autostart/nutstore-daemon.desktop
    cd $srcdir/bin
    sed -i '/gvfs-set-attribute/s|gvfs-set-attribute|gio set|' nutstore-pydaemon.py
    python -m compileall .
}

package() {
    cd $srcdir
    install -D -m755 nutstore $pkgdir/usr/bin/nutstore
    install -D -m644 license $pkgdir/usr/share/licenses/nutstore/license
    rm nutstore license *.tar.gz
    mkdir -p $pkgdir/opt/nutstore && cp -aR ./ $pkgdir/opt/nutstore
    install -D -m644 gnome-config/menu/nutstore-menu.desktop $pkgdir/usr/share/applications/nutstore.desktop
    install -D -m644 app-icon/nutstore.png $pkgdir/usr/share/icons/hicolor/512x512/apps/nutstore.png
}
