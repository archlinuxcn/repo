# Maintainer: Eli Schwartz <eschwartz@archlinux.org>

# All my PKGBUILDs are managed at https://github.com/eli-schwartz/pkgbuilds

pkgname=pacman-static
pkgver=5.1.3
_cares_ver=1.15.0
_nghttp2_ver=1.39.2
_curlver=7.66.0
_sslver=1.1.1d
_zlibver=1.2.11
_xzver=5.2.4
_bzipver=1.0.8
_zstdver=1.4.3
_libarchive_ver=3.4.0
_gpgerrorver=1.36
_libassuanver=2.5.3
_gpgmever=1.13.1
pkgrel=6
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
source+=("https://curl.haxx.se/download/curl-${_curlver}.tar.gz"{,.asc})
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
source+=("https://sourceware.org/pub/bzip2/bzip2-${_bzipver}.tar.gz"{,.sig})
validpgpkeys+=('EC3CFE88F6CA0788774F5C1D1AA44BE649DE760A') # Mark Wielaard <mark@klomp.org>
# zstd
source+=("zstd-${_zstdver}.tar.gz::https://github.com/facebook/zstd/archive/v${_zstdver}.tar.gz")
# libgpg-error
source+=("https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-${_gpgerrorver}.tar.bz2"{,.sig}
         "https://github.com/gpg/libgpg-error/commit/7865041c77f4f7005282f10f9b6666b19072fbdf.patch")
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
            'd8c971543e3e87736dfafebca55e9ecd0644e304c9731edaccba34170205824476595861a439077289b438ad489dd6008dedf2c6b2c111920300329be1b1bf34'
            'a1de6c5e7e1a6a13c926aae690e83d5caa51e7313d63da1cf2af6bc757c41d585aad5466bc3ba7b7f7793cb1748fa589f40972b196728851c8b059cfc8c3be50'
            'SKIP'
            '2a7d5e8b11eeb78c7a22bbaec0c10977d2c3e8cdabeb768e9d7cabd59e72e30a6d638b27f3815d6384954e96cc133c9670ce8a2a7c8aa03dde0ccf838aa93dae'
            'SKIP'
            '2bc9f528c27fe644308eb7603c992bac8740e9f0c3601a130af30c9ffebbf7e0f5c28b76a00bbb478bad40fbe89b4223a58d604001e1713da71ff4b7fe6a08a7'
            'SKIP'
            '3857c298663728a465b5f95a3ef44547efbfb420d755e9dde7f20aa3905171b400e1c126d8db5c2b916c733bbd0724d8753cad16c9baf7b12dcd225a3ee04a97'
            '73fd3fff4adeccd4894084c15ddac89890cd10ef105dd5e1835e1e9bbb6a49ff229713bd197d203edfa17c2727700fce65a2a235f07568212d820dca88b528ae'
            'SKIP'
            'e5bf6eb88365d2dbdc774db49261fb9fae0544ed297891fc20f1ed223f4072cb0357cbd98146ac35b6d29410a12b6739bbd111cd57d4a225bef255ed46988578'
            'SKIP'
            '083f5e675d73f3233c7930ebe20425a533feedeaaa9d8cc86831312a6581cefbe6ed0d08d2fa89be81082f2a5abdabca8b3c080bf97218a1bd59dc118a30b9f3'
            'SKIP'
            'ccda90c7437635f92d0db39dfba3604e256f1f08284c35c042763a54b0ead45dca8e7fa3e5cf8032292d1dd9eefc1369e23f78a80d9335d69170563090677d5f'
            '6e5f853f77dc04f0091d94b224cab8e669042450f271b78d0ea0219658d059c9cab1ab0eaa020a4227f451520b417fc340b85971a6f5e144fa69be57e15df346'
            'SKIP'
            '3c40b189c428c93d10685934cfaa2e35f71330da5ec271b7e5382b2b66090ccb4139efd743071cc0ea62a68bdc34d165d4a73bd0ef49fc357147f0b5166870b8'
            'e7ccb651ea75b07b2e687d48d86d0ab83cba8e2af7f30da2aec794808e13e6ec93f21d607db50d3431f1c23cb3a07a2793b71170e69fa2f5a82cffb81961f617'
            'SKIP'
            '11de670c6cf512508103fe67af56d9fbb2a9dda6fc6fa3cd321371bbe337c7c2c81913ca557d07187adb2a63d37ea1a44da97ab22345bbe6022c405d0cb083b8'
            'SKIP'
            '2f9e2a551a6bcab56fb1a030b5d656df7299a3d151465aa02f0420d344d2fada49dee4755b3abff9095f62519e14dc9af8afa1695ecc6d5fdb4f0b28e6ede852'
            'SKIP')
