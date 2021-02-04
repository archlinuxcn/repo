pkgname=ntfs3-dkms
pkgver=19.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20210128090455.3576502-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20210128090455.3576502-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20210128090455.3576502-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20210128090455.3576502-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20210128090455.3576502-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20210128090455.3576502-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20210128090455.3576502-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20210128090455.3576502-9-almaz.alexandrovich@paragon-software.com/raw")
sha512sums=('3d47cccc7914b42dbcc670bcb9144f948a42d0ba57843140373afec0483570597b4b4ad61753742b282626f50aec25cabbeb88aadc94d2cb67ec1c612b6ed41d'
            'f98f7ebeba0e3aa0555801b05d7d8e54139ae4b9c4443c67475c17fd1cde91126f1a275ab5ad7ea48a8161fb3a210986237da1fa1c9dfd315cf108ebdc645633'
            '5d084ca098eb0753ec325a04b02f0c92a6c8e25c2e590539868e56dae1185327aa232300e3ad382ea5a5a9a6a044b827762891d394745774e553e82cf0ef8099'
            '9949726ea2e0ec98ccfae30aeb99f801245d0912269498a9c4ebc1fa8cf0ed205d7518cb5626aead41c64578131559cf6c7195cca104184dc1c658fae3be0180'
            '2268105de76feebb684e42d5a1885ca53cbd308d8ddc5d749126339218fb39f7867a36624af240e2c7ec6d3fda049c5e947815ae262f2c083c1ae6c6beb9bbe1'
            'fddbda4c4a3d858f6740673c69613eacc4fca51ad564770588a363f2f09f2225a000f1507fca9f5dda723f4250438e9c3b6373fb2e98c0cf0ba197e9b4ef2c99'
            'c77ba7eb033286963569ab32a457ff613b6244eafb08c4ab9c5a8945ff058caccd5af65885c34a7caa82b09821edc9b6ed562c7def19f1bce2f5369fa5b6d2ff'
            'a78ef11cef86d563148669bab42b2bf8ac756c9de0a796dacc36810fc8f19484f74ae8c91ec063188b219d7201bee8bd98258f3b1341f93210a361d06212c149'
            'fcf2d17aeb22c00b3886150f970e2adf61a4cc00efe6185ac935164a32ad69c95a0be6d03152b3f3de58e3a701d8c25c7c3d340fc56c19d1995eb5df1041a8a3'
            'b894ee23f7722e2515048dadbd07605a6cf93fbe9194891b0038374c4bce9e00b811249f8c945c83bf5c84eaea57f1c78aa87834d5dde412e67f669ce67f32fd')


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
