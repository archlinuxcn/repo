# Maintainer: Nocifer <apmichalopoulos at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>

#NOTE: The UT dictionary's project page: http://linuxplayers.g1.xrea.com/mozc-ut.html

ENABLED_DICTIONARIES=(
'alt-cannadic'
'edict2'
'jawiki'
'neologd'
'personal-names'
'place-names'
'skk-jisyo'
'sudachidict'
)

pkgname='mozc-ut'
pkgver=2.31.5712.102.20250117
pkgrel=1
pkgdesc='The Open Source edition of Google Japanese Input bundled with the UT dictionary'
arch=('x86_64')
url='https://github.com/google/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-2.0-only AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('qt6-base')
makedepends=('bazel' 'git' 'python' 'qt6-base')
optdepends=('fcitx5-mozc-ut: Fcitx5 integration'
            'ibus-mozc: IBus integration'
            'emacs-mozc: Emacs integration')
provides=('mozc=2.31.5712.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=('git+https://github.com/google/mozc.git#commit=58ebfadae04bc46c46e70edc9662347a29d8b7bc'
        'git+https://github.com/abseil/abseil-cpp.git#commit=4447c7562e3bc702ade25105912dce503f0c4010'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=b514bdc898e2951020cbdca1304b75f5950d1f59'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=7cc670c1809e704ebeba90fb430d50e009f36727'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=c0a210388ce78ee7ebfa918810d8224e717a693e'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=bf26bcbb1846f2e9cf35cbfcafcc91c015a1fb22'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=520fbc99080bd2b3111440c23ca0e2edaa4c76c5'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=342b9b00c1cc58c9c124b9d7551fdac9a71ee56b'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=e33ac4ce808fa4253c6c97bf5178e229a4bfb50f'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=5221f96d59b797e915845a4a51b2e8a8543b47e1'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=9789d69e28b7ee7176c9ea0a5826317cfdac75a5'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=c52cdb15e0a014c96050ce1bd02932f50706a3f0'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=3eb0a18fe59f9d60a558585f3f9734c66665cf9b'
        'https://dumps.wikimedia.org/jawiki/20250101/jawiki-20250101-pages-articles-multistream-index.txt.bz2')
noextract=('jawiki-20250101-pages-articles-multistream-index.txt.bz2')
sha256sums=('62df60053b087f4636f1c60bf4fca42abe95f77a2d73274ad9a0f29c891661af'
            'e131bbdd4e207d6cc2930bca9db82d6da9e347175c1125d9d1f2e09a36652278'
            '5168bb8ea19e2f696eeecbdee991f28e496aea206a473fd7cb49b547f5d0c5af'
            'c081295f2c22705e07fc430e152a30b36f949a179075d47d3e12ff3109d43c6a'
            '8a136786407526c64686c3f9990d6416d62c7e2d474ef4a75ced337ecfc58cef'
            '10a13d356071f2b0c2b6dcab1d841fae451f6a2020ee9b901533533fc7ac3008'
            '578ead09a4a3fbf2f70b6af56e0b385ca136c79a4f4a62c777cb13e7a6f733f5'
            'abb86ac4d546c98d7d9a10fdeb1059d6e3395e892d5397fb03179361f37c98fe'
            'a386071ea217c6f808e853f90beae68e921c2401cbdd3f5bc8d4e35d8e537f43'
            '81ed16f6b59f64e08482ea7ab676913584d95ecac00255e981374f02df2188e9'
            '4f3c4b53da5b3fa673bd7bec916b6717a63bafb9fe80991e69a28cab2f7dcb47'
            '840cf0f50ca8d1f6ce1cbaa255e3158eedeafb06e25317c2962f85d6272a0bc9'
            '2bb007c54db6bb70d1771bffaeb05217c0e768cb176b9343ec0a25e9756d9f67'
            '5d4a776a92adb181558bf3ec5012fb30dee00a782e74e2dd60e7c6a3eec4f7cd'
            '6d79ee654bf3a22d66214495aa62f0223cb28b5bdc61bf9500ca54e279fa9bce'
            'd3b1dd5a6419f6f9217d209f8aad6ce853077fbfeaaf73768503efc888f662b8'
            '598c69bf9aaccf29562d7983c649aca6aef14018eb88481a33362958b692fbe4'
            '3cb690b2faf073d0e5c5c158ebc4757a6d794071926b775871d9ee8eb4060bb8')

