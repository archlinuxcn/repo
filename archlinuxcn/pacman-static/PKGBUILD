# Maintainer: Eli Schwartz <eschwartz@archlinux.org>

# All my PKGBUILDs are managed at https://github.com/eli-schwartz/pkgbuilds

pkgname=pacman-static
pkgver=5.2.2
_cares_ver=1.16.1
_nghttp2_ver=1.41.0
_curlver=7.71.0
_sslver=1.1.1g
_zlibver=1.2.11
_xzver=5.2.5
_bzipver=1.0.8
_zstdver=1.4.5
_libarchive_ver=3.4.3
_gpgerrorver=1.38
_libassuanver=2.5.3
_gpgmever=1.13.1
pkgrel=1
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
source+=("https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-${_gpgerrorver}.tar.bz2"{,.sig})
validpgpkeys+=('D8692123C4065DEA5E0F3AB5249B39D24F25E3B6'  # Werner Koch
               '031EC2536E580D8EA286A9F22071B08A33BD3F06') # NIIBE Yutaka (GnuPG Release Key) <gniibe@fsij.org>
# libassuan
source+=("https://gnupg.org/ftp/gcrypt/libassuan/libassuan-${_libassuanver}.tar.bz2"{,.sig})
# gpgme
source+=("https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-${_gpgmever}.tar.bz2"{,.sig})
# libarchive
source+=("https://github.com/libarchive/libarchive/releases/download/v${_libarchive_ver}/libarchive-${_libarchive_ver}.tar.xz"{,.asc})
validpgpkeys+=('A5A45B12AD92D964B89EEE2DEC560C81CEC2276E') # Martin Matuska <mm@FreeBSD.org>

sha512sums=('1f9c569fb9cfe90afeeb7e3715bfa821ec4c57fdbbd7e09cd1e2519fad1a555b2f5378dedb2c2e551d2e92db92f1db9684969b472507f676c5bb932cdf436eda'
            'SKIP'
            'c92e8022ccc876fa311f21bc5bf5af75feff8232efb56a4b2ab198031e974d15b67c16c046188cc76552f75a1b2e7115925d6ce1e42d6f94ae482fe69727466d'
            '4ac2a5d5c6da74eb1d6155c4eadc7127ab1b53a8d13caec41bd6172db5417a79f3ab022e77ba37d8b13da6893d7ced5fd8baf5cc3950a4154b4de8743ad31471'
            'SKIP'
            'c983a2a71bf5037a0f2b7f55b7638fbc1f43b4bd56db5c407ae42482b0dc9b94ae90a108c48e0526a5fa580d992d9c1a96b35d35f82ba0d4c982f9bf5ab695f6'
            'SKIP'
            '01e3d0b1bceeed8fb066f542ef5480862001556e0f612e017442330bbd7e5faee228b2de3513d7fc347446b7f217e27de1003dc9d7214d5833b97593f3ec25ab'
            'SKIP'
            '3857c298663728a465b5f95a3ef44547efbfb420d755e9dde7f20aa3905171b400e1c126d8db5c2b916c733bbd0724d8753cad16c9baf7b12dcd225a3ee04a97'
            '73fd3fff4adeccd4894084c15ddac89890cd10ef105dd5e1835e1e9bbb6a49ff229713bd197d203edfa17c2727700fce65a2a235f07568212d820dca88b528ae'
            'SKIP'
            '7443674247deda2935220fbc4dfc7665e5bb5a260be8ad858c8bd7d7b9f0f868f04ea45e62eb17c0a5e6a2de7c7500ad2d201e2d668c48ca29bd9eea5a73a3ce'
            'SKIP'
            '083f5e675d73f3233c7930ebe20425a533feedeaaa9d8cc86831312a6581cefbe6ed0d08d2fa89be81082f2a5abdabca8b3c080bf97218a1bd59dc118a30b9f3'
            'SKIP'
            'b03c497c3e0590c3d384cb856e3024f144b2bfac0d805d80e68deafa612c68237f12a2d657416d476a28059e80936c79f099fc42331464b417593895ea214387'
            'b936a4738c2cee111d855b1ba3ec433da8c77799a87d1f71275f974f871ebfa593c9db06ea53f0490b6cd6b94bef34f6052a587a4d13d839ec0128500c2dd9de'
            'SKIP'
            'e7ccb651ea75b07b2e687d48d86d0ab83cba8e2af7f30da2aec794808e13e6ec93f21d607db50d3431f1c23cb3a07a2793b71170e69fa2f5a82cffb81961f617'
            'SKIP'
            '11de670c6cf512508103fe67af56d9fbb2a9dda6fc6fa3cd321371bbe337c7c2c81913ca557d07187adb2a63d37ea1a44da97ab22345bbe6022c405d0cb083b8'
            'SKIP'
            '9ad2b80de8edd94f9b2e590bfbcd07d36234382595784d918ed47fc532859cabd4bcf45cb3cf08ba7fc5202098191a42629c38f66a63a9efff194fac63a79c76'
            'SKIP')
