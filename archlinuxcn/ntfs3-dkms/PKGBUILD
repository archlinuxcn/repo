pkgname=ntfs3-dkms
pkgver=14.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/patchwork/patch/1349515/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/patchwork/patch/1349516/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/patchwork/patch/1349512/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/patchwork/patch/1349517/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/patchwork/patch/1349514/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/patchwork/patch/1349513/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/patchwork/patch/1349518/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/patchwork/patch/1349509/raw")
sha512sums=('989009d7bc7dba6e4cc380bbd660e2c50b20cb312b678031da9fe4a330b92a4b8cd5bcaa8b6de3e4972dfdcb8db2e750c82628b3449350cb8c67f9f4df1cd977'
            'af96b27a8033e066022facaaae0ebf2a058ce82c354b97fb66e3e54c50887ecaa27a3e29a2c104fdbc4b8c79e3ec039e743ba1ccee6bf4b8edbc491188851a2c'
            '071b7c16394730ba46a0e6f1bcfea16a7c8e192485648c9e429c3924ee97d0271a67948f7f6c593f153a77800a071f3742c5ca29e3cf02bc3d7ebf52be6915ed'
            '2bebb6565f596b38f5c84da70b8235cbf776c5c157aa9fa0cb13f838455f057bae65616552b55b2a53cd583f8821ebb7b66ad80cb948eb505fe464701c8ccbab'
            '17d1e267baca8ba75f5245726d1815e74a2ef8dfe18c6c08118a2f0f125c2ace98ac7ab70d017be51a0fc40236c59faac6813efc523270f52668a3978f1c343d'
            '1acbb407b47ee200061d9b60b0aabc84795032f65b58777685db87a32a4bfc1f839b677af75f2d99fd03352f9ce68ee2596552502dfbaf1bd16e93d3dac7b602'
            'dd895eb3775c45e36a824ff9bd8c9b6ddaa4fa1128d3ea539cd6b375d84044c22ced1958e0c7902125ccf66b8e82cca11d9d3c0ddd9458b44211237dda49e114'
            'f689e0959cc37f8b97e2078e4d5c087d5774f17d04ab8a10cdec0939ecc2413b1a57b3c59ee697f5da6df2fabc5789dae2f1d0e20d7c34a1410be6c6b4c84036'
            'e8df577d6741624f246e9517d2be3eadb5f77ce8382e3d785a5294fd078139b25011ec1b8b8895d8d963085c626290ee8592d89713e167baf3bf6974c4707426'
            '9498e642e3bdcdccf9bb11a83333c7c11bb9a9252bc38058cf132a1d36b9e70411f725d18e376d22010e703450f8c32ead61344090dbeecfdf77c516dd7c851a')


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