b2sums=('f933a37f201ef842b0e4bb041961db6def67c7e811299966b6e2054ae640180a5a10ba904aa4c4356e351a5cefb228d8853e79c5707ddf08dfa271b054d3b169'
        'SKIP'
        '4569774c33f17d51ac889c385697fcead82106db421399ceb22ad2aafabe64a576445d9272adcf37e2fec47cdd6ac1dc6423efd49012ca7be0aa2087609a0397'
        'c4028bb2840af23274b79c73600bfcf73a348c7ab63ae3c215829e0fe2cf149f4ad38a3ec657c3997bad818ced3cacaed0579dd0dd2ef42eaffd074bdc4f22ed'
        'SKIP'
        'be3c8060804ee159e38ac066bf6f66eb1ae7bc69b5a80ef6eb75ee0325f0a4098ad8e624e6a510cad7a8327701efc6b8b8088856b316087980fb82cc35e1c210'
        'SKIP'
        'd3155f07b487ebd8dd4fe25396c874f9af18b5cfd7e622298d29c4f2c8ce14ad4534609d321314a4bcd0d44414e1306190340daaacd3c8fca061c04498446244'
        'SKIP'
        'e2ff99e8236487f43171c771d0ee89137b73f3d0b2756bcb0d6525c810ffa9f5a3763c3744327fb47cef21eabfc50fff96632f4bbe2cd244206a99daffa0c25a'
        '6bfc4bca5dcadba8a0d4121a2b3ed0bfe440c261003521862c8e6381f1a6f0a72d3fc037351d30afd7ef321e8e8d2ec817c046ac749f2ca0c97fbdc2f7e840b7'
        'SKIP'
        '877242324afd3c7eb21d3a9414c53843f4d1bb089206e8e545e280b32ff5372f7fb4a1b0c27cb6fdf0d0a27a668e9772ecc3fffc181df95d081ca9c2e987b83b'
        'SKIP'
        '22ab3acd84f4db8c3d6f59340c252faedfd4447cea00dafbd652e65b6cf8a20adf6835c22e58563004cfafdb15348c924996230b4b23cae42da5e25eeac4bdad'
        'SKIP'
        'da4c4b4f6afc36a23a13a9582874891ad206b01dc805f9e79879cb833b47c0bb18ec1b3bb5c0b99f4e8707d21659ca0b7446a84d15f513a3fcab206bc7f49539'
        '81684f6e47192c50cfa408977d53dc3812befca28733b531d51dffa0a6799a47366a50f64755557a7b3111a179ac4aba9e6a527418461cdbcccea80ae6bed4fa'
        'SKIP'
        '06d379b0d2cdf2ddc315a741291419a4f3cb809454fedf70bbfccc7626b86824665c3361a9a2f7923e1c71e779bc2e2ed181174edaa2d1658a395da0c5bb2d72'
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
    cd "${srcdir}"/libarchive-${_libarchive_ver}
    autoreconf -fi

    cd "${srcdir}"/libgpg-error-${_gpgerrorver}
    # fix build with gawk 5
    patch -p1 -i ../7865041c77f4f7005282f10f9b6666b19072fbdf.patch
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
