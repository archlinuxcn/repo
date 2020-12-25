pkgname=ntfs3-dkms
pkgver=16.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20201225135119.3666763-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20201225135119.3666763-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20201225135119.3666763-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20201225135119.3666763-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20201225135119.3666763-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20201225135119.3666763-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20201225135119.3666763-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20201225135119.3666763-9-almaz.alexandrovich@paragon-software.com/raw")
sha512sums=('989009d7bc7dba6e4cc380bbd660e2c50b20cb312b678031da9fe4a330b92a4b8cd5bcaa8b6de3e4972dfdcb8db2e750c82628b3449350cb8c67f9f4df1cd977'
            '6fab40baa5cd377a51e5934f7f7711e4155c795371c51e4715162108fc44a86817a08d88479720e2fade6eafd7f02c62c52f3e40232697a0feb3de9481d899aa'
            'a2a888306647d61ba93eb8b265968f1611392313dfdc53f172795603cdce34364cd132f1ac78cfc08152e73db6a104cb8e03d984517f4fb1af4d445767193b43'
            'badc07260145ebe94b9a6020c8cc04d9866d2dc3212927c7427c82576e072f868319f8d104b3bed2b7d6585c5c2394d6f5fc970a0551167762d8ed8b8962ba66'
            'f76a5a2ddd01540937d6d38cfa5bb2cff918858f29e32ed29605f09fac1fbc67188f11474bdbf09bb23d5c1eaf360a26a359835c051cbc6636e32e975534da26'
            '7b41ac091b595fb090531923a0a7c03dd69a4f77fc16d2fc64ea18bb0888f88a560dba3f51f2719e18db19bff15642275901b4721115be404daf150bc993d17d'
            '18f326fc8791e41999be666d4b57dbbe3a9dd897254e2f517bbb02c8af61d1616bb5a1672106b2a2bf0d9bd15f6cae71edf9f1c9105341ec82a4de10ea1ece57'
            '86a8a83a39fc3a9a42bba4c4cf8aa06819a915753f8ed0bcb2241ea7d23dd3e565c5b5ba28ddc58fbf7edcd08121986f4cfe13b8b342ac03edbb54bec8b1f276'
            '294c0a44a28f3052886d7db02daf07cae5caff8495ee06b79158d64bcf319186aeff8e1d08a679d0fb99c1744cc02b865d6dc6db697e8643fbe93581cc8f3be1'
            '741380cc7338f7949db3887cc2f429cfff44dff182808ea831fe07e91aacc9219f67a8155832829cbec1609e60cbe7ed8fb6c2e7c6168db1a3314642efedb475')


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
