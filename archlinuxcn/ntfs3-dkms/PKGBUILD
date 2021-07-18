pkgname=ntfs3-dkms
pkgver=26.0.0
pkgrel=4
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v${pkgver}~1.patch::https://lore.kernel.org/lkml/20210402155347.64594-2-almaz.alexandrovich@paragon-software.com/raw"
        "v${pkgver}~2.patch::https://lore.kernel.org/lkml/20210402155347.64594-3-almaz.alexandrovich@paragon-software.com/raw"
        "v${pkgver}~3.patch::https://lore.kernel.org/lkml/20210402155347.64594-4-almaz.alexandrovich@paragon-software.com/raw"
        "v${pkgver}~4.patch::https://lore.kernel.org/lkml/20210402155347.64594-5-almaz.alexandrovich@paragon-software.com/raw"
        "v${pkgver}~5.patch::https://lore.kernel.org/lkml/20210402155347.64594-6-almaz.alexandrovich@paragon-software.com/raw"
        "v${pkgver}~6.patch::https://lore.kernel.org/lkml/20210402155347.64594-7-almaz.alexandrovich@paragon-software.com/raw"
        "v${pkgver}~7.patch::https://lore.kernel.org/lkml/20210402155347.64594-8-almaz.alexandrovich@paragon-software.com/raw"
        "v${pkgver}~8.patch::https://lore.kernel.org/lkml/20210402155347.64594-9-almaz.alexandrovich@paragon-software.com/raw"
        legacy_kernel.patch)
sha512sums=('5b5b487eb66d2f74699cbd10c0c669c0dbbd87c0c8ed1d96685aa5f3eb992fdfe859f0eb7aa3a31ade9e267cf6a9a9df228a760f305ff4a2874f01cd7844bf98'
            '67147d0dc534a9bec5f1761f24ff182add0a8e79aab9c094f78263fb00c8f508e6bdd69b389a2b0d8ae3673007eaad5dc6986cff77ba9e77559d9580b40abac3'
            'a79eea8aaf696324c3e90688af5c7dea6ea359198a2f912fc9057eec7ee3d6a307530352e666f27011a6ccfb6458b8e87e4091ad7a9f31b61da85aa287a19753'
            '17b5154a1de598975d4e77805273ecda8d9d7bf439386e1f0ab8c5d90177bfde451ab4448752cc908e7456f3231399d20b9a809104369db08702b6964f449cc9'
            '6432424ff5f589f3af96656110449d71eb1030fa0e2bf967b178b20cb82c848eb80a049ff9ba32f2bd8dd94df16216972acedbadbe47870316af786b6ebd1db4'
            '1768395281a3a15d03757ceece875b335616aec44f2aa8b2a78755942e87804accaad164f1681bfa3a9cef397cfc24580e8a9e357b1bc43ae2466ee051aac2e7'
            '5bbbc24e2b147794c4b0333bd850908eb86c343a31cf96619b05fda8fb475c5e16fac03ddb8f600084c53538f40510c7fec8d667cd28b9426a8cf28ebf27ad36'
            '99b51749a18dcbf304b118a5f5426962e59929aaae9a9b0328b66bd779d35f91712fd02ae22884e785344fa8ec34ffa50f6710b0054b71a43f98255b35308015'
            '9ab39282b83d282aaa33f8c40ff6224a5af990505681a34deee0e958887c9ca9e4dc173681c52854e665ebcd42308c7ab3292666b24e73f61ee604452fba3005'
            '8d820df6c472869a6bf7b7173a706f3f0ce629c3bd243a131ffcac08a17a5b13da2757715508a9c13a1914652eb8b653d53b0497756111c4e8aa5345cbd14029'
            '374c6fa524defb5dcac093493bc7526e43ca9fe07602357fb51df4a26b02280ba4f2d764d3ba2ba2b32d5318ef466f3e0b6cbfdad1cdac0b04c31e8543114e33')


prepare() {
  mkdir -p "${pkgver}"
  cd "${pkgver}"

  for patch in "${srcdir}/v${pkgver}~"* ; do
    patch -p3 -N -i "${patch}"
  done

  patch -p0 -N -i "${srcdir}/Makefile.patch"
}

package() {
  local dest="${pkgdir}/usr/src/ntfs3-${pkgver}"
  mkdir -p "${dest}"
  cd "${dest}"
  cp -r "${srcdir}/${pkgver}/"* ./
  cp "${srcdir}/dkms.conf" ./
  mkdir -p "./patches"
  cp "${srcdir}/legacy_kernel.patch" "./patches/"
}
