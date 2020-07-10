# Maintainer: Eli Schwartz <eschwartz@archlinux.org>

pkgname=lastpass
pkgver=4.51.0.1
pkgrel=1
_universalver=4.1.59
_chromever=4.17.0.4
_amo_file=3601545
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
sha256sums=('5ab2106cc70b8dbf84a7f400ce97155e68d3c619a762da46cb462ccbb5ec507f'
            '905474aceb9998ba25118c572f727336d239a146aad705207f78cacf9052ea29'
            'e8eb3b585809d6644807727c5bd0a74ead96dd2c5a7e6d2ce29e0b6ea28b9e59'
            '82af9e9296f92e92ca325449e0c2b2deb3c21f65afea45aeb823090cb32aad76'
            'f82b920620575654fcbc0baf9b5d6c275835cbfc05b779ad309de5c6411c8bc9'
            '1c061cb5352d84dd6cde4dd6ce3889d41a31fd38acc4d97a7d69709e3d5ac693'
            '17a871edf1134c498f6e91465f5b3138ba5af7d822e4c253cda81ab929906388')
b2sums=('9afc154256a91de769a7b90025764ee2ad434b1fed3f40545b8d016e32f853b6b413f428289540eb0307d329958aba8e536309d9843e79b70ccb77457cd67ce8'
        '714fb34708f9dda8dbacfce8e76adf004f1cc966d685c0efbaac7b25c45068bb5595e954e554092852d575f1fedc5f318d05b121bc2ce1aa4888e4bf374f7b96'
        '258c7e2b37d424f8bec7d9932a7d854e8edcc45c5f316dfe1a0a61a2f26460714358f15414946d49b16ad205f029d6ba27641e883de610632c95dece4e032821'
        '6d7576cc4bb96be15073066d07d94981c8914427dcf35d912510566f45d67115b80fca86dd5b038a853518ff51eb50db2e68f68a8834ab4d732b0da54e0e8555'
        '85900c7c9d6c8cd81e334d03a67de31e9bc444f416af1b0d828d63ad84599a4e267971cbd10e381ff1d318dda6abac5e0c7f48f98bd8455b808eb58471982140'
        'e093927964018f60260fff02aa7c8ad1f011d032dfb96db2eb7d7e0c4e2bd185ac321ad0c467ac0bf7d92c0fe1f814d8bda43a30b41bcc8574c0133c57376619'
        'b0bcb7be17134a256ae9ec91de2b907ebd48f55c381348be803f2735b42857968b86efdd31dbde1e6bcd7162c8f3ce787215772af5d31569a28b5ad93e3683eb')

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
