# Maintainer: Eli Schwartz <eschwartz@archlinux.org>

# All my PKGBUILDs are managed at https://github.com/eli-schwartz/pkgbuilds

pkgname=pacman-static
pkgver=5.1.3
_cares_ver=1.15.0
_nghttp2_ver=1.36.0
_curlver=7.65.1
_sslver=1.1.1c
_zlibver=1.2.11
_xzver=5.2.4
_bzipver=1.0.6
_zstdver=1.4.0
_libarchive_ver=3.4.0
_gpgerrorver=1.36
_libassuanver=2.5.3
_gpgmever=1.13.1
pkgrel=5
pkgdesc="Statically-compiled pacman (to fix or install systems without libc)"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://www.archlinux.org/pacman/"
license=('GPL')
depends=('pacman')
makedepends=('musl' 'kernel-headers-musl')

# pacman
source=("https://sources.archlinux.org/other/pacman/pacman-${pkgver}.tar.gz"{,.sig})
validpgpkeys=('6645B0A8C7005E78DB1D7864F99FFE0FEAE999BD'  # Allan McRae <allan@archlinux.org>
              'B8151B117037781095514CA7BBDFFC92306B1121') # Andrew Gregory (pacman) <andrew@archlinux.org>
# nghttp2
source+=("https://github.com/nghttp2/nghttp2/releases/download/v$_nghttp2_ver/nghttp2-$_nghttp2_ver.tar.xz")
# c-ares
source+=("https://c-ares.haxx.se/download/c-ares-${_cares_ver}.tar.gz"{,.asc})
validpgpkeys+=('27EDEAF22F3ABCEB50DB9A125CC908FDB71E12C2') # Daniel Stenberg <daniel@haxx.se>
# curl
source+=("https://curl.haxx.se/download/curl-${_curlver}.tar.gz"{,.asc}
         "https://github.com/curl/curl/commit/094b5f3540fec1401f514bc470f11f441527d30a.patch"
         "https://github.com/curl/curl/commit/8b987cc7eb8bd58eaf7c184e0db7103a236704bd.patch"
         "https://github.com/curl/curl/commit/6cc18c59a77bccdd04f65a9abcc9a2b2f88d368d.patch"
         )
# openssl
source+=("https://www.openssl.org/source/openssl-${_sslver}.tar.gz"{,.asc}
         "ca-dir.patch")
validpgpkeys+=('8657ABB260F056B1E5190839D9C4D26D0E604491'  # Matt Caswell <matt@openssl.org>
               '7953AC1FBC3DC8B3B292393ED5E9E43F7DF9EE8C') # Richard Levitte <levitte@openssl.org>
# zlib
source+=("https://zlib.net/zlib-${_zlibver}.tar.gz"{,.asc})
validpgpkeys+=('5ED46A6721D365587791E2AA783FCD8E58BCAFBA') # Mark Adler <madler@alumni.caltech.edu>
# xz
source+=("https://tukaani.org/xz/xz-${_xzver}.tar.gz"{,.sig})
validpgpkeys+=('3690C240CE51B4670D30AD1C38EE757D69184620') # Lasse Collin <lasse.collin@tukaani.org>
# bzip2
source+=("https://sources.archlinux.org/other/packages/bzip2/bzip2-${_bzipver}.tar.gz")
# zstd
source+=("${pkgname}-${pkgver}.tar.gz::https://github.com/facebook/zstd/archive/v${_zstdver}.tar.gz")
# libgpg-error
source+=("https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-${_gpgerrorver}.tar.bz2"{,.sig})
validpgpkeys+=('D8692123C4065DEA5E0F3AB5249B39D24F25E3B6'  # Werner Koch
               '031EC2536E580D8EA286A9F22071B08A33BD3F06') # NIIBE Yutaka (GnuPG Release Key) <gniibe@fsij.org>
