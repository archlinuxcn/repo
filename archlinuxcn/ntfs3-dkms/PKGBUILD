pkgname=ntfs3-dkms
pkgver=23.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20210315144414.3365314-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20210315144414.3365314-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20210315144414.3365314-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20210315144414.3365314-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20210315144414.3365314-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20210315144414.3365314-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20210315144414.3365314-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20210315144414.3365314-9-almaz.alexandrovich@paragon-software.com/raw"
        kernel_version_fix.patch)
sha512sums=('55523ce0d3c3790c33fbe73bd396e5e5f1d015608303e497202a232f51af9bb172003cc836880a7fa85163947609281754606067e5e0df79e9630cd6d1821b96'
            '7db159146ec980979625f63045042f179070b3b16df99cca42359c9494390d3d4f16d93ffc2a28f1e2d738be753900a5eccb2a845b8f79847b3503e71624d381'
            'e0832b2fed7ddf7631041767f3ef31f941f23338db45b879866ad5fce90932c89bcb9e37638e85ea0c1d96bc36cbd91479c2949b20cfb1bc4dfa707b67b31dc7'
            '8a91e6662b5749153090b7a4df898308087743c60d46ad00ab225a0393ad5d872c9ac17b8cacb00f9dd6f2163e0649ecdd7a38b780b8912b0fc9d670e477af14'
            '04268c5beddfc0cca73d0b06448617c9c871a0e6d06d1b2559e492e79e4cf2f5d81e05f1b98d3f7333f2c015ea226fd348672d9b277e6099570b6a907817dcbd'
            '4b6818bdc2d19389515b4ef9dc5ef9c18357807e3e9c46461111b32356ef00c33b8a5e2edead1ec4360a1e14097266567d008a0f1913948661bd6376605a520a'
            'df3f848e140c6ef711962f7e1a331ff72453263306a2b97e59e168356e79ad2f01f3c0229c303a9463a83580b774654f8fca51aad037d1baae970b2c4590fad9'
            '0b77fd4c03eb311c58db5a07a2d21d7437105a5f49420be364b911e401d7205f26daa4bc999a72632beec9717ca3d0276f660ec9a22229f9e9f7de20272e3166'
            '5fdf496ceb35036097ad042e09612c3a811a3000eeffd01a146f54fbece1278728b6e0a2fffe886e6f457084c760ae291dd96edd32e2a831d65fb612737983b5'
            '0e3f492b36e9a0d9e3b879718e6757d3d51fe9333469dd943bcd8964fc0e060e8da114fa7862d44a9a66018a436fb2dae3808174f9f43bec4aac0381e68f3b73'
            '6aab8c8c82bb6cc36606c871fc1a6607d4b9a332280abdc4877f0ee3a5e4e9a9480c8504302b431b2cdd38e0cb48603983f26a1ffd7a247382008deb67db26f3')


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
