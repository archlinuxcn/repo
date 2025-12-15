# Maintainer: Morgan <morganamilo@archlinux.org>
# Co-Maintainer: Andreas Baumann <mail@andreasbaumann.cc>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

pkgname=pacman-static
pkgver=7.1.0.r7.gb9f7d4a
_cares_ver=1.34.6
_nghttp2_ver=1.68.0
_curlver=8.17.0
_sslver=3.6.0
_zlibver=1.3.1
_xzver=5.8.1
_bzipver=1.0.8
_zstdver=1.5.7
_libarchive_ver=3.8.4
_gpgerrorver=1.57
_libassuanver=3.0.0
_gpgmever=2.0.1
_libseccompver=2.5.6
pkgrel=4
# use annotated tag and patch level commit from release branch (can be empty for no patches)
_git_tag=7.1.0
_git_patch_level_commit=b9f7d4a5b0bea75953f5892621a2caecc5672de5
pkgdesc="Statically-compiled pacman (to fix or install systems without libc)"
arch=('i486' 'i686' 'pentium4' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://www.archlinux.org/pacman/"
license=('GPL-2.0-or-later')
depends=('pacman')
makedepends=('meson' 'musl' 'kernel-headers-musl' 'git' 'gperf')
options=('!emptydirs' '!lto')

# pacman
source=("git+https://gitlab.archlinux.org/pacman/pacman.git#tag=v${_git_tag}?signed"
        pacman-revertme-makepkg-remove-libdepends-and-libprovides.patch::https://gitlab.archlinux.org/pacman/pacman/-/commit/354a300cd26bb1c7e6551473596be5ecced921de.patch
        pacman-reproducible-builds.patch::https://gitlab.archlinux.org/pacman/pacman/-/commit/f4bdb77470528019aaba4d8b8f947e918c6db17d.patch)

validpgpkeys=('6645B0A8C7005E78DB1D7864F99FFE0FEAE999BD'  # Allan McRae <allan@archlinux.org>
              'B8151B117037781095514CA7BBDFFC92306B1121') # Andrew Gregory (pacman) <andrew@archlinux.org>
# nghttp2
source+=("https://github.com/nghttp2/nghttp2/releases/download/v$_nghttp2_ver/nghttp2-$_nghttp2_ver.tar.xz")
# c-ares
source+=("https://github.com/c-ares/c-ares/releases/download/v${_cares_ver}/c-ares-${_cares_ver}.tar.gz"{,.asc})
validpgpkeys+=('27EDEAF22F3ABCEB50DB9A125CC908FDB71E12C2'  # Daniel Stenberg <daniel@haxx.se>
               'DA7D64E4C82C6294CB73A20E22E3D13B5411B7CA') # Brad House <brad@brad-house.com>
# curl
source+=("https://curl.haxx.se/download/curl-${_curlver}.tar.gz"{,.asc})
validpgpkeys+=('27EDEAF22F3ABCEB50DB9A125CC908FDB71E12C2') # Daniel Stenberg
# openssl
source+=("https://github.com/openssl/openssl/releases/download/openssl-${_sslver}/openssl-${_sslver}.tar.gz"{,.asc}
         "ca-dir.patch"
         "openssl-3.0.7-no-atomic.patch")
validpgpkeys+=('8657ABB260F056B1E5190839D9C4D26D0E604491'
              '7953AC1FBC3DC8B3B292393ED5E9E43F7DF9EE8C'
              'A21FAB74B0088AA361152586B8EF1A6BA9DA2D5C'
              'EFC0A467D613CB83C7ED6D30D894E2CE8B3D79F5'
              'BA5473A2B0587B07FB27CF2D216094DFD0CB81EF')

validpgpkeys+=('8657ABB260F056B1E5190839D9C4D26D0E604491'  # Matt Caswell <matt@openssl.org>
              '7953AC1FBC3DC8B3B292393ED5E9E43F7DF9EE8C'   # Matt Caswell <matt@openssl.org>
              'A21FAB74B0088AA361152586B8EF1A6BA9DA2D5C'   # Tom?? Mr?z <tm@t8m.info>
              'EFC0A467D613CB83C7ED6D30D894E2CE8B3D79F5')  # OpenSSL security team key
# zlib
source+=("https://zlib.net/zlib-${_zlibver}.tar.gz"{,.asc})
validpgpkeys+=('5ED46A6721D365587791E2AA783FCD8E58BCAFBA') # Mark Adler <madler@alumni.caltech.edu>
# xz
source+=("git+https://github.com/tukaani-project/xz#tag=v${_xzver}")
validpgpkeys+=('3690C240CE51B4670D30AD1C38EE757D69184620')  # Lasse Collin <lasse.collin@tukaani.org>
# bzip2
source+=("https://sourceware.org/pub/bzip2/bzip2-${_bzipver}.tar.gz"{,.sig})
validpgpkeys+=('EC3CFE88F6CA0788774F5C1D1AA44BE649DE760A') # Mark Wielaard <mark@klomp.org>
# zstd
source+=("https://github.com/facebook/zstd/releases/download/v${_zstdver}/zstd-${_zstdver}.tar.zst"{,.sig})
validpgpkeys+=('4EF4AC63455FC9F4545D9B7DEF8FE99528B52FFD') # Zstandard Release Signing Key <signing@zstd.net>
# libgpg-error
source+=("https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-${_gpgerrorver}.tar.bz2"{,.sig})
validpgpkeys+=('D8692123C4065DEA5E0F3AB5249B39D24F25E3B6'  # Werner Koch
               '031EC2536E580D8EA286A9F22071B08A33BD3F06'  # NIIBE Yutaka (GnuPG Release Key) <gniibe@fsij.org>
               '6DAA6E64A76D2840571B4902528897B826403ADA') # "Werner Koch (dist signing 2020)"
# libassuan
source+=("https://gnupg.org/ftp/gcrypt/libassuan/libassuan-${_libassuanver}.tar.bz2"{,.sig})
# gpgme
source+=("https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-${_gpgmever}.tar.bz2"{,.sig})
validpgpkeys+=('AC8E115BF73E2D8D47FA9908E98E9B2D19C6C8BD') #  Niibe Yutaka (GnuPG Release Key)
# libarchive
source+=("https://github.com/libarchive/libarchive/releases/download/v${_libarchive_ver}/libarchive-${_libarchive_ver}.tar.xz"{,.asc})
validpgpkeys+=('DB2C7CF1B4C265FAEF56E3FC5848A18B8F14184B'  # Martin Matuska <martin@matuska.org>
              '659C84C0E23EA1FA97E0B58CC040B508D63D2B36') # Martin Matuska <mm@FreeBSD.org>
# libseccomp
source+=(git+https://github.com/seccomp/libseccomp.git#tag=v${_libseccompver}?signed)
validpgpkeys+=('7100AADFAE6E6E940D2E0AD655E45A5AE8CA7C8A' # Paul Moore <paul@paul-moore.com>
              '47A68FCE37C7D7024FD65E11356CE62C2B524099') # Tom Hromatka <tom.hromatka@oracle.com>

sha512sums=('512c5096c82e00730c884e5d4d452928a66d35b42a831a2b4b8b17af9215140d6b21b2d2de7233eefae70edb8ddd8fc4d4c750bda1ba0235489bc427396c04ba'
            '1a108c4384b6104e627652488659de0b1ac3330640fc3250f0a283af7c5884daab187c1efc024b2545262da1911d2b0b7b0d5e4e5b68bb98db25a760c9f1fb1a'
            '7ca20c2ab350f72552544004b37c5c920ae32b852e7f5315b8b29ee8acb86ca8e1f9f9678792842723908e3cb894f63904af8488cb4d49066a3dba5fc14518aa'
            'a5182c2c54cdff3c70bdad204bff9a573cf7951e189d68665087f047cb79e5fc2d5d5aefbb41e2dfe264e2e74fbbe10196cb596248e328c944406ca09da98344'
            '826eecdb40942caf75da982b9ca57fbe7c3e7c23af43a908683c7c1523c46b06ebac68405c26db8bf4c8b0774ca415666866249a3bde663a71c278f4ec7b1827'
            'SKIP'
            '88ab4b7aac12b26a6ad32fb0e1a9675288a45894438cb031102ef5d4ab6b33c2bc99cae0c70b71bdfa12eb49762827e2490555114c5eb4a6876b95e1f2a4eb74'
            'SKIP'
            '866825a1cdf0b705b409402fbc7a713e7d9b8e7736c5126be57b354927954c148a341fc52b02c0629c1e015a889bfd40217f8e703b73235892e91da060909b76'
            'SKIP'
            'b1873dbb7a49460b007255689102062756972de5cc2d38b12cc9f389b6be412da6797579b1acd3717a8cd2ee118fd9801b94e55f063d4328f050f0876a5eb53c'
            'b5887ea77417fae49b6cb1e9fa782d3021f268d5219701d87a092235964f73fa72a31428b630445517f56f2bb69dcbbb24119ef9dbf8b4e40a753369a9f9a16f'
            '580677aad97093829090d4b605ac81c50327e74a6c2de0b85dd2e8525553f3ddde17556ea46f8f007f89e435493c9a20bc997d1ef1c1c2c23274528e3c46b94f'
            'SKIP'
            'b9a0f746215cd93c04fecd390ca44fc281d892b989e740ec6abbaa6a1eb457bbef40a33596dfe6e2285a319f2b09ae1994d778f0cf61114cbee9454a0eaa754b'
            '083f5e675d73f3233c7930ebe20425a533feedeaaa9d8cc86831312a6581cefbe6ed0d08d2fa89be81082f2a5abdabca8b3c080bf97218a1bd59dc118a30b9f3'
            'SKIP'
            '2af02be3df319556b65403450acc55964d971fe263fed87dea823fb264a862db807a2a3d89358564277a83e5b303302cc677f66b5e523e3d224120b884e5ef1b'
            'SKIP'
            'd45d2ba1539d99f2886fd568cc29642b12a028d26d13b494e5f6df5b3ed5cdec04a861b29e310ba3fa2ef6d1bbeca3e0ae922a230d4769756492ab912bd6902c'
            'SKIP'
            '7c5c95c1b85bef2d4890c068a5a8ea8a1fe0d8def6ab09e5f34fc2746d8808bbb0fc168e3bd66d52ee5ed799dcf9f258f4125cda98c8384f6411bcad8d8b3139'
            'SKIP'
            'ad19169594b6048b11df9311080e179232ff03def08f377e7d7536a3a91e12f722cbae93e80364b73db013152b327bc3457ec9a9ddea9c660d74f389f6ab8837'
            'SKIP'
            '088f3726de7f8e2f4b2ac6cc9c01338328493de19f5b0645157114ef3b7a0fa5213cb6d64123736cae83354a2137bba9e2187bb4208cb7848e2566c65b100489'
            'SKIP'
            'SKIP')

export LDFLAGS="$LDFLAGS -static"
export CC=musl-gcc
export CXX=musl-gcc

# https://www.openwall.com/lists/musl/2014/11/05/3
# fstack-protector and musl do not get along but only on i686
if [[ $CARCH = i686 || $CARCH = pentium4 || $CARCH = i486 ]]; then
    # silly build systems have configure checks or buildtime programs that don't CFLAGS but do do CC
    export CC="musl-gcc -fno-stack-protector"
    export CXX="musl-gcc -fno-stack-protector"
    export CFLAGS="${CFLAGS/-fstack-protector-strong/}"
    export CXXFLAGS="${CXXFLAGS/-fstack-protector-strong/}"
fi

# to enable func64 interface in musl for 64-bit file system functions
export CFLAGS+=' -D_LARGEFILE64_SOURCE'
export CXXFLAGS+=' -D_LARGEFILE64_SOURCE'

# keep using xz-compressed packages, because one use of the package is to
# recover on systems with broken zstd support in libarchive
[[ $PKGEXT = .pkg.tar.zst ]] && PKGEXT=.pkg.tar.xz

prepare() {
    cd "${srcdir}/pacman"

    # apply patch level commits on top of annotated tag for pacman
    if [[ -n ${_git_patch_level_commit} ]]; then
        if [[ v${_git_tag} != $(git describe --tags --abbrev=0 "${_git_patch_level_commit}") ]] then
            error "patch level commit ${_git_patch_level_commit} is not a descendant of v${_git_tag}"
            exit 1
        fi
        git rebase "${_git_patch_level_commit}"
    fi

    # handle local pacman patches
    local -a patches
    patches=($(printf '%s\n' "${source[@]}" | grep 'pacman-.*.patch'))
    patches=("${patches[@]%%::*}")
    patches=("${patches[@]##*/}")

    if (( ${#patches[@]} != 0 )); then
        for patch in "${patches[@]}"; do
            if [[ $patch =~ revertme-* ]]; then
                msg2 "Reverting patch $patch..."
                patch -RNp1 < "../$patch"
            else
                msg2 "Applying patch $patch..."
                patch -Np1 < "../$patch"
            fi
        done
    fi

    # openssl
    cd "${srcdir}"/openssl-${_sslver}
    patch -Np1 -i "${srcdir}/ca-dir.patch"
    case ${CARCH} in
        arm|armv6h|armv7h)
            # special patch to omit -latomic when installing pkgconfig files
            msg2 "Applying openssl patch openssl-3.0.7-no-atomic.patch..."
            patch -Np1 -i "${srcdir}/openssl-3.0.7-no-atomic.patch"
    esac
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
        pentium4)
            openssltarget='linux-elf'
            optflags=''
            ;;
        i686)
            openssltarget='linux-elf'
            optflags='no-sse2'
            ;;
        i486)
            openssltarget='linux-elf'
            optflags='386 no-threads'
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
    cd "${srcdir}"/xz
    ./autogen.sh --no-po4a --no-doxygen
    ./configure --prefix="${srcdir}"/temp/usr \
                --disable-shared
    cd src/liblzma
    make
    make install

    # bzip2
    cd "${srcdir}"/bzip2-${_bzipver}
    sed -i "s|-O2|${CFLAGS}|g;s|CC=gcc|CC=${CC}|g" Makefile
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
                    --disable-{bsdtar,bsdcat,bsdcpio,bsdunzip} \
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
        --disable-shared --disable-tests
    make -C src/lib
    make install-pkgconfigDATA
    make -C src/lib install
    make -C include install

    # curl
    cd "${srcdir}"/curl-${_curlver}
    # c-ares is not detected via pkg-config :(
    ./configure --prefix="${srcdir}"/temp/usr \
                --disable-shared \
                --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
                --disable-{dict,gopher,imap,ldap,ldaps,manual,pop3,rtsp,smb,smtp,telnet,tftp} \
                --without-{brotli,libidn2,librtmp,libssh2,libpsl} \
                --disable-libcurl-option \
                --with-openssl \
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
    make -C src install-{binSCRIPTS,libLTLIBRARIES,nodist_includeHEADERS,pkgconfigDATA}

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

    # libseccomp for sanboxing
	cd "${srcdir}/libseccomp"
	autoreconf -fiv
	./configure --prefix="${srcdir}"/temp/usr \
		--disable-shared --enable-static \
		--disable-python
	make
	make install

    # ew libtool
    rm "${srcdir}"/temp/usr/lib/lib*.la

    # Finally, it's a pacman!
    mkdir -p "${srcdir}"/pacman
    cd "${srcdir}"/pacman
    meson --prefix=/usr \
        --includedir=lib/pacman/include \
        --libdir=lib/pacman/lib \
        --buildtype=plain \
        -Dbuildstatic=true \
        -Ddefault_library=static \
        -Ddoc=disabled \
        -Ddoxygen=disabled \
        -Dldconfig=/usr/bin/ldconfig \
        -Dscriptlet-shell=/usr/bin/bash \
        build
    meson compile -C build
}

package() {
    cd "${srcdir}"/pacman
    DESTDIR="${pkgdir}" meson install -C build

    rm -rf "${pkgdir}"/usr/share "${pkgdir}"/etc
    for exe in "${pkgdir}"/usr/bin/*; do
        if [[ -f ${exe} && $(head -c4 "${exe}") = $'\x7fELF' ]]; then
            mv "${exe}" "${exe}"-static
        else
            rm "${exe}"
        fi
    done

    cp -a "${srcdir}"/temp/usr/{bin,include,lib} "${pkgdir}"/usr/lib/pacman/
    sed -i "s@${srcdir}/temp/usr@/usr/lib/pacman@g" \
        "${pkgdir}"/usr/lib/pacman/lib/pkgconfig/*.pc \
        "${pkgdir}"/usr/lib/pacman/bin/*
}
