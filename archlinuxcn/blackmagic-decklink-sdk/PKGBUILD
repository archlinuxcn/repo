# Maintainer: Daniel Bermond < gmail-com: danielbermond >

_downloadid='c63b4b939005460b880d5cf8e7885e43'
_referid='8b5333fa8f67452196c9f867a9b94023'
_srcurl="https://www.blackmagicdesign.com/api/register/us/download/${_downloadid}"

pkgname=blackmagic-decklink-sdk
pkgver=11.2
pkgrel=1
pkgdesc='Blackmagic DeckLink SDK'
arch=('any')
url='https://www.blackmagicdesign.com/support/family/capture-and-playback'
license=('custom')
provides=('decklink-sdk')
conflicts=('decklink-sdk')
source=("Blackmagic_DeckLink_SDK_${pkgver}.zip"::"$_srcurl"
        'LICENSE')
sha256sums=('4919b09740cb9cfd64751d4006f826e72fed929b16b52eab67c9cdbad1e9dbb9'
            'cc90e53ac2ef2442d2d0adfe9214119baa31ec080e75c3b087365efdbccc23df')

_useragent="User-Agent: Mozilla/5.0 (X11; Linux ${CARCH}) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/74.0.3729.169 \
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
