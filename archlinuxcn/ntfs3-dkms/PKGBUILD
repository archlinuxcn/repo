pkgname=ntfs3-dkms
pkgver=15.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20201211161844.3590331-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20201211161844.3590331-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20201211161844.3590331-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20201211161844.3590331-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20201211161844.3590331-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20201211161844.3590331-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20201211161844.3590331-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20201211161844.3590331-9-almaz.alexandrovich@paragon-software.com/raw")
sha512sums=('989009d7bc7dba6e4cc380bbd660e2c50b20cb312b678031da9fe4a330b92a4b8cd5bcaa8b6de3e4972dfdcb8db2e750c82628b3449350cb8c67f9f4df1cd977'
            '3896726cdfaef8b5e86ea90336c2069c8b65808aa45e1c7588fca23e04340addcd0dea0cf8bce692e6ca0281dfe5664baab045b04677ca074a0c947e343591c5'
            '42f0469e8a12afcb740cc56cbe556659f40eea1fcedb0d4edba0e274963040e417d9d30a6ce71e1193fbc91e6d22094c48f9cdeaa46f417ee80e2b89743342e4'
            '50f94e40e5d5dc65a7703e81c5f23d02c51b455fc46a5ff090e7a4feb1002192e71c98a9054fad5a15e4d7d972a5aea6a78802e872fd0b17285c89f18ac07f33'
            'a94ef5e81c5a17d8723ff76e777ee20a57575d2e8aa168c49724ab5ffafd9ded26c13cf16216ddb1c21ce8f6bc409a65c45deb2a25e2e210c4d3882a4fcee162'
            'edc8ba83442a7fc27162d4fd838e682962711f13231d4060bf032d0bf36fb7839fa309a00d029705aab1deb426a39f224d3556434cecb0d3173c96460ffff245'
            '6610211fc824cbd5d534ab5cd88f82667c2b0091465ab94c354c10b2e51f15a04cc0ca1e7deacb32675f20fcf6640b760e04ecb0142e1670c4639ac117d067ef'
            'f2dc0e1d8cc7683ab13451b5f246838f93be103837b8f414f822ef2292097d03525e140720438705dfe971d33c485b967e70b022548934f7f2eea105752bbe88'
            '9d60b7903db61a98f129a89bbf30b17a42824fdb55bd8a897cfeb9f24d09ce6e1ae019a62c1774876430104c7def983eb238b7d300d04d9e08abd0dc4b8297f1'
            '70cf2822c31a5bbc44598877b22cc95203df46d7865063e5981d1316514a7e0a85de76be0954b3ac48c3de9dbd8a933b47411248d06bdabf3483d8d6b77bfd02')


prepare() {
  mkdir -p ${pkgname}-${pkgver}
  cd ${pkgname}-${pkgver}
  for patch in "$srcdir/v$pkgver~"*
  do
    patch -p3 -N -i "$patch"
  done
  patch -p0 -N -i "$srcdir/Makefile.patch"
}

package() {
  mkdir -p "${pkgdir}/usr/src"
  cp -r "${pkgname}-${pkgver}" "${pkgdir}/usr/src/ntfs3-${pkgver}"
  install -Dm644 "${srcdir}/dkms.conf" "${pkgdir}/usr/src/ntfs3-${pkgver}/dkms.conf"
}
