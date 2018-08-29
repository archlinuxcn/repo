# Maintainer: Eli Schwartz <eschwartz@archlinux.org>

pkgname=lastpass
pkgver=4.17.0.4
pkgrel=1
_universalver=4.1.51
_chromever=4.1.52
_amo_file=1053588
_crx_id=hdokiejnpimakedhajhdlcegeplioahd
pkgdesc="The Universal LastPass installer for Firefox, Chrome, and Opera"
arch=('i686' 'x86_64')
url="https://lastpass.com"
license=('custom')
makedepends=('unzip')
optdepends=('firefox'
            'chromium'
            'google-chrome'
            'opera')
options=('!strip')
# Apparently, API endpoints are all the rage -- so this isn't actually a file...
source=("${pkgname}-${pkgver}.xpi::https://addons.mozilla.org/firefox/downloads/file/${_amo_file}/"
        "lpchrome-${_chromever}.crx::${url}/lpchrome_linux.crx"
        "lplinux-${_universalver}.tar.bz2::${url}/lplinux.tar.bz2"
        "com.lastpass.nplastpass.json"
        "firefox-com.lastpass.nplastpass.json"
        "lastpass_policy_sources.json"
        "lastpass_policy_install.json"
        "License.txt")
noextract=("${pkgname}-${pkgver}.xpi"
           "lpchrome-${_chromever}.crx")
sha256sums=('936e6aa954fdf617be237d4268451ca30f38c7d3a5208d25a0501c8c450ce2c4'
            '47937f48972b73f024a1e616547405d41e368cb3756f97958423d20d2196762d'
            '22690e30f5670205df2e5508ae799757b81060aa25b33bb115eeea6ba90e4425'
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

    tail -c +307 lpchrome-${_chromever}.crx > lpchrome-${_chromever}.zip
    unzip -qqo lpchrome-${_chromever}.zip -d lpchrome-${_chromever}

    unzip -qqo "${pkgname}-${pkgver}.xpi" -d "${pkgname}-${pkgver}"
}

package() {
    cd "${srcdir}"

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
    install -Dm755 nplastpass$_64 "$pkgdir"/usr/lib/lastpass/nplastpass
    for i in opt/chrome chromium chromium-dev; do
        install -Dm644 com.lastpass.nplastpass.json "$pkgdir"/etc/$i/native-messaging-hosts/com.lastpass.nplastpass.json
        install -Dm644 lastpass_policy_sources.json "$pkgdir"/etc/$i/policies/managed/lastpass.json
    done
    for i in google-chrome chromium ; do
        install -Dm644 lastpass_policy_install.json "$pkgdir"/usr/share/$i/extensions/hdokiejnpimakedhajhdlcegeplioahd.json
    done

    # Opera
    install -Dm755 lpchrome-${_chromever}/libnplastpass${_64}.so "${pkgdir}"/usr/lib/opera/plugins/libnplastpass.so

    install -Dm644 License.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