# libassuan
source+=("https://gnupg.org/ftp/gcrypt/libassuan/libassuan-${_libassuanver}.tar.bz2"{,.sig})
# gpgme
source+=("https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-${_gpgmever}.tar.bz2"{,.sig})
# libarchive
source+=("https://github.com/libarchive/libarchive/releases/download/v${_libarchive_ver}/libarchive-${_libarchive_ver}.tar.gz"{,.asc})
validpgpkeys+=('CB55788360B992FA0885C878F040F7196BA99AF4') # Martin Matuska <martin@matuska.org>

sha512sums=('b556b6d01d651a675ce1e153ede776e682ca0eb671cd2be00d7b7c602504dd119291f38ef5c318e675b4ce865db7e1c57e0ebc157510f0fc72e656feb8947e54'
            'SKIP'
            '4e0d5c5cdb4f1b7e5f12790850237f36649af4aa9596033392725972e4e0e5a33bb78bd1aa0735e35e489b523b7e9a236a7b5847dfca69bd7583fcab36c13c76'
            'a1de6c5e7e1a6a13c926aae690e83d5caa51e7313d63da1cf2af6bc757c41d585aad5466bc3ba7b7f7793cb1748fa589f40972b196728851c8b059cfc8c3be50'
            'SKIP'
            '0a4b81d115f579df8301859f7d06d00bd9820cbf2fb6b63c6a49418aa174ab32bcbc8942f032f2ea924d208f147de8a30f02f6b922f627d3d9d4afc60df8a39f'
            'SKIP'
            'c187c7a4352ef16881272d2ac4856b06b5f7b66da0a65df63736183c30942ad70795cff96a6f2a20084bbe58c36bfc0f56472d0e505fe1300ef5dc05527019de'
            '23584888c3c430f5b8586bf9cc5138b7f28e43e922781b03ea761a5dd550fefcc47d143e3309ffb0f3fea961670fab551911c9c4ec79610ef0d96249157fe829'
            '368ec44f907e9b358065f335468fd111e9898d892c87379fb97fef4fcd10dc581c0ffd420054b9996b431ed04695f3bb627a11ddbaae778277407b8d912437ce'
            '8e2c5cc11c120efbb7d7850980cb6eaa782d29b4996b3f3378d37613c1679f852d7cc08a90d62e78fcec3439f06bdbee70064579a8c2adaffd91532a97f646ff'
            'SKIP'
            '3857c298663728a465b5f95a3ef44547efbfb420d755e9dde7f20aa3905171b400e1c126d8db5c2b916c733bbd0724d8753cad16c9baf7b12dcd225a3ee04a97'
            '73fd3fff4adeccd4894084c15ddac89890cd10ef105dd5e1835e1e9bbb6a49ff229713bd197d203edfa17c2727700fce65a2a235f07568212d820dca88b528ae'
            'SKIP'
            'e5bf6eb88365d2dbdc774db49261fb9fae0544ed297891fc20f1ed223f4072cb0357cbd98146ac35b6d29410a12b6739bbd111cd57d4a225bef255ed46988578'
            'SKIP'
            '00ace5438cfa0c577e5f578d8a808613187eff5217c35164ffe044fbafdfec9e98f4192c02a7d67e01e5a5ccced630583ad1003c37697219b0f147343a3fdd12'
            '8614934e25eb1e82b554c483bc9d2d055f51344697295e83b22a8d726321b12068cfa7f7d2a9fe28a2de7c9edda59733826277efc7046e13674d6f7f02af5671'
            '6e5f853f77dc04f0091d94b224cab8e669042450f271b78d0ea0219658d059c9cab1ab0eaa020a4227f451520b417fc340b85971a6f5e144fa69be57e15df346'
            'SKIP'
            'e7ccb651ea75b07b2e687d48d86d0ab83cba8e2af7f30da2aec794808e13e6ec93f21d607db50d3431f1c23cb3a07a2793b71170e69fa2f5a82cffb81961f617'
            'SKIP'
            '11de670c6cf512508103fe67af56d9fbb2a9dda6fc6fa3cd321371bbe337c7c2c81913ca557d07187adb2a63d37ea1a44da97ab22345bbe6022c405d0cb083b8'
            'SKIP'
            '2f9e2a551a6bcab56fb1a030b5d656df7299a3d151465aa02f0420d344d2fada49dee4755b3abff9095f62519e14dc9af8afa1695ecc6d5fdb4f0b28e6ede852'
            'SKIP')
