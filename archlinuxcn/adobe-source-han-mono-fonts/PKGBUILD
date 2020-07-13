_pkgbase=adobe-source-han-mono
pkgbase=$_pkgbase-fonts
pkgname=($_pkgbase-jp-fonts $_pkgbase-kr-fonts $_pkgbase-cn-fonts $_pkgbase-tw-fonts $_pkgbase-hk-fonts $_pkgbase-otc-fonts)
pkgver=1.002
pkgrel=6
pkgdesc='Adobe Source Han Mono - A set of Pan-CJK fonts designed to complement Source Code Pro'
arch=('any')
license=('custom:OFL')
url='https://github.com/adobe-fonts/source-han-mono'
_commit=9a10a4fe9797b9777dd9b77cd093e8f76dd55e1d #tag=1.002
source=(44-source-han-mono-otc.conf
$url/releases/download/1.002/SourceHanMono.ttc
44-source-han-mono-jp.conf
$url/raw/$_commit/Bold/OTC/SourceHanMono-Bold.otf
$url/raw/$_commit/ExtraLight/OTC/SourceHanMono-ExtraLight.otf
$url/raw/$_commit/Heavy/OTC/SourceHanMono-Heavy.otf
$url/raw/$_commit/Light/OTC/SourceHanMono-Light.otf
$url/raw/$_commit/Medium/OTC/SourceHanMono-Medium.otf
$url/raw/$_commit/Normal/OTC/SourceHanMono-Normal.otf
$url/raw/$_commit/Regular/OTC/SourceHanMono-Regular.otf
44-source-han-mono-kr.conf
$url/raw/$_commit/Bold/OTC/SourceHanMonoK-Bold.otf
$url/raw/$_commit/ExtraLight/OTC/SourceHanMonoK-ExtraLight.otf
$url/raw/$_commit/Heavy/OTC/SourceHanMonoK-Heavy.otf
$url/raw/$_commit/Light/OTC/SourceHanMonoK-Light.otf
$url/raw/$_commit/Medium/OTC/SourceHanMonoK-Medium.otf
$url/raw/$_commit/Normal/OTC/SourceHanMonoK-Normal.otf
$url/raw/$_commit/Regular/OTC/SourceHanMonoK-Regular.otf
44-source-han-mono-cn.conf
$url/raw/$_commit/Bold/OTC/SourceHanMonoSC-Bold.otf
$url/raw/$_commit/ExtraLight/OTC/SourceHanMonoSC-ExtraLight.otf
$url/raw/$_commit/Heavy/OTC/SourceHanMonoSC-Heavy.otf
$url/raw/$_commit/Light/OTC/SourceHanMonoSC-Light.otf
$url/raw/$_commit/Medium/OTC/SourceHanMonoSC-Medium.otf
$url/raw/$_commit/Normal/OTC/SourceHanMonoSC-Normal.otf
$url/raw/$_commit/Regular/OTC/SourceHanMonoSC-Regular.otf
44-source-han-mono-tw.conf
$url/raw/$_commit/Bold/OTC/SourceHanMonoTC-Bold.otf
$url/raw/$_commit/ExtraLight/OTC/SourceHanMonoTC-ExtraLight.otf
$url/raw/$_commit/Heavy/OTC/SourceHanMonoTC-Heavy.otf
$url/raw/$_commit/Light/OTC/SourceHanMonoTC-Light.otf
$url/raw/$_commit/Medium/OTC/SourceHanMonoTC-Medium.otf
$url/raw/$_commit/Normal/OTC/SourceHanMonoTC-Normal.otf
$url/raw/$_commit/Regular/OTC/SourceHanMonoTC-Regular.otf
44-source-han-mono-hk.conf
$url/raw/$_commit/Bold/OTC/SourceHanMonoHC-Bold.otf
$url/raw/$_commit/ExtraLight/OTC/SourceHanMonoHC-ExtraLight.otf
$url/raw/$_commit/Heavy/OTC/SourceHanMonoHC-Heavy.otf
$url/raw/$_commit/Light/OTC/SourceHanMonoHC-Light.otf
$url/raw/$_commit/Medium/OTC/SourceHanMonoHC-Medium.otf
$url/raw/$_commit/Normal/OTC/SourceHanMonoHC-Normal.otf
$url/raw/$_commit/Regular/OTC/SourceHanMonoHC-Regular.otf
$url/raw/$_commit/LICENSE.md)

