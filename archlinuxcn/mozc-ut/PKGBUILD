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
pkgver=2.30.5544.102.20240731
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
provides=('mozc=2.30.5544.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=('git+https://github.com/google/mozc.git#commit=5e6abfe1853b080766def432b746a9bed79e54b0'
        'git+https://github.com/abseil/abseil-cpp.git#commit=2f9e432cce407ce0ae50676696666f33a77d42ac'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=58d77fa8070e8cec2dc1ed015d66b454c8d78850'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=a978b75794a6ce4547c9db08a115c458d9190934'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=1f1cdcf545b952f84fdad78d58c0db7a662b592d'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=50fee0397b87fe508f9edd45bac56f5290d8ce66'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=b2112277d0d479b9218f42772356da3601b3e8cf'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=29dd6d3202119d88a2356a11300b7b338f5cb950'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=b7035b88db25ad1a933f05a33f193711c6c3b2db'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=5df5cedaef3b55c509cacfbf3e97ded852535a1b'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=5c2167541200528d8b25214c52be7a4c3dd3b89b'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=7300f19e6a3f27334ed7af64589de8782549a13f'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=a754f1fff5fded62cc066aa6be0ab0169059a144'
        'https://dumps.wikimedia.org/jawiki/20240720/jawiki-20240720-all-titles-in-ns0.gz')
noextract=('jawiki-20240720-all-titles-in-ns0.gz')
sha256sums=('7af613c21dae383a410b270a21d970ecdc63100fd343932e44884fda4fe24f3c'
            '8380cac08316c35118999b95845b8c28d9c9c4688402960fb1558d5eeda90f73'
            '5168bb8ea19e2f696eeecbdee991f28e496aea206a473fd7cb49b547f5d0c5af'
            '2acda2cf88e375a7638f521f25c61b308d0eae8a7e188a54fafa2f2c8c2a063f'
            '8a136786407526c64686c3f9990d6416d62c7e2d474ef4a75ced337ecfc58cef'
            '10a13d356071f2b0c2b6dcab1d841fae451f6a2020ee9b901533533fc7ac3008'
            'f09520ceeb7f1f1bb7e1cb61a8cd7a490fff84302ed5dc91f923f0e82ee191dc'
            'abb86ac4d546c98d7d9a10fdeb1059d6e3395e892d5397fb03179361f37c98fe'
            '8f81d5ea8044007af572a7432f1f7a2b40f4506a71dfa139239b976b4bdd5ddb'
            '1e7a58fcac2599be29b0ced9cb0bb8210703c1a568e06038d2779106a100a33a'
            '86e95d1aba4b2ab5ec67f7b2d59d14fd1d20ecf08ef4e12f7c20e122ee61d2b1'
            '05d9e8bd344a51d41905f0d8010dede5b26f5e4ba871b07f861d317e7b0c4be5'
            'b348668059cc75744b4eb82fb8ae1c0cc72a4dc6d24c430db652db0090149534'
            '5d26dfb78283e515f4a1d9b4a0c3319b9240f2b708d5499cc3c01bb2e9f29f3d'
            '657be228b7e16bda1c551622835ad7f1ea76fdee5a1a257bdfa332ea32ebecfe'
            '5afa03b188822e5e056dc7517e838935f5c5547f8cb2adee4c60059805850b97'
            'd58121b2b1166d7349e95e331571111282b524003b5ee3e53db9cd5150ba439f'
            'b7c43de8540468e26cd5c73dc924ab558c83e08fc3bdf5e1e94c6f5111c71d69')

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
    sed -i -e "s|file_name = \"jawiki-|file_name = \"${srcdir}/jawiki-|g" count_word_hits.py
    sed -i -e 's|jawiki-[a-z0-9]\{6,8\}|jawiki-20240720|g' count_word_hits.py apply_word_hits.py

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
