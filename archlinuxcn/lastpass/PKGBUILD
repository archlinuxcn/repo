# Maintainer: Eli Schwartz <eschwartz@archlinux.org>

pkgname=lastpass
pkgver=4.21.0.4
pkgrel=1
_universalver=4.1.59
_chromever=4.17.0.4
_amo_file=1179518
_crx_id=hdokiejnpimakedhajhdlcegeplioahd
pkgdesc="The Universal LastPass installer for Firefox, Chrome, and Opera"
arch=('i686' 'x86_64')
url="https://lastpass.com"
license=('custom')
makedepends=('unzip')
optdepends=('firefox'
            'chromium'
            'google-chrome')
options=('!strip')
# Apparently, API endpoints are all the rage -- so this isn't actually a file...
source=("${pkgname}-${pkgver}.xpi::https://addons.mozilla.org/firefox/downloads/file/${_amo_file}/"
        #"lpchrome-${_chromever}.crx::https://clients2.google.com/service/update2/crx?response=redirect&prodversion=68.0.3440.106&x=id%3D${_crx_id}%26uc"
        "lplinux-${_universalver}.tar.bz2::https://download.cloud.lastpass.com/linux/lplinux.tar.bz2"
        "com.lastpass.nplastpass.json"
        "firefox-com.lastpass.nplastpass.json"
        "lastpass_policy_sources.json"
        "lastpass_policy_install.json"
        "License.txt")
noextract=("${pkgname}-${pkgver}.xpi"
           "lpchrome-${_chromever}.crx")
sha256sums=('9e60ccb3892635024be6940596a812180c92d12f2c4a509e941aaea34a5d9e7e'
            '905474aceb9998ba25118c572f727336d239a146aad705207f78cacf9052ea29'
            'e8eb3b585809d6644807727c5bd0a74ead96dd2c5a7e6d2ce29e0b6ea28b9e59'
            '82af9e9296f92e92ca325449e0c2b2deb3c21f65afea45aeb823090cb32aad76'
            'f82b920620575654fcbc0baf9b5d6c275835cbfc05b779ad309de5c6411c8bc9'
            '1c061cb5352d84dd6cde4dd6ce3889d41a31fd38acc4d97a7d69709e3d5ac693'
            '17a871edf1134c498f6e91465f5b3138ba5af7d822e4c253cda81ab929906388')

# 64-bit?
if [[ $CARCH = x86_64 ]]; then
    _64=64
fi

prepare() {
    cd "${srcdir}"

    #tail -c +307 lpchrome-${_chromever}.crx > lpchrome-${_chromever}.zip
    #unzip -qqo lpchrome-${_chromever}.zip -d lpchrome-${_chromever}

    unzip -qqo "${pkgname}-${pkgver}.xpi" -d "${pkgname}-${pkgver}"
}

package() {
    cd "${srcdir}"

    # universal native messaging host
    install -Dm755 nplastpass$_64 "$pkgdir"/usr/lib/lastpass/nplastpass

    # Firefox
    if [[ -f ${pkgname}-${pkgver}/install.rdf ]]; then
        _extension_id="$(sed -n '/.*<em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' ${pkgname}-${pkgver}/install.rdf)"
    else
        _extension_id="$(sed -n 's/.*"id": "\(.*\)".*/\1/p' ${pkgname}-${pkgver}/manifest.json)"
    fi
    _extension_dest="${pkgdir}/usr/lib/firefox/browser/extensions/${_extension_id}"
    # Should this extension be unpacked or not?
    if grep -q '<em:unpack>true</em:unpack>' ${pkgname}-${pkgver}/install.rdf 2>/dev/null; then
        install -dm755 "${_extension_dest}"
        cp -R ${pkgname}-${pkgver}/* "${_extension_dest}"
        chmod -R ugo+rX "${_extension_dest}"
    else
        install -Dm644 ${pkgname}-${pkgver}.xpi "${_extension_dest}.xpi"
    fi

    # This cannot use the same (unified) file as chromium. Although chromium
    # ignores the Mozilla-specific key in *its* native messaging hosts
    # description, and continues to work, Firefox refuses to recognize the
    # binary plugin if unknown (chromium-specific) keys are present.
    install -Dm644 firefox-com.lastpass.nplastpass.json "$pkgdir"/usr/lib/mozilla/native-messaging-hosts/com.lastpass.nplastpass.json

    # Chrome(ium)
    for i in opt/chrome chromium chromium-dev; do
        install -Dm644 com.lastpass.nplastpass.json "$pkgdir"/etc/$i/native-messaging-hosts/com.lastpass.nplastpass.json
        install -Dm644 lastpass_policy_sources.json "$pkgdir"/etc/$i/policies/managed/lastpass.json
    done
    for i in google-chrome chromium ; do
        install -Dm644 lastpass_policy_install.json "$pkgdir"/usr/share/$i/extensions/${_crx_id}.json
    done

    # Opera
    # Plugin does not exist in Chrome Webstore version of .crx, install
    # instructions claim to use that, no viable solution at the moment so this
    # is disabled until an Opera user is motivated to acquire a source.
    #install -Dm755 lpchrome-${_chromever}/libnplastpass${_64}.so "${pkgdir}"/usr/lib/opera/plugins/libnplastpass.so

    install -Dm644 License.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
