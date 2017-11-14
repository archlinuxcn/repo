# Maintainer: Bian Jiaping <ssbianjp [AT] gmail.com>
# Contributor: Jove Yu <yushijun110 [AT] gmail.com>
# Contributor: csslayer <wengxt [AT] gmail.com>
# Contributor: Felix Yan <felixonmars [AT] gmail.com>

pkgname=fcitx-sogoupinyin
pkgver=2.2.0.0102
pkgrel=1
pkgdesc="Sogou Pinyin for Linux"
arch=('x86_64' 'i686')
url="http://pinyin.sogou.com/linux/"
license=('custom')
depends=('fcitx' 'opencc' 'libidn' 'fcitx-qt4' 'lsb-release' 'xorg-xprop' 'qtwebkit')

if [ "${CARCH}" = "i686" ]; then
    _LIB_DIR=i386-linux-gnu
    _ARCH=i386
    _time=1509619879
    _md5_checksum=6845cbfe09d0e1b5a6c62c3c092a9c09
else
    _LIB_DIR=x86_64-linux-gnu
    _ARCH=amd64
    _time=1509619794
    _md5_checksum=2a58e8b4c2ae619e2b3f706665a559d5
fi

source=(
    "http://cdn2.ime.sogou.com/dl/index/${_time}/sogoupinyin_${pkgver}_${_ARCH}.deb"
    "sogou-autostart"
)
md5sums=(
    ${_md5_checksum}
    60b1dcd637c932cf4f3bfaed797f5401
)

package(){
    cd ${srcdir}

    tar xJvf data.tar.xz -C "${pkgdir}"

    mv "$pkgdir"/usr/lib/{$_LIB_DIR/,}fcitx
    rmdir "$pkgdir/usr/lib/${_LIB_DIR}"

    # Avoid "No such key 'Gtk/IMModule' in schema 'org.gnome.settings-daemon.plugins.xsettings'" warning
    sed -i "s#Gtk/IMModule=fcitx#overrides={'Gtk/IMModule':<'fcitx'>}#" "$pkgdir"/usr/share/glib-2.0/schemas/50_sogoupinyin.gschema.override

    rm -r "$pkgdir"/usr/share/keyrings

    ln -s /usr/lib/libopencc.so "$pkgdir"/usr/lib/libopencc.so.1

    install -m755 sogou-autostart "$pkgdir"/usr/bin

    rm "$pkgdir"/etc/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop
    cp "$pkgdir"/usr/share/applications/fcitx-ui-sogou-qimpanel.desktop "$pkgdir"/etc/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop
    sed -i 's/sogou-qimpanel\ %U/sogou-autostart/g' "$pkgdir"/etc/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop
}