b2sums=('f933a37f201ef842b0e4bb041961db6def67c7e811299966b6e2054ae640180a5a10ba904aa4c4356e351a5cefb228d8853e79c5707ddf08dfa271b054d3b169'
        'SKIP'
        '7c116988c22801688c50d6d514ddb904920cc54d3c3d141137e6ed8b2182ef4e670f0a0fdebaeabfe0df8cdea4cfd1ee3fb083628f035201f104de6f3614dd25'
        'c4028bb2840af23274b79c73600bfcf73a348c7ab63ae3c215829e0fe2cf149f4ad38a3ec657c3997bad818ced3cacaed0579dd0dd2ef42eaffd074bdc4f22ed'
        'SKIP'
        '1c5378789ba5779355e3af3543c36cefb7019abf490e92ec97b2d768bcc7ba58bf7efe3614a7819794095fe8bc690a534f1183796d9074f9358470b046a27769'
        'SKIP'
        '6b61b8b9509028d1df40280f77508e7c7c1a01e0fb06ca98c4b4e630ac6be323538786300840e36aabd8aac916b8dc277bd3cf4dec89c314d79742ca7ae594b4'
        'e31c7678302f9e899b05a3b72826e0cb2dd4b56cae5820c466b41bbf06084fc93bb0b882a4860729e608a1039a7f58f2e35fbda22000aedbbb6f1a0970f3818a'
        '49f8ab4bc5cd850a85b3dbd493476967be31bff55300bc0b78f0523d8367d8cd84a348422b16607bcbef9396d6b1528de7f4d9485a367729e0dfcc230cbaee24'
        'bd157b244bedcefb8e646a743732945119b267236789ac69c38856570318aca09299bdaaea3f20294863b633e6fd4dfe124820597185b3b7461cfdf094daadb0'
        'SKIP'
        'e2ff99e8236487f43171c771d0ee89137b73f3d0b2756bcb0d6525c810ffa9f5a3763c3744327fb47cef21eabfc50fff96632f4bbe2cd244206a99daffa0c25a'
        '6bfc4bca5dcadba8a0d4121a2b3ed0bfe440c261003521862c8e6381f1a6f0a72d3fc037351d30afd7ef321e8e8d2ec817c046ac749f2ca0c97fbdc2f7e840b7'
        'SKIP'
        '877242324afd3c7eb21d3a9414c53843f4d1bb089206e8e545e280b32ff5372f7fb4a1b0c27cb6fdf0d0a27a668e9772ecc3fffc181df95d081ca9c2e987b83b'
        'SKIP'
        'b31533af7c71d715e6600874bb0a11b9b3aebbb08af0414a6d88bd5a2ad879a482ad408338159cb6c241815da8f48798d2ea7789ea971431d0be42ee827b0a7e'
        '1b92a055712bb47c3d56c51f3ddddeaba00f9b746f7e47a2fa1a0afdf9798ff90f0ec734880a5d03644d47deb0e55f75c2cd3cbdab1a146dba5f49d4efeb2ae0'
        '81684f6e47192c50cfa408977d53dc3812befca28733b531d51dffa0a6799a47366a50f64755557a7b3111a179ac4aba9e6a527418461cdbcccea80ae6bed4fa'
        'SKIP'
        'ae3a5a9a03e85d62cf87271cd4a0718a2b89a4f90ea814837913e4b2bb6e5af9746e766d99685cc0cc3a801efaee597e491a2bc03d42ac26059580ea4680fd7a'
        'SKIP'
        '17fff261ab76b72e096aa42cc847443bfd3bbf0eb6d04af1d38561ddce1d11cfe9a98b6ced268b28f33e2cb7d900a9e6b3dfc56f1c784a021dbefbf493522e70'
        'SKIP'
        '6da5798ceabb542d8b877b3d672f6e6431ed7340ec0160a5d8cef28591b516b55d426002379eddc632a478bfd2f034a358f8552f55c9f066fd7f5c31c218b462'
        'SKIP')