prepare() {
    cd mozc/src

    git submodule init
    git config submodule.src/third_party/abseil-cpp.url "${srcdir}/abseil-cpp"
    git config submodule.src/third_party/breakpad.url "${srcdir}/breakpad"
    git config submodule.src/third_party/gtest.url "${srcdir}/googletest"
    git config submodule.src/third_party/gyp.url "${srcdir}/gyp"
    git config submodule.src/third_party/japanese_usage_dictionary.url "${srcdir}/japanese-usage-dictionary"
    git config submodule.src/third_party/protobuf.url "${srcdir}/protobuf"
    git config submodule.src/third_party/wil.url "${srcdir}/wil"
    git -c protocol.file.allow=always submodule update

    cd "${srcdir}"/merge-ut-dictionaries/src/merge/

    # Use a dated snapshot for the jawiki dump data
    sed -i -e '65,69d' merge_dictionaries.py
    sed -i -e "s|jawiki-[a-z0-9]\{6,8\}|${srcdir}/jawiki-20250101|g" merge_dictionaries.py

    # Use our local copy of the Mozc repo
    sed -i -e "17s|'https://raw.githubusercontent.com/'.*$|'file://${srcdir}/mozc/src/data/dictionary_oss/id.def'|" merge_dictionaries.py
    sed -i -e '18d' merge_dictionaries.py

    # Compile the UT dictionary
    printf '\nCompiling the UT dictionary...\n\n'

    [[ -e mozcdic-ut.txt ]] && rm mozcdic-ut.txt

    for dict in "${ENABLED_DICTIONARIES[@]}"
    do
        bzip2 -dfk "${srcdir}"/mozcdic-ut-${dict}/mozcdic-ut-${dict}.txt.bz2
        cat "${srcdir}"/mozcdic-ut-${dict}/mozcdic-ut-${dict}.txt >> mozcdic-ut.txt
    done

    python merge_dictionaries.py mozcdic-ut.txt

    # Append the UT dictionary
    cat mozcdic-ut.txt >> "${srcdir}"/mozc/src/data/dictionary_oss/dictionary00.txt
}

build() {
    cd mozc/src

    unset ANDROID_NDK_HOME
    unset ANDROID_HOME
    export JAVA_HOME='/usr/lib/jvm/java-21-openjdk/'

    bazel build server:mozc_server gui/tool:mozc_tool --config oss_linux --compilation_mode opt
}

package() {
    cd mozc/src

    # BSD-3-Clause
    sed -n 67,94p data/installer/credits_en.html > Mozc
    install -Dm644 Mozc "${pkgdir}"/usr/share/licenses/mozc/Mozc
    # BSD-3-Clause
    sed -n 317,344p data/installer/credits_en.html > Breakpad
    install -Dm644 Breakpad "${pkgdir}"/usr/share/licenses/mozc/Breakpad
    # NAIST-2003
    sed -n 355,424p data/installer/credits_en.html > IPAdic
    install -Dm644 IPAdic "${pkgdir}"/usr/share/licenses/mozc/IPAdic
    # BSD-2-Clause
    sed -n 435,457p data/installer/credits_en.html > Japanese-Usage-Dictionary
    install -Dm644 Japanese-Usage-Dictionary "${pkgdir}"/usr/share/licenses/mozc/Japanese-Usage-Dictionary
    # Public Domain Data
    sed -n 468,470p data/installer/credits_en.html > Okinawa-Dictionary
    install -Dm644 Okinawa-Dictionary "${pkgdir}"/usr/share/licenses/mozc/Okinawa-Dictionary
    # BSD-3-Clause
    sed -n 481,513p data/installer/credits_en.html > Protocol-Buffers
    install -Dm644 Protocol-Buffers "${pkgdir}"/usr/share/licenses/mozc/Protocol-Buffers
    # MIT
    sed -n 698,704p data/installer/credits_en.html > Tamachi-Phonetic-Kanji-Alphabet
    install -Dm644 Tamachi-Phonetic-Kanji-Alphabet "${pkgdir}"/usr/share/licenses/mozc/Tamachi-Phonetic-Kanji-Alphabet
    # MIT
    sed -n 762,782p data/installer/credits_en.html > Windows-Implementation-Library
    sed -i -e 's|^[ \t]*||g' Windows-Implementation-Library
    install -Dm644 Windows-Implementation-Library "${pkgdir}"/usr/share/licenses/mozc/Windows-Implementation-Library

    install -Dm755 bazel-bin/server/mozc_server "${pkgdir}"/usr/lib/mozc/mozc_server
    install -Dm755 bazel-bin/gui/tool/mozc_tool "${pkgdir}"/usr/lib/mozc/mozc_tool
}
