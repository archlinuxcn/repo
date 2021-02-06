pkgname=ntfs3-dkms
pkgver=20.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20210205150244.542628-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20210205150244.542628-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20210205150244.542628-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20210205150244.542628-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20210205150244.542628-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20210205150244.542628-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20210205150244.542628-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20210205150244.542628-9-almaz.alexandrovich@paragon-software.com/raw"
        v20_fix.patch)
sha512sums=('55523ce0d3c3790c33fbe73bd396e5e5f1d015608303e497202a232f51af9bb172003cc836880a7fa85163947609281754606067e5e0df79e9630cd6d1821b96'
            '88e9cf87ab809df7753012b0e285beaa902930a02c4140573967289ea34ae5603159a116cafd5a6bda2e29987d146ed32dc19d831ba44b1db8ca23fc2f3d8f12'
            '3abe2a46b4099e50664914a1f743594c1e591a903ed21bd988e615de0a458d53abfb4d4f49064b7838f75f3e335594f5771f79779a0e656855463eb8d434845b'
            '96a05006a7bded3e1ba122c8a4916eb0326d83d6820642f433676fc08063340d9799d69b71a20717bb5032750b909c7e2ad9468a09b85aea8774f3f493a1fdc5'
            '862a8ed7e7c68027eff42d40b4698a3f984e5f5d90a70623b2e83488dc37bb90c38babfe108a73d46baea2b0a7cc63a643d60f48d1b48afa17aaaaa9ddef5a75'
            '725bb2673d1a61463aff61cc1d8fcaac3888b3177e7af75bed464974da0cfa07383628ce863bb214e9c48969f0d978cbbd845dcfbc971ef850f08af3eb3eb740'
            'd2366ffa6108c78a4579a8dbc55cea27006fcdb0a8c60638b7e0d4b78067f4b1450c69030dfdf6daf077b3e827bf052f0fc63aa02a963cd1e6b9914972abe143'
            'eb420dc335e8b522bfcf037c4eb608da254e570d4d41ea6b688eed6b7ff4e4df560d573d31c51b587139dd82f0b9bce538a964ee6e3431aea78e2b5beb9d03fc'
            '0b4d47b79c6884f657b974700e4709f9527bfdd60b931e10b3402fcea514107a82fcfe81c1a0dcb7e64247b3661ecaa1868e4c1fe1c7f0f0564d591d612085f4'
            'fae49f1a1ae6bcdb56337f43b78467c282a4a7405be75821b8ac41740595cf4b1af091cae59ba26aa6118448d6710494aca7d13a31260316042e49c693e687c3'
            'a799437ebe798fa88d667ddb086f4c752a41cac7aa5e70bd5f1d718c923272eaff7b59deaeac6794f801dc99bcb4f1c6bacbc8e59539c1e7e8180acf4f0a43dd')


prepare() {
  mkdir -p ${pkgname}-${pkgver}
  cd ${pkgname}-${pkgver}
  for patch in "$srcdir/v$pkgver~"*
  do
    patch -p3 -N -i "$patch"
  done
  patch -p3 -N -i "$srcdir/v20_fix.patch"
  patch -p0 -N -i "$srcdir/Makefile.patch"
}

package() {
  mkdir -p "${pkgdir}/usr/src"
  cp -r "${pkgname}-${pkgver}" "${pkgdir}/usr/src/ntfs3-${pkgver}"
  install -Dm644 "${srcdir}/dkms.conf" "${pkgdir}/usr/src/ntfs3-${pkgver}/dkms.conf"
}
