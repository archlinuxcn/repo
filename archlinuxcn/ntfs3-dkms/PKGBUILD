pkgname=ntfs3-dkms
pkgver=18.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20210122140159.4095083-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20210122140159.4095083-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20210122140159.4095083-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20210122140159.4095083-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20210122140159.4095083-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20210122140159.4095083-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20210122140159.4095083-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20210122140159.4095083-9-almaz.alexandrovich@paragon-software.com/raw")
sha512sums=('3d47cccc7914b42dbcc670bcb9144f948a42d0ba57843140373afec0483570597b4b4ad61753742b282626f50aec25cabbeb88aadc94d2cb67ec1c612b6ed41d'
            '615642fcd0e08dae34ad6c0831f699ee015d380b5b1694633ec14abe9b2c4b4f9ebf7191e4b96bfcba2cbea7ec52324c43f60d358311fbfbed0de77cbbefd4f0'
            '3020b87db81f4a5a251a6828e4b3740a959e9a80a3ee6d7daf5de835e989c802ee045dacd15e9b177964ee8fdc78897a8c66bcc118d892a731130980b6d3f222'
            '24fcb531496a75cb9f4d49dadbc5f5586944242ba732a24c04333ff5f9935be24e60f45877f217068d393cca97d7d80106a4c2d8f197fd4e0aef0ba049d64b9d'
            '90d111d67b93e95930454500870a9807450565fc184eccc79481627c0b245436679a91b4903e9f98b68505092bde95bb332d156fc6c7b5fe35d34f951c381fa2'
            '2702cce126a7b70f98ea8532c53216503cf8e906e7605fc0759114fedc4f3a410aedecde3a93419d850298417b790845dfc50d13a49763985b3169fbbdf8dac8'
            '0972022364c532e89b4a67b4ce84c6b3edbf2f10acad88230e091c385dcd88d8799872a950248141360700a81db36c1335363a90926e6ddee0fa4646bd5be7ca'
            '2282f2470f3cdc1340c04e4ab4e0db257699afef49deabc546c03254056307ba7530e15aeb6a21cecdffbc25676490fecd81486fda91b593e23a7ab688b8c259'
            '1e8ff7fabcdbc60ad09c5d749fb3b3e4f8114177950c6a4e2e22bcb0ecb29788810baf07c6f188e35ac7cdfc2bdee440dc3a08f3668f11e57fec4d397b04f3ac'
            'c504180a8cd032e60a910106f324e78379ad8783195d3fb7df2977823263063b81ee17c630c2ce237eb8a802135e17a352b6b425a8d01c7f93b3f1dbf748835a')


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
