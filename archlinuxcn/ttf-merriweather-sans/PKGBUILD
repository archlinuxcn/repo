# Maintainer: Tyler Swagar <buttpickle69@shaw.ca>

pkgname=ttf-merriweather-sans
_commit='8a1b078e3aeec6aecc856c3422898816af9b9dc7'
pkgver=1.008
pkgrel=2
pkgdesc='A sans-serif typeface that is pleasant to read on screens by Sorkin Type Co'
arch=('any')
url='https://fonts.google.com/specimen/Merriweather+Sans'
license=('custom:SIL Open Font License v1.1')
depends=('xorg-fonts-encodings')
conflicts=('ttf-google-fonts-opinionated-git' 'ttf-merriweather-sans-ib')
source=("MerriweatherSans-Black-${pkgver}.ttf::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/fonts/ttfs/MerriweatherSans-Black.ttf"
        "MerriweatherSans-Bold-${pkgver}.ttf::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/fonts/ttfs/MerriweatherSans-Bold.ttf"
        "MerriweatherSans-BoldItalic-${pkgver}.ttf::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/fonts/ttfs/MerriweatherSans-BoldItalic.ttf"
        "MerriweatherSans-Italic-${pkgver}.ttf::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/fonts/ttfs/MerriweatherSans-Italic.ttf"
        "MerriweatherSans-Light-${pkgver}.ttf::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/fonts/ttfs/MerriweatherSans-Light.ttf"
        "MerriweatherSans-LightItalic-${pkgver}.ttf::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/fonts/ttfs/MerriweatherSans-LightItalic.ttf"
        "MerriweatherSans-Regular-${pkgver}.ttf::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/fonts/ttfs/MerriweatherSans-Regular.ttf"
        "MerriweatherSans-UltraBoldItalic-${pkgver}.ttf::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/fonts/ttfs/MerriweatherSans-UltraBoldItalic.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://github.com/SorkinType/Merriweather-Sans/raw/${_commit}/OFL.txt")
sha256sums=('af690e015ff424d071721e6ad6af80f7c6386ba31abb47a2f389f197cb8a8a32'
            '5f81558a46b8c5f4ad6adcaa739f634af47218ae7d9ebe04f927ff6beb50fce0'
            'f19e7d24d08196b48db236c15c267deaae68eaac5cf3f867d3de8a476bda61e9'
            '00c8297889d599864cc7f7ae55c4cd2719101c86bd791f6ef5b74d4bbe7bd14b'
            '3135cab712b7eede2cab5068c01cd819673e5a4274a8469d75a01265c5bbcc9f'
            '6323a0925f394f40e893791462a22ef32368bae8648cf90aaac501b4e304927a'
            '38919382a6e9c750affc4c851b7dac2d66c3c1e264b5676544ab0692fdae6369'
            '582dc62d2b45bdd565a905e13e182fb0996b9687b11c6687688bb7083ed19779'
            '6f3f956d48ae50afab7931fd82b88187d84d12d3a70d279e7ff3e2c963e11c43')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 MerriweatherSans-Black-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/MerriweatherSans-Black.ttf"
  install -m 644 MerriweatherSans-Bold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/MerriweatherSans-Bold.ttf"
  install -m 644 MerriweatherSans-BoldItalic-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/MerriweatherSans-BoldItalic.ttf"
  install -m 644 MerriweatherSans-Italic-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/MerriweatherSans-Italic.ttf"
  install -m 644 MerriweatherSans-Light-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/MerriweatherSans-Light.ttf"
  install -m 644 MerriweatherSans-LightItalic-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/MerriweatherSans-LightItalic.ttf"
  install -m 644 MerriweatherSans-Regular-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/MerriweatherSans-Regular.ttf"
  install -m 644 MerriweatherSans-UltraBoldItalic-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/MerriweatherSans-UltraBoldItalic.ttf"
  install -Dm644 ${pkgname}-${pkgver}-OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
