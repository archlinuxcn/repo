pkgname=ntfs3-dkms
pkgver=21.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20210212162416.2756937-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20210212162416.2756937-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20210212162416.2756937-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20210212162416.2756937-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20210212162416.2756937-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20210212162416.2756937-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20210212162416.2756937-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20210212162416.2756937-9-almaz.alexandrovich@paragon-software.com/raw"
        kernel_version_fix.patch)
sha512sums=('55523ce0d3c3790c33fbe73bd396e5e5f1d015608303e497202a232f51af9bb172003cc836880a7fa85163947609281754606067e5e0df79e9630cd6d1821b96'
            '6954d129fc1ed01fea288c65d41bcac4caac537d3632aa323b531e095b673428ae38bb480b68ef05b5b2a3333678a61a982a54d40e9ce1d2ca48985a29557f1c'
            '01ca8bd32d3f3a740f2ec8d83ae14c0e1cda2bdde054a62b9382715a95c0ea37516ee92c448db039b0c6209e142bfecdba6cb3025cd3eaf9375349396ddeed83'
            '6361f3ada2f977859ec79ded80438476c6f74ebef2f22760ab81bd97f183888f270b235d1afbcef8c41a55de261cbbb5030be49aedad90920037a3a370072e21'
            'a681cf4b0ec10aa4b8d59824d179de697b6e24403b72022a352f6f4bb85441c60a23c34d2a8c437952ebc2d155fa0862f75e933bf3ae2c000bc0c2b8f5d22b6a'
            'cbb32352ee33f687b2c88b83243ea36bfe9387ebba13173412ddb53531c4b7b18be8668108e51cf10ff36cec16a36cf497d6d2957208b95d6ea7bd36c0670008'
            'f7646039872ade9cde19fb9be74c4fe8b676ab8fd0bb83c50737afae73c48424fc4fcaa94168b19127a2710dca94ad14969d0f4c57b08d1fd434195439da8912'
            '9715dbf4c294bd59f666a8dcae330407e7da7329c6b5b15781b5ee6401ee6cbbc54a0accda93d819c0007a7df27721d3a7ae8c77b9def8d4959f0fef97b663a5'
            '11f108c0d1f91cdbf100e9f572132a3e0ca9ff2e3f131f82a053e20b20e430cb38e09a8ed385404dbe66c46fa1c930c68eba3d805f864fa66f60985d79d98176'
            '525d4ef57365f5a813fa9e17c8f62b3b664def6c1db94c4d88bf8c35504743823c29db003146204d6ca9401ef1360cadc8cb40373828a3c85461790d3ea2dc0c'
            '12e2df3b2646371852c7370726b2635d023385edeeb4fdd4e8d0585f88388d4b9041bf30e8ae1c9fb5fc84e032a5f553576b8ed21d5612ed204b7dec2174010f')


prepare() {
  mkdir -p ${pkgname}-${pkgver}
  cd ${pkgname}-${pkgver}
  for patch in "$srcdir/v$pkgver~"*
  do
    patch -p3 -N -i "$patch"
  done
  patch -p3 -N -i "$srcdir/kernel_version_fix.patch"
  patch -p0 -N -i "$srcdir/Makefile.patch"
}

package() {
  mkdir -p "${pkgdir}/usr/src"
  cp -r "${pkgname}-${pkgver}" "${pkgdir}/usr/src/ntfs3-${pkgver}"
  install -Dm644 "${srcdir}/dkms.conf" "${pkgdir}/usr/src/ntfs3-${pkgver}/dkms.conf"
}