export LDFLAGS="$LDFLAGS -static"
export CC=musl-gcc
export CXX=musl-gcc

# https://www.openwall.com/lists/musl/2014/11/05/3
# fstack-protector and musl do not get along but only on i686
if [[ $CARCH = i686 ]]; then
    # silly build systems have configure checks or buildtime programs that don't CFLAGS but do do CC
    export CC="musl-gcc -fno-stack-protector"
    export CXX="musl-gcc -fno-stack-protector"
    export CFLAGS="${CFLAGS/-fstack-protector-strong/}"
    export CXXFLAGS="${CXXFLAGS/-fstack-protector-strong/}"
fi

prepare() {
    cd "${srcdir}"/curl-${_curlver}
    # backport fix for segfaults in DNS resolution
    patch -p1 -i ../094b5f3540fec1401f514bc470f11f441527d30a.patch
    # backport more upstream fixes for crashes in multi stack (FS#62892)
    patch -p1 -i ../8b987cc7eb8bd58eaf7c184e0db7103a236704bd.patch
    patch -p1 -i ../6cc18c59a77bccdd04f65a9abcc9a2b2f88d368d.patch

    cd "${srcdir}"/libarchive-${_libarchive_ver}
    autoreconf -fi
}

build() {
    export PKG_CONFIG_PATH="${srcdir}"/temp/usr/lib/pkgconfig
    export PATH="${srcdir}/temp/usr/bin:${PATH}"

    # openssl
    cd "${srcdir}"/openssl-${_sslver}
    case ${CARCH} in
        x86_64)
            openssltarget='linux-x86_64'
            optflags='enable-ec_nistp_64_gcc_128'
            ;;
        i686)
            openssltarget='linux-elf'
            optflags=''
            ;;
        arm|armv6h|armv7h)
            openssltarget='linux-armv4'
            optflags=''
            ;;
        aarch64)
            openssltarget='linux-aarch64'
            optflags='no-afalgeng'
            ;;
    esac
    # mark stack as non-executable: http://bugs.archlinux.org/task/12434
    ./Configure --prefix="${srcdir}"/temp/usr \
                --openssldir=/etc/ssl \
                --libdir=lib \
                -static \
                no-ssl3-method \
                ${optflags} \
                "${openssltarget}" \
                "-Wa,--noexecstack ${CPPFLAGS} ${CFLAGS} ${LDFLAGS}"
    make build_libs
    make install_dev

    # xz
    cd "${srcdir}"/xz-${_xzver}
    ./configure --prefix="${srcdir}"/temp/usr \
                --disable-shared
    cd src/liblzma
    make
    make install

    # bzip2
    cd "${srcdir}"/bzip2-${_bzipver}
    sed -i "s|-O2|${CFLAGS}|g" Makefile
    make libbz2.a
    install -Dvm644 bzlib.h "${srcdir}"/temp/usr/include/
    install -Dvm644 libbz2.a "${srcdir}"/temp/usr/lib/

    cd "${srcdir}"/zstd-${_zstdver}/lib
    make libzstd.a
    make PREFIX="${srcdir}"/temp/usr install-pc install-static install-includes

    # zlib
    cd "${srcdir}/"zlib-${_zlibver}
    ./configure --prefix="${srcdir}"/temp/usr \
                --static
    make libz.a
    make install

    # libarchive
    cd "${srcdir}"/libarchive-${_libarchive_ver}
    CPPFLAGS="-I${srcdir}/temp/usr/include" CFLAGS="-L${srcdir}/temp/usr/lib" \
        ./configure --prefix="${srcdir}"/temp/usr \
                    --without-xml2 \
                    --without-nettle \
                    --disable-{bsdtar,bsdcat,bsdcpio} \
                    --without-expat \
                    --disable-shared
    make
    make install-{includeHEADERS,libLTLIBRARIES,pkgconfigDATA,includeHEADERS}

    # nghttp2
    cd "${srcdir}"/nghttp2-${_nghttp2_ver}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-shared \
        --disable-examples \
        --disable-python-bindings
    make -C lib
    make -C lib install

    # c-ares
    # needed for curl, which does not use it in the repos
    # but seems to be needed for static builds
    cd "${srcdir}"/c-ares-${_cares_ver}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-shared
    make
    make install-{libcares_laHEADERS,libLTLIBRARIES,pkgconfigDATA}

    # curl
    cd "${srcdir}"/curl-${_curlver}
    # c-ares is not detected via pkg-config :(
    ./configure --prefix="${srcdir}"/temp/usr \
                --disable-shared \
                --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
                --disable-{dict,gopher,imap,imaps,ldap,ldaps,manual,pop3,pop3s,rtsp,scp,sftp,smb,smbs,smtp,smtps,telnet,tftp} \
                --without-{brotli,libidn2,librtmp,libssh2} \
                --disable-libcurl-option \
                --with-ssl \
                --enable-ares="${srcdir}"/temp/usr
    make -C lib
    make install-pkgconfigDATA
    make -C lib install
    make -C include install

    # libgpg-error
    cd "${srcdir}"/libgpg-error-${_gpgerrorver}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-shared
    make -C src
    make -C src install-{{,dist_}binSCRIPTS,libLTLIBRARIES,nodist_includeHEADERS,pkgconfigDATA}

    # libassuan
    cd "${srcdir}"/libassuan-${_libassuanver}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-shared
    make -C src
    make -C src install-{binSCRIPTS,libLTLIBRARIES,nodist_includeHEADERS,pkgconfigDATA}

    # gpgme
    cd "${srcdir}"/gpgme-${_gpgmever}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-fd-passing \
        --disable-shared \
        --disable-languages
    make -C src
    make -C src install-{binSCRIPTS,libLTLIBRARIES,nodist_includeHEADERS,pkgconfigDATA}

    # ew libtool
    rm "${srcdir}"/temp/usr/lib/lib*.la
    export PKG_CONFIG='pkg-config --static'

    # Finally, it's a pacman!
    cd "${srcdir}"/pacman-${pkgver}
    ./configure --prefix=/usr \
                --libdir=/usr/lib/pacman/lib \
                --sysconfdir=/etc \
                --localstatedir=/var \
                --program-suffix=-static \
                --with-scriptlet-shell=/usr/bin/bash \
                --with-ldconfig=/usr/bin/ldconfig \
                --disable-shared \
                --disable-doc
    make V=1 AM_LDFLAGS=-all-static
}

package() {
    cd "${srcdir}"/pacman-${pkgver}
    make -C lib/libalpm  DESTDIR="${pkgdir}" install-libLTLIBRARIES install-pkgconfigDATA
    make -C src/util  DESTDIR="${pkgdir}" install
    make -C src/pacman  DESTDIR="${pkgdir}" install-binPROGRAMS

    cp -a "${srcdir}"/temp/usr/{bin,include,lib} "${pkgdir}"/usr/lib/pacman/
    sed -i "s@${srcdir}/temp/usr@/usr/lib/pacman@g" \
        "${pkgdir}"/usr/lib/pacman/lib/pkgconfig/*.pc \
        "${pkgdir}"/usr/lib/pacman/bin/*
}
