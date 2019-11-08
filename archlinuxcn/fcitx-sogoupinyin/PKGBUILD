# Maintainer: Bian Jiaping <ssbianjp [AT] gmail.com>
# Contributor: Jove Yu <yushijun110 [AT] gmail.com>
# Contributor: csslayer <wengxt [AT] gmail.com>
# Contributor: Felix Yan <felixonmars [AT] gmail.com>

pkgname=fcitx-sogoupinyin
pkgver=2.3.1.0112
_time=1571302197
pkgrel=1
pkgdesc="Sogou Pinyin for Linux"
arch=("x86_64")
url="https://pinyin.sogou.com/linux/"
license=("custom")
depends=("fcitx" "opencc" "libidn11" "lsb-release" "xorg-xprop" "qtwebkit")

source=("sogou-autostart"
	"http://cdn2.ime.sogou.com/dl/index/${_time}/sogoupinyin_${pkgver}_amd64.deb")
sha256sums=("4357c28ba35d9441e47cc5c9a4c5f1ccbb8957cb3434212a609201aee485c092"
           "4e15aad4785b30f35a8d891de878abe8892ffaea1882f570fec74fd821d0c448")

package(){
    cd ${srcdir}

    tar -xJvf data.tar.xz -C "${pkgdir}"

    mv "$pkgdir"/usr/lib/*-linux-gnu/fcitx "$pkgdir"/usr/lib/
    rmdir "$pkgdir"/usr/lib/*-linux-gnu

    # Avoid warning "No such key "Gtk/IMModule" in schema "org.gnome.settings-daemon.plugins.xsettings""
    sed -i "s#Gtk/IMModule=fcitx#overrides={"Gtk/IMModule":<"fcitx">}#" "$pkgdir"/usr/share/glib-2.0/schemas/50_sogoupinyin.gschema.override

    rm -r "$pkgdir"/usr/share/keyrings
    rm -r "$pkgdir"/etc/X11

    # install -m755 sogou-autostart "$pkgdir"/usr/bin

    # Do not modify $pkgdir/etc/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop, as it is
    # a symlink to absolute path "/usr/share/applications/fcitx-ui-sogou-qimpanel.desktop"
    # sed -i "s/sogou-qimpanel\ %U/sogou-autostart/g" "$pkgdir"/usr/share/applications/fcitx-ui-sogou-qimpanel.desktop
}