_jp=(
SourceHanMono-Bold.otf
SourceHanMono-ExtraLight.otf
SourceHanMono-Heavy.otf
SourceHanMono-Light.otf
SourceHanMono-Medium.otf
SourceHanMono-Normal.otf
SourceHanMono-Regular.otf
)
_kr=(
SourceHanMonoK-Bold.otf
SourceHanMonoK-ExtraLight.otf
SourceHanMonoK-Heavy.otf
SourceHanMonoK-Light.otf
SourceHanMonoK-Medium.otf
SourceHanMonoK-Normal.otf
SourceHanMonoK-Regular.otf
)
_cn=(
SourceHanMonoSC-Bold.otf
SourceHanMonoSC-ExtraLight.otf
SourceHanMonoSC-Heavy.otf
SourceHanMonoSC-Light.otf
SourceHanMonoSC-Medium.otf
SourceHanMonoSC-Normal.otf
SourceHanMonoSC-Regular.otf
)
_tw=(
SourceHanMonoTC-Bold.otf
SourceHanMonoTC-ExtraLight.otf
SourceHanMonoTC-Heavy.otf
SourceHanMonoTC-Light.otf
SourceHanMonoTC-Medium.otf
SourceHanMonoTC-Normal.otf
SourceHanMonoTC-Regular.otf
)
_hk=(
SourceHanMonoHC-Bold.otf
SourceHanMonoHC-ExtraLight.otf
SourceHanMonoHC-Heavy.otf
SourceHanMonoHC-Light.otf
SourceHanMonoHC-Medium.otf
SourceHanMonoHC-Normal.otf
SourceHanMonoHC-Regular.otf
)
_otc=(
SourceHanMono.ttc
)

_pkgdesc=("Adobe Source Han Mono - Pan-CJK OpenType/CFF Collection fonts"
          "Adobe Source Han Mono - Japanese OpenType/CFF fonts"
          "Adobe Source Han Mono - Korean OpenType/CFF fonts"
          "Adobe Source Han Mono - Simplified Chinese OpenType/CFF fonts"
          "Adobe Source Han Mono - Traditional Chinese (Taiwan) OpenType/CFF fonts"
          "Adobe Source Han Mono - Traditional Chinese (Hong Kong) OpenType/CFF fonts")

function _package {
    case "$1" in
        $_pkgbase-jp-fonts)
            fonts=(${_jp[@]})
            _fontconfig_filename=44-source-han-mono-jp.conf
            pkgdesc="Adobe Source Han Mono OTF - Japanese OpenType/CFF fonts";;
        $_pkgbase-kr-fonts)
            fonts=(${_kr[@]})
            _fontconfig_filename=44-source-han-mono-kr.conf
            pkgdesc="Adobe Source Han Mono OTF - Korean OpenType/CFF fonts";;
        $_pkgbase-cn-fonts)
            fonts=(${_cn[@]})
            _fontconfig_filename=44-source-han-mono-cn.conf
            pkgdesc="Adobe Source Han Mono OTF - Simplified Chinese OpenType/CFF fonts";;
        $_pkgbase-tw-fonts)
            fonts=(${_tw[@]})
            _fontconfig_filename=44-source-han-mono-tw.conf
            pkgdesc="Adobe Source Han Mono OTF - Traditional Chinese (Taiwan) OpenType/CFF fonts";;
        $_pkgbase-hk-fonts)
            fonts=(${_hk[@]})
            _fontconfig_filename=44-source-han-mono-hk.conf
            pkgdesc="Adobe Source Han Mono OTF - Traditional Chinese (Hong Kong) OpenType/CFF fonts";;
        $_pkgbase-otc-fonts)
            fonts=(${_otc[@]})
            _fontconfig_filename=44-source-han-mono-otc.conf
            pkgdesc="Adobe Source Han Mono - Pan-CJK OpenType/CFF Collection fonts";;
    esac

    # Prepare destination directory
    install -dm755 "$pkgdir/usr/share/fonts/adobe-source-han-sans"

    # Install fonts
    for font in "${fonts[@]}"; do
        install -m644 "$srcdir/$font" "$pkgdir/usr/share/fonts/adobe-source-han-sans"
    done

    # Install fontconfig files
    install -d "$pkgdir/etc/fonts/conf.d"
    install -Dm644 "$srcdir/$_fontconfig_filename" "$pkgdir/etc/fonts/conf.avail/$_fontconfig_filename"
    ln -s ../conf.avail/$_fontconfig_filename "$pkgdir/etc/fonts/conf.d/$_fontconfig_filename"
    
    # Install license file
    install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 LICENSE.md
}

for _pkgname in ${pkgname[@]}; do
    eval "function package_$_pkgname() { _package $_pkgname; }"
done

