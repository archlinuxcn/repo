# Maintainer: Daniel Bermond < gmail-com: danielbermond >

_downloadid='9bfd3eb624fc47b38a985893fcc1c8ac'
_referid='271210a0edb54303a887bd31cb8d17b0'
_srcurl="https://www.blackmagicdesign.com/api/register/us/download/${_downloadid}"

pkgname=blackmagic-decklink-sdk
pkgver=11.3
pkgrel=1
pkgdesc='Blackmagic DeckLink SDK'
arch=('any')
url='https://www.blackmagicdesign.com/support/family/capture-and-playback'
license=('custom')
provides=('decklink-sdk')
conflicts=('decklink-sdk')
source=("Blackmagic_DeckLink_SDK_${pkgver}.zip"::"$_srcurl"
        'LICENSE')
sha256sums=('c465b5de84d7f0caca51e7ab54581c1c82c9e937b6debae6b157e23501046730'
            'cc90e53ac2ef2442d2d0adfe9214119baa31ec080e75c3b087365efdbccc23df')

_useragent="User-Agent: Mozilla/5.0 (X11; Linux ${CARCH}) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/76.0.3809.100 \
                        Safari/537.36"

_reqjson="{ \
    \"platform\": \"Linux\", \
    \"country\": \"us\", \
    \"firstname\": \"Arch\", \
    \"lastname\": \"Linux\", \
    \"email\": \"someone@archlinux.org\", \
    \"phone\": \"202-555-0194\", \
    \"state\": \"New York\", \
    \"city\": \"AUR\", \
    \"hasAgreedToTerms\": true, \
    \"product\": \"Desktop Video ${pkgver} SDK\" \
}"

_reqjson="$(  printf '%s' "$_reqjson"   | sed 's/[[:space:]]\+/ /g')"
_useragent="$(printf '%s' "$_useragent" | sed 's/[[:space:]]\+/ /g')"
_useragent_escaped="${_useragent// /\\ }"

DLAGENTS=("https::/usr/bin/curl \
              -gqb '' -C - --retry 3 --retry-delay 3 \
              -H Host:\ sw.blackmagicdesign.com \
              -H Upgrade-Insecure-Requests:\ 1 \
              -H ${_useragent_escaped} \
              -H Accept:\ text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8 \
              -H Accept-Language:\ en-US,en;q=0.9 \
              -o %o \
              --compressed \
              $(curl \
                  -s \
                  -H 'Host: www.blackmagicdesign.com' \
                  -H 'Accept: application/json, text/plain, */*' \
                  -H 'Origin: https://www.blackmagicdesign.com' \
                  -H "$_useragent" \
                  -H 'Content-Type: application/json;charset=UTF-8' \
                  -H "Referer: https://www.blackmagicdesign.com/support/download/${_referid}/Linux" \
                  -H 'Accept-Encoding: gzip, deflate, br' \
                  -H 'Accept-Language: en-US,en;q=0.9' \
                  -H 'Authority: www.blackmagicdesign.com' \
                  -H 'Cookie: _ga=GA1.2.1849503966.1518103294; _gid=GA1.2.953840595.1518103294' \
                  --data-binary "$_reqjson" \
                  --compressed \
                  "$_srcurl"
              )"
)

package() {
    # directories creation
    mkdir -p "${pkgdir}/usr/include"
    mkdir -p "${pkgdir}/usr/share/doc/${pkgname}"
    
    # headers
    cd "${srcdir}/Blackmagic DeckLink SDK ${pkgver}/Linux/include"
    install -D -m644 * "${pkgdir}/usr/include"
    
    # documentation
    cd "${srcdir}/Blackmagic DeckLink SDK ${pkgver}"
    install -D -m644 *.pdf "${pkgdir}/usr/share/doc/${pkgname}"
    
    # license
    install -D -m644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