b2sums=('14896b3911f851f66b93443fe29eca9ffe21a73698ce7844a7924450c0399ce71d038843d8a4acedb029d5444cd1b409776d482edff5e58928e248068acb68dd'
        'SKIP'
        '8dbd5f80bb9617d792e2eece09f6cae82907ad3a14a90084578b213191015c32ac38de87d9a39246651087b5d0e9c6c624ff806a0690973b5faa8624ee033d8f'
        '0d87538f5d6cac5b6b9c92d6ba5525af0e580e6506bee9270318f0951aaccdc7e135b446381e8150241d367789ccf2f73dbb333d45de4dbb5a87af05483063a8'
        'SKIP'
        'd2e2c5389fd5ff20b232711f07cf8d83f12e0acb8b865d209dadf34a28925e922bc37270cef6e48b9aa33e8cff7ea1832d57879de73966cee77531f815a8838d'
        'SKIP'
        '5e3dd4725ff89b959a5436d64b521317c6ffeb377418cc24c6d1927fab923423cb5f5fce2f9c2cdee597041c7be156d09668a5fd13dc6ff06d235a83db94cf19'
        'SKIP'
        'e2ff99e8236487f43171c771d0ee89137b73f3d0b2756bcb0d6525c810ffa9f5a3763c3744327fb47cef21eabfc50fff96632f4bbe2cd244206a99daffa0c25a'
        '6bfc4bca5dcadba8a0d4121a2b3ed0bfe440c261003521862c8e6381f1a6f0a72d3fc037351d30afd7ef321e8e8d2ec817c046ac749f2ca0c97fbdc2f7e840b7'
        'SKIP'
        'aded57324e129572c41646b3cc3b0b59a459452d9338d9245663b63dac2a463fb1f1b2b1d2d4ad3c09cb71fb8439df52cd94f24db99e782fc899b94a288a3043'
        'SKIP'
        '22ab3acd84f4db8c3d6f59340c252faedfd4447cea00dafbd652e65b6cf8a20adf6835c22e58563004cfafdb15348c924996230b4b23cae42da5e25eeac4bdad'
        'SKIP'
        '1497d4e87040e5c71466468ebf1a57f4073666f2b005229925bc1d95a4b4fcb2a51d88bb79be20f21860e5750da42f8aac21d2997421d07ba37bd6bb12a28b55'
        '9532402466748503805366b94c82c9adfe5b448f885c26b33ebf7ba9957161ca046b4057f5ca862224accb9f2af731652a55d20e7a4ab69107190a58c8e11ad6'
        'SKIP'
        'ae3a5a9a03e85d62cf87271cd4a0718a2b89a4f90ea814837913e4b2bb6e5af9746e766d99685cc0cc3a801efaee597e491a2bc03d42ac26059580ea4680fd7a'
        'SKIP'
        '17fff261ab76b72e096aa42cc847443bfd3bbf0eb6d04af1d38561ddce1d11cfe9a98b6ced268b28f33e2cb7d900a9e6b3dfc56f1c784a021dbefbf493522e70'
        'SKIP'
        '45eaa44468b55d81626a8c315f80a7504c43c27dc5055b719952bb7deaa19e934b579e8f529e268bbd629223b9c0296a2925278950ab9e8a296fb6b919d6f56f'
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

# keep using xz-compressed packages, because one use of the package is to
# recover on systems with broken zstd support in libarchive
[[ $PKGEXT = .pkg.tar.zst ]] && PKGEXT=.pkg.tar.xz

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
