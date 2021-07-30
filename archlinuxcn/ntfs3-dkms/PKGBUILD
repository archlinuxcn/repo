pkgname=ntfs3-dkms
pkgver=27.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')

source=(
    Makefile.patch
    dkms.conf
    kernel-5.12-backport.patch
    kernel-5.14-backport.patch
    "ntfs3-v${pkgver}~1.patch::https://lore.kernel.org/lkml/20210729134943.778917-2-almaz.alexandrovich@paragon-software.com/raw"
    "ntfs3-v${pkgver}~2.patch::https://lore.kernel.org/lkml/20210729134943.778917-3-almaz.alexandrovich@paragon-software.com/raw"
    "ntfs3-v${pkgver}~3.patch::https://lore.kernel.org/lkml/20210729134943.778917-4-almaz.alexandrovich@paragon-software.com/raw"
    "ntfs3-v${pkgver}~4.patch::https://lore.kernel.org/lkml/20210729134943.778917-5-almaz.alexandrovich@paragon-software.com/raw"
    "ntfs3-v${pkgver}~5.patch::https://lore.kernel.org/lkml/20210729134943.778917-6-almaz.alexandrovich@paragon-software.com/raw"
    "ntfs3-v${pkgver}~6.patch::https://lore.kernel.org/lkml/20210729134943.778917-7-almaz.alexandrovich@paragon-software.com/raw"
    "ntfs3-v${pkgver}~7.patch::https://lore.kernel.org/lkml/20210729134943.778917-8-almaz.alexandrovich@paragon-software.com/raw"
    "ntfs3-v${pkgver}~8.patch::https://lore.kernel.org/lkml/20210729134943.778917-9-almaz.alexandrovich@paragon-software.com/raw"
)

sha512sums=(
    '533c249f0f6bd4833faf02d0d92ca1b5802a49afc5feb2e46a7d37275cfca7896db76cd83593f4f313977d278a9a7e92eda550667be2b93910c49cfb68ead4fb'
    'ac00adb4a6d7fc685c39af054474631c930455e9ad0838338e6b3622b72451e81397506866b83a4a51dd0e34ed7752963c0fed9e8b017da5122e0dca3d345fb6'
    '374c6fa524defb5dcac093493bc7526e43ca9fe07602357fb51df4a26b02280ba4f2d764d3ba2ba2b32d5318ef466f3e0b6cbfdad1cdac0b04c31e8543114e33'
    '081b19b271ed89c47a9306874827a0c15feba6dda6d7c8a085f634a72a6691a78fdeccf47488ed141b979f7bfbf3df2d117301f09ba2da8416449460d4711d34'
    '5a018d5f5255a907dc40eeb8819163addd0a84e588c9ff81ca0abd5b5d01f8921966ef530ed71b3504e43a23ee0250a6eebb673c19b0350e125d4261cef147c1'
    '6485a1b72e40b44a65462762f0b803f021c08960ea7f5efa2b5ba4f6b60f887689ebf7ef8840f9fda1706aa413a76edf78319b31a99623daa1ea5b067859b8d2'
    'bac7d87d506fde67d637044d15841a8f8c7a90e361efefaa99c0375851f1192210e5e0122466fc44c421426d82445eaa35338386754d67ea9ba0ef6363f9f708'
    'd06114a86eca34252d5aafb667a3938418594ce096a8930d477849d36f590613bd658bc6bed70a2dac4f8b2a3b619762d1a07d6c516c7871f11d6499b8d5c409'
    '27b0cb8de12524b5f6c4725e02631474785dd72608ac9070f1f5d4521cfac4517281b9e7615e88ace923e55fcca90462797d2f0ee5da08317c43aae00cd54beb'
    '5791f97578c47f5332076bd9d6d4388df1a4392ac110a4649965806502db20a0184f9b1f1826ad2b129d99f2f46f15ee69312509393cda401774825b0285d5bd'
    'e35dfc2144e5449fb7ca76555eb0067595589bd0fe0a30a9a1dd8642be66912bf3a7545b9f6bf4b5a9397b894a1b63535372b5ec268179dd35b5890c8bb744be'
    '16605ef35c3534e61e8d06655e9c7237ee04e163e972f2c8b77ba9adfe775813a1788a5333bcd9cc41b6cd8e051f71c89f33f620047e302b24464c5d0ab1edf1'
)

prepare() {
    mkdir -p "${pkgver}"
    cd "${pkgver}"

    for patch in "${srcdir}/ntfs3-v${pkgver}"*.patch; do
        patch -p3 -N -i "${patch}"
    done

    patch -p0 -N -i "${srcdir}/Makefile.patch"

    # For testing
    # patch -p1 -N -i "${srcdir}/kernel-5.12-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.14-backport.patch"
}

package() {
    local dest="${pkgdir}/usr/src/ntfs3-${pkgver}"
    mkdir -p "${dest}"
    cd "${dest}"
    cp -r "${srcdir}/${pkgver}/"* ./
    cp "${srcdir}/dkms.conf" ./
    mkdir -p "./patches"
    cp "${srcdir}/kernel-"*.patch "./patches/"
}
