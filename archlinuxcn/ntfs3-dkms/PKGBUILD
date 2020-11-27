pkgname=ntfs3-dkms
pkgver=13.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/patchwork/patch/1342503/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/patchwork/patch/1342506/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/patchwork/patch/1342501/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/patchwork/patch/1342504/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/patchwork/patch/1342502/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/patchwork/patch/1342498/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/patchwork/patch/1342505/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/patchwork/patch/1342499/raw")
sha512sums=('ab49381b37714bc61b17c5a4d857aac776a674574e8dbd46738eab438eef984b7762430cac05860038d8a875d5538347a1e1176acfd2169d9b5a640a9ef04d7c'
            'd4d2eb4f628642074b841ddab238a68f6cef0a0f8c039aae0a12e8d02f14b9fca891f1608f3b94fad4e2f9fbc0c729a23a51a4d28fc1fd8e4e312459bef06b7f'
            '9db431b6d394fcb5c21dbfcd9f4fc09447b9d5f784032d6ff2fd727dbf17004879232af32c0a22c353fce90a248f8e1a1ea2cc46eaf8dbf28176f4fd63d49ebe'
            '280b9421b9a6aaca1d24b1fe93bdc46f42990e8b2e837e648807e99e75be3c862a5412153e8fbb7618449253f944830388a41652e4b16d17878d8041be4ea8eb'
            '17d1e267baca8ba75f5245726d1815e74a2ef8dfe18c6c08118a2f0f125c2ace98ac7ab70d017be51a0fc40236c59faac6813efc523270f52668a3978f1c343d'
            '6507d2a3ee46194649f4b9c281366f4c921ecfed0c48df1659ce323c31e4d08eb0c03efcda57928dc2e64f959577d9a217e1ce394e56e3f32cae081ebbbb1d8b'
            'ea4afcd3daf4e401bb3e05dcc0fae5560b2ab45f7d6d2f60dd6373095df5686d84b471f8bfad791ddb3869a5c480d98e9695cf80f0caad5a8aeeb390e4ef2cd1'
            '67c5b0d58a9c9ae76bc00c05110a16354da9c63f68a22462e58aaa5c559d25f2da04aaa7f7506a4bdf243a058a381712b7f28752fe52a06ad321cb892a41485a'
            'e8df577d6741624f246e9517d2be3eadb5f77ce8382e3d785a5294fd078139b25011ec1b8b8895d8d963085c626290ee8592d89713e167baf3bf6974c4707426'
            '7e7b73cf9b920b58892343de442ed5c41e27d92e8b31cb47c95e0b4851312ef667535203103f0415522115f670a0c739125783743f86a9a24bd27ba6a4cbfd9a')


prepare() {
  mkdir -p ${pkgname}-${pkgver}
  cd ${pkgname}-${pkgver}
  for patch in "$srcdir/v$pkgver~"*
  do
    patch -p3 -N -i "$patch"
  done
  patch -p1 -N -i "$srcdir/Makefile.patch"
}

package() {
  mkdir -p "${pkgdir}/usr/src"
  cp -r "${pkgname}-${pkgver}" "${pkgdir}/usr/src/ntfs3-${pkgver}"
  install -Dm644 "${srcdir}/dkms.conf" "${pkgdir}/usr/src/ntfs3-${pkgver}/dkms.conf"
}
