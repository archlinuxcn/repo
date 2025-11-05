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
pkgver=2.32.5994.102.20251105
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
provides=('mozc=2.32.5994.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=('git+https://github.com/google/mozc.git#commit=d9c3f195582de6b0baa07ecb81a04e8902acf9af'
        'git+https://github.com/abseil/abseil-cpp.git#commit=4447c7562e3bc702ade25105912dce503f0c4010'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=b514bdc898e2951020cbdca1304b75f5950d1f59'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=7cc670c1809e704ebeba90fb430d50e009f36727'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=05942c4da7a4066882e8aa3c972bce8c880ba3cf'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=69d40eed4e9cf016384d9629920fefa199116ea2'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=4f82fc1003403874d9d4dd9adecfeff17f06a1f1'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=17c5ca473b0b001460215fcd42c9cc520634516f'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=e33ac4ce808fa4253c6c97bf5178e229a4bfb50f'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=0310f591108cffdfc9e39ff56e17fb3bb188b2e0'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=b10b5c2c946e68f32cce4173cfd8c4676e4145b9'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=384ad926e306d5308839c6dedb63696f11703968'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=33f9835cfafc85d6761037342debec0e7ae8aa17'
        'https://dumps.wikimedia.org/jawiki/20251101/jawiki-20251101-pages-articles-multistream-index.txt.bz2')
noextract=('jawiki-20251101-pages-articles-multistream-index.txt.bz2')
b2sums=('d522977e6612b69e8c1088e0a7f22c1ed346e334a3778824ef027718372b5b17145b5644a6edb68c8ab606643f7281f75c9437b0f2a22103cb482bf2fc7a24fb'
        '45ca8cc8c61d9696365d19064e36be9edf38112f57e413063b0f72155fc8a67147768386eae005e1e23e9c95ede95ce1df0c630b1704a84f2d3e05397b0ddade'
        'eb54c87947561d6d985b3a244860a247a6ae41e5667ed6f4687dc864a3f02bc0b52d111c5b16025e06f44a1db31d7731c42eb38725521512b4c102475aebf585'
        '89cbc8965037def33f8c46210b16c35e306fceb437f74aa0133e9a914dbc876d363394f4e7b94485e6d518e78f20db07a832751b0afd7a732e37c22eb1896435'
        'a6de318769bc421794d46b207eceb92920c7610cf107249183b40801fec3b1b079d679565de05e6a24b9970623563d914a8a674c5481a498d9fecf5a23e214ca'
        '7abe2c678b7983fbc86b11b25e6f6f1dfc4dfe75b8db40510849ce8b06f415dc4932c16fa0bae213fa0a466d7a837363d0860024ac0e5bcb87f64dc23561c220'
        'd284ef75e86d80000a65afe5e1d60493a70af47acb664432e8e12e9cf84a33acfebd7751f75b4693d187c36def1bdca1d5f9e336dd2edea6c28120064f7956c3'
        '8d105ce08ca103db180ec99c7845eee08d15abcc3e7cfce51d1b565a4ed5942be40aaefbc78e80e09e84c5583640d6a33feed7d3d9ec572c4a9ebf505ea6a7f5'
        '0d892a32ef01d77adebb9d646aa5a78713946fa74c8e1b4c1183f40fe8afd0605281280b7d6d8e15bb3d3bc0cc481dc624e27cca4fe023235265107fe803ead0'
        'f585f3d3463e01669eea5568198cd9bf49492a0a1f5fc3afa7ce3fc2ce744ce02e4fe970cc2ab9b40fa287569c66ed8fb8fec6f580042c2fb76850e3cd93da6c'
        '9bb7d0dc31341b91f31831189ac7a3443cfc845b9f6f2eb970c83490c78c9fc9fe85ed50d64ffac94997062c229a95ba02bf15ce0ced14ba551c89a267e814ce'
        '4ea3b9aa4a729ca78d8a114f5afffb39fb00c999372d890a2b0bb91443b4fd1e62ed5738538aec26d47ce15f251a62b77e6be886e067ad0aa422495840e18ff7'
        'b2a8a919973d1a74e18b69adf7753cf0cacfa038b3c97bb37c57f6ff0749092e323befd56ae58a3eea637cefe2a3f55280f391d25fd4639dbca3ede2e8472f44'
        '194b02857dfe477bea93e47c844eb4a6757988745e0c4b8f00ad07704b8393b8384e920ad041d1344b42bba9be0ba10df53e640cc5d8d733da812866cb6a72e1'
        '1fefd676841f6534d93d0be22dc6cdacf516282db159f91372a9d2258143ffd555d59d07a2b4543e5d2fa79a3496a174687d0b397ca1ba7a9c2c1b53ab7555b9'
        '3c63f51241bd659e5841f26b11620ce755663aafe2a7c750738bb840df2e50de6b033f6cbf43e8a74258b1d07e86f1487b4caf1954e99354ce8f526ab469623a'
        'fad5b6d720c6e4a76947a790ac727fbacd03d6da76802b7f75b1f07fcdeae88bd401d0ba130073e4804efca481aaedf039c7a9e60b5c07f7eb5ed42cd3470839'
        'bc23729bb43c750a757cf140638551edf663ef7bf52095033e859391a6109a7490c30156defb389fc95483ea4d4c4da561b04dc7b511d8dd6843b0a60a989139')

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
    sed -i -e '124,127d' merge_dictionaries.py
    sed -i -e "s|jawiki-[a-z0-9]\{6,8\}|${srcdir}/jawiki-20251101|g" merge_dictionaries.py

    # Use our local copy of the Mozc repo
    sed -i -e "65s|os\.path\.exists(f'mozc-{date}.zip')|False|" merge_dictionaries.py
    sed -i -e '71s|zip_ref\.||' merge_dictionaries.py
    sed -i -e "72s|mozc-master/src/data/dictionary_oss/id\.def|${srcdir}/mozc/src/data/dictionary_oss/id\.def|" merge_dictionaries.py
    sed -i -e '74s|id_mozc\.|file\.read()\.|' merge_dictionaries.py
    sed -i -e '80s|zip_ref\.||' merge_dictionaries.py
    sed -i -e "81s|mozc-master/src/data/dictionary_oss/|${srcdir}/mozc/src/data/dictionary_oss/|" merge_dictionaries.py
    sed -i -e '83s|decode()\.||' merge_dictionaries.py
    sed -i -e '53,64d;66,69d;73d' merge_dictionaries.py

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
    sed -n 715,735p data/installer/credits_en.html > Windows-Implementation-Library
    sed -i -e 's|^[ \t]*||g' Windows-Implementation-Library
    install -Dm644 Windows-Implementation-Library "${pkgdir}"/usr/share/licenses/mozc/Windows-Implementation-Library

    install -Dm755 bazel-bin/server/mozc_server "${pkgdir}"/usr/lib/mozc/mozc_server
    install -Dm755 bazel-bin/gui/tool/mozc_tool "${pkgdir}"/usr/lib/mozc/mozc_tool
}
