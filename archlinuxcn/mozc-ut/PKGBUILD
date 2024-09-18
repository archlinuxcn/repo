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
pkgver=2.30.5595.102.20240918
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
provides=('mozc=2.30.5595.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=('git+https://github.com/google/mozc.git#commit=b52f3048e4becb08f0addc997e40540f6baa5508'
        'git+https://github.com/abseil/abseil-cpp.git#commit=4447c7562e3bc702ade25105912dce503f0c4010'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=b514bdc898e2951020cbdca1304b75f5950d1f59'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=7cc670c1809e704ebeba90fb430d50e009f36727'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=35dfcca5c8657f2bf78bc000baa349c322ecb771'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=50fee0397b87fe508f9edd45bac56f5290d8ce66'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=b2112277d0d479b9218f42772356da3601b3e8cf'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=08814f70cc0cc9b0f4757fa46f40d918dfd7073d'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=b7035b88db25ad1a933f05a33f193711c6c3b2db'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=bbf04c902d8640d0799d151272c968cea7d91de9'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=4525819546a26fc994d7ca4a2e883fde14bf908c'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=7300f19e6a3f27334ed7af64589de8782549a13f'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=a754f1fff5fded62cc066aa6be0ab0169059a144'
        'https://dumps.wikimedia.org/jawiki/20240901/jawiki-20240901-all-titles-in-ns0.gz')
noextract=('jawiki-20240901-all-titles-in-ns0.gz')
sha256sums=('367dbf90873203766785ce17e00df56d9682af6d0082a9974934d599e7e29e93'
            'e131bbdd4e207d6cc2930bca9db82d6da9e347175c1125d9d1f2e09a36652278'
            '5168bb8ea19e2f696eeecbdee991f28e496aea206a473fd7cb49b547f5d0c5af'
            'c081295f2c22705e07fc430e152a30b36f949a179075d47d3e12ff3109d43c6a'
            '8a136786407526c64686c3f9990d6416d62c7e2d474ef4a75ced337ecfc58cef'
            '10a13d356071f2b0c2b6dcab1d841fae451f6a2020ee9b901533533fc7ac3008'
            '578ead09a4a3fbf2f70b6af56e0b385ca136c79a4f4a62c777cb13e7a6f733f5'
            'abb86ac4d546c98d7d9a10fdeb1059d6e3395e892d5397fb03179361f37c98fe'
            '11759b412db8382c4ae956c45202951575edcede10bfac3a7bb16dbb012da8de'
            '1e7a58fcac2599be29b0ced9cb0bb8210703c1a568e06038d2779106a100a33a'
            '86e95d1aba4b2ab5ec67f7b2d59d14fd1d20ecf08ef4e12f7c20e122ee61d2b1'
            '21dd679762febe1ec92f206b100a84c3ecb33360c7ae4a89f7400407b0fcff70'
            'b348668059cc75744b4eb82fb8ae1c0cc72a4dc6d24c430db652db0090149534'
            '7d6556a7f6a101e499f793c48d438a86ce57ad4b299721fd02b15e5e2636a6cc'
            'b20c240b9a76d92afe0da3f5bddcf1dd09dd1ad8b273523806127669a8c469fd'
            '5afa03b188822e5e056dc7517e838935f5c5547f8cb2adee4c60059805850b97'
            'd58121b2b1166d7349e95e331571111282b524003b5ee3e53db9cd5150ba439f'
            'baea6951c6a0622833557c7e767f7a08e786133ef294b3cf2ed5f319f763babe')

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
    sed -i -e 's|jawiki-[a-z0-9]\{6,8\}|jawiki-20240901|g' count_word_hits.py apply_word_hits.py

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
