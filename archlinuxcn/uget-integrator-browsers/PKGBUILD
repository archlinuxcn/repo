#Maintainer : Sasasu <lizhaolong0123@gmail.com>
pkgbase=uget-integrator-browsers
pkgname=(uget-integrator-chrome uget-integrator-chromium uget-integrator-opera uget-integrator-firefox uget-integrator-libreworlf)
arch=('any')
url="https://github.com/ugetdm/uget-integrator"
license=('GPL3')
depends=('uget-integrator')
pkgver=1.0.0
pkgrel=4
makedepends=()
source=("ugetdm-chrome-$pkgver::https://raw.githubusercontent.com/ugetdm/uget-integrator/v$pkgver/conf/com.ugetdm.chrome.json"
        "ugetdm-firefox-$pkgver::https://raw.githubusercontent.com/ugetdm/uget-integrator/v$pkgver/conf/com.ugetdm.firefox.json")
md5sums=('09303ac5e041a9788cf0748929cbd827'
         '14049191a778e186d6805b65972245d9')

build() {
    cd "$srcdir"
}

#for Google Chrome
package_uget-integrator-chrome(){
    optdepends=('google-chrome: the browser')
    pkgdesc="Configuration to connect Google Chrome with uget-integrator"
    install="chrome.install"
    cd "$srcdir"
    mkdir -p "$pkgdir/etc/opt/chrome/native-messaging-hosts"
    install -m644 "ugetdm-chrome-$pkgver" "$pkgdir"/etc/opt/chrome/native-messaging-hosts/com.ugetdm.chrome.json
}

#for Chromium and Vivaldi
package_uget-integrator-chromium(){
    optdepends=('chromium: the browser')
    pkgdesc="Configuration to connect Chromium with uget-integrator"
    install="chrome.install"
    cd "$srcdir"
    mkdir -p "$pkgdir/etc/chromium/native-messaging-hosts"
    install -m644 "ugetdm-chrome-$pkgver" "$pkgdir"/etc/chromium/native-messaging-hosts/com.ugetdm.chrome.json
}

#for Opera
package_uget-integrator-opera(){
    optdepends=('opera-beta: the browser beta version' 'opera-developer: the browser developer version')
    pkgdesc="Configuration to connect Opera with uget-integrator"
    install="opera.install"
    cd "$srcdir"
    mkdir -p "$pkgdir/etc/opera/native-messaging-hosts"
    install -m644 "ugetdm-chrome-$pkgver" "$pkgdir"/etc/opera/native-messaging-hosts/com.ugetdm.chrome.json
}

#for Firefox
package_uget-integrator-firefox(){
    optdepends=('firefox: the browser')
    pkgdesc="Configuration to connect Firefox with uget-integrator"
    install="firefox.install"
    cd "$srcdir"
    mkdir -p "$pkgdir/usr/lib/mozilla/native-messaging-hosts"
    install -m644 "ugetdm-firefox-$pkgver" "$pkgdir"/usr/lib/mozilla/native-messaging-hosts/com.ugetdm.firefox.json
}

#for LibreWolf, thanks quentin
package_uget-integrator-libreworlf(){
    optdepends=('librewolf: the browser')
    pkgdesc="Configuration to connect LibreWolf with uget-integrator"
    install="firefox.install"
    cd "$srcdir"
    mkdir -p "$pkgdir/usr/lib/librewolf/native-messaging-hosts"
    install -m644 "ugetdm-firefox-$pkgver" "$pkgdir"/usr/lib/librewolf/native-messaging-hosts/com.ugetdm.firefox.json
}
