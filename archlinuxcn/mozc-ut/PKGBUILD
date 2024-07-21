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
pkgver=2.30.5520.102.20240721
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
provides=('mozc=2.30.5520.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=('git+https://github.com/google/mozc.git#commit=d2fc9c7d9269cc84b9a4a680cafc382a55e90f42'
        'git+https://github.com/abseil/abseil-cpp.git#commit=2f9e432cce407ce0ae50676696666f33a77d42ac'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=58d77fa8070e8cec2dc1ed015d66b454c8d78850'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=a978b75794a6ce4547c9db08a115c458d9190934'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=95582779c7f906aaacf97625f565a1e7af0c1fae'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=b3d151c189c55b00e3e384ddb847cc76b3565746'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=a3febcb019454af445809965d4f64baddd962c73'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=263fe3243f98e1a9438f8f4c3bf1ae5ade371a6c'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=c1524034b08fad881957d72f5b29931cc5964f8c'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=e1049584984ac9376685937661ae18c968e25c48'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=99cb804417a5816933d87ac9d2caeb993ea98339'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=d5bf4e970e35c0ccd51c3a24ff301ed1d0770cef'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=1aa3d3d56bf26a77010febfa87e1a6c745770dd7'
        'https://dumps.wikimedia.org/jawiki/20240701/jawiki-20240701-all-titles-in-ns0.gz')
noextract=('jawiki-20240701-all-titles-in-ns0.gz')
sha256sums=('195f1218deae0daa22a6ae0e2b2f42eb900e314e3442ef549b6f9d666aa68644'
            '8380cac08316c35118999b95845b8c28d9c9c4688402960fb1558d5eeda90f73'
            '5168bb8ea19e2f696eeecbdee991f28e496aea206a473fd7cb49b547f5d0c5af'
            '2acda2cf88e375a7638f521f25c61b308d0eae8a7e188a54fafa2f2c8c2a063f'
            '8a136786407526c64686c3f9990d6416d62c7e2d474ef4a75ced337ecfc58cef'
            '10a13d356071f2b0c2b6dcab1d841fae451f6a2020ee9b901533533fc7ac3008'
            'f09520ceeb7f1f1bb7e1cb61a8cd7a490fff84302ed5dc91f923f0e82ee191dc'
            'abb86ac4d546c98d7d9a10fdeb1059d6e3395e892d5397fb03179361f37c98fe'
            '3ee1ed7438f7ad3963ed4129a47ff7ac7d72b56f6d9c48da9e19d00f72d80541'
            '80f0189f8047a3cb28d45d8309f1908e53dce00ddb1ca087aeff7b410839ecef'
            '1366916e2d07d6e66fab69ba1d46a2d1b786d563a3e82f5a92978117e9b24a65'
            '12d3988f49be34e5f9b0f5f05c7ac85491654f905c90e90b493b6920b6886a59'
            'c190da70b1e35bae2e58d568d5e1ed4f05e9941e7265fe45d252b951f00dbd2d'
            'ce1341bbcfe4488f95e5c2d4bf9e4157817ed834d2e25a476ba6f3591b65fba3'
            '0ed13d4ab3c2aebf8389b4fbcf88c877fb5e62d06a653b1b2c0f78ad6e82ecab'
            'f701e403045a39dbf8113e6482941681caf57443f447db4d4ec5ec3dc66ecf87'
            '9d67b0375cb50a7ad879847f05c4fdaaba1b45a667dad77d3e8a60acd8baaa14'
            'b6c426a38d5c9f41547e48c8c5a8a7955e012119d231e701ae5437bf700a622a')

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

    cd "${srcdir}"/merge-ut-dictionaries/src/

    # Use our local copy of the Mozc repo
    sed -i -e "s|https://raw.githubusercontent.com/google/mozc/master/src|file://${srcdir}/mozc/src|" remove_duplicate_ut_entries.py

    # Use a dated snapshot for the JAWiki dump data
    sed -i -e '/wget/d' count_word_hits.py
    sed -i -e "s|filename = \"jawiki-|filename = \"${srcdir}/jawiki-|g" count_word_hits.py
    sed -i -e 's|jawiki-[a-z0-9]\{6,8\}|jawiki-20240701|g' count_word_hits.py apply_word_hits.py

    # Compile the UT dictionary
    printf '\nCompiling the UT dictionary...\n\n'

    [[ -e mozcdic-ut.txt ]] && rm mozcdic-ut.txt

    for dict in "${ENABLED_DICTIONARIES[@]}"
    do
        tar -xf "${srcdir}"/mozcdic-ut-${dict}/mozcdic-ut-${dict}.txt.tar.bz2
        cat mozcdic-ut-${dict}.txt >> mozcdic-ut.txt
    done

    python remove_duplicate_ut_entries.py mozcdic-ut.txt
    python count_word_hits.py
    python apply_word_hits.py mozcdic-ut.txt

    # Append the UT dictionary
    cat mozcdic-ut.txt >> "${srcdir}"/mozc/src/data/dictionary_oss/dictionary00.txt
}

build() {
    cd mozc/src

    unset ANDROID_NDK_HOME
    unset ANDROID_HOME
    export JAVA_HOME='/usr/lib/jvm/java-21-openjdk/'

    bazel build server:mozc_server gui/tool:mozc_tool --config oss_linux --compilation_mode opt --copt='-Wno-maybe-uninitialized' --host_copt='-Wno-maybe-uninitialized'
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