sha256sums=('34eb9b5060f6eaece4995aa51e6a6be9fcf2a8cd1e2a5388f1d8d2283585abfa'
            '0c192448de90848f11eb8336876883a9a36dc65b8965e489600cfcc7a67358c1'
            'a262b1646e81e04b448d07610b83ed9ecb0aefef604b8a3ee0c155c5603be7b6'
            '7e4b4d99cd67c3bf0c6c8df7a27bec5cb4906932dc50612305e79aebea57fe56'
            'fbb7eb709388e5351896758115d9dcbc16b8eb9f2a4210fbc05778a9cf259e7e'
            '6898c9b0de0005fe43f6abd36bf5985948e9fa219acb9d1608c7edfd66c5271a'
            'fc211c3008f58a19279dbe05cfed4b36b0d311922c0ff8b976bc50450db818a7'
            'b5102b68ccc2eae6d87454a1110258aa3b6ed2eb0fb388c306c99549bc3718a2'
            'd1c6f9b0b03da9aee984819d7e3b010b23856d5b1510a87982191848066e5c21'
            'b7300a290332e1b89421f251157b2be9ab384f5ca96eb58307b6f98c2c3a631b'
            '79f67392a1120b50646569f903f4fa15e3a515b0896e16d94ecc1350c07a9df3'
            '3cf20a4653892cab36dd1e011082e1190861bead470d867c7ade7af62ea48ee4'
            '28ee224407febea818455149fde7c38d9a5f1eaab596d3fe117a719471b68844'
            '34fbe1d90fdb41eb8732be43936d5d4c5241c7a3df1bc40ca6b66976dc33c129'
            'dabcb41f296130a8fb7c1283ece022ec411fc9939725fc11accf93e6896f74b6'
            'd4edcbc0ce80c3eb1a399e82644977035eb576180f038aa8781bbe2aba77556c'
            'b1270fc99fceefb0bbfe9a25497f3a7c1911cbdd1b90d00dacb953e866e0c889'
            '2931bfb8dc3fe0c09ea99de226dc9954c9b7d883876a45547edcb0852c51949e'
            '1fc1638366c3625b1079610fdcc146e4c91ec25777c30bed2edea1e5729f562e'
            '7bead3459a3afe4bcf4ce353cf639c13d54d3381bdb6ecaf58572ef4dac05091'
            '2b8c234ad2c3e1ecc8c4298d33f2927d824eab11686b5811402386e03a2dfa04'
            '9e4864ff8705d1a22d1b84754d41db3093e2189428912b530d05572214be4835'
            '05a961ea5bbd3fc45c43d128916fc820b4bcc5016de1ed55c9e9866321d45cbe'
            'c041398e1ba376442f27e8ea01a92ac5bc4e8cb762e9cccd2da1cc502c4df21b'
            '131ef446a8ba42b63bbfd159fc542bc24881f04634129793bfa170654f952703'
            'cecd1a14b948b8468389af021e1304d00a660d9e9c6b971aa322908d00edfe7a'
            'fee16e49f687e8a3e4d691471d87e298e96250faf897981641cc2efcd794d78b'
            '3492f0d29a3f7a4e9ed8d4e0dadf360c2829a470caec08d3eec48694cbe6e2c1'
            '0bda36d1d2effe5b6e1e4c6e4461a82567e851b1e74a0cbd5b7103e8331f58c9'
            '80f9b50f21ee1dd7f16c2997c862fd4af8d5c366000727bc44089211611a24ed'
            'ad3386db980e458ba9418f7ed93f1a5c3f08b4bee219016b84dc754c085edf9d'
            '83e2be5fba3b029cc1894e7b9fa48162839f582f296e87c81cecdd58fe37d717'
            'a376ef80b9be9d54d94e997ec141a8f6fc8db925523e11616ea91c1839cb3b72'
            '89c98a5001395e69ca8bd9b92f3588682b2d91a320a7ab314b29c5fcf2fd2c73'
            '2c01deb0b0de0e3ca831d40525dd2ed8b683209d812bac8cafe6bce579cacee2'
            '0886ed83b6720d2bc82e9e9c7c0c37adebf53455762960fb3a513bf2e1833583'
            '417e34dac262b0db041a5e86308cb76a852631ef9692d02f716cde4441c49a9f'
            'e23282adb2f0937eb5ddcbd5820532c8cb89ae740c96f61bdc5c89526e6e8764'
            '209f75513446c0edd253b4e1c22205c46ce1a1a0c46eaf32ffeb5a18d0e1ffc2'
            '2eec8c27fc357a120c9aff40a7d4a08af9a07586ae42007b2f261fe8d285b5c9'
            'e82cad8e32048ec757cdef92f0f150d12ffd2fb310b3fb7b0b7b9d0b88897f77'
            '920351def2dfff03955a5b2f9044800049920cf19a7696d59ba263fe11780e9d'
            '0983abed9371adc8958c321bf8d8036324b4a2e8cc324682b0fe0c699e63a009')
