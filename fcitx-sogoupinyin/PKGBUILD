# Maintainer: Vanitas <ssbianjp [AT] gmail.com>
# Contributor: Jove Yu <yushijun110 [AT] gmail.com>
# Contributor: csslayer <wengxt [AT] gmail.com>
# Contributor: Felix Yan <felixonmars [AT] gmail.com>

pkgname=fcitx-sogoupinyin
pkgver=2.0.0.0072
pkgrel=1
pkgdesc="Sogou Pinyin for Linux"
arch=('x86_64' 'i686')
url="http://pinyin.sogou.com/linux/"
license=('custom')
depends=('fcitx' 'opencc' 'libidn' 'fcitx-qt4' 'lsb-release' 'xorg-xprop')

if [ "${CARCH}" = "i686" ]; then
    _LIB_DIR=i386-linux-gnu
    _ARCH=i386
    _time=1461208026
    md5sums=('898fa8d6f1a5a809bebec631ac22e8c1'
             '60b1dcd637c932cf4f3bfaed797f5401')
else
    _LIB_DIR=x86_64-linux-gnu
    _ARCH=amd64
    _time=1461207453
    md5sums=('accbbd9ba0eea9bafc4da7ff90cc1c13'
             '60b1dcd637c932cf4f3bfaed797f5401')
fi

source=("http://cdn2.ime.sogou.com/dl/index/${_time}/sogoupinyin_${pkgver}_${_ARCH}.deb"
        "sogou-autostart")

package(){
    cd ${srcdir}

    tar xJvf data.tar.xz -C "${pkgdir}"

    mv "$pkgdir"/usr/lib/{$_LIB_DIR/,}fcitx
    rmdir "$pkgdir/usr/lib/${_LIB_DIR}"

    # Avoid "No such key 'Gtk/IMModule' in schema 'org.gnome.settings-daemon.plugins.xsettings'" warning
    sed -i '/Gtk\/IMModule=fcitx/d' "$pkgdir/usr/share/glib-2.0/schemas/50_sogoupinyin.gschema.override"

    rm -r "$pkgdir"/usr/share/keyrings

    ln -s /usr/lib/libopencc.so "$pkgdir"/usr/lib/libopencc.so.1

    install -m755 sogou-autostart "$pkgdir"/usr/bin

    rm "$pkgdir"/etc/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop
    cp "$pkgdir"/usr/share/applications/fcitx-ui-sogou-qimpanel.desktop "$pkgdir"/etc/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop
    sed -i 's/sogou-qimpanel\ %U/sogou-autostart/g' "$pkgdir"/etc/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop
}
