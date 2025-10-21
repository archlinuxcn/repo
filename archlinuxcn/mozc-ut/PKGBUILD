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
pkgver=2.32.5981.102.20251020
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
provides=('mozc=2.32.5981.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=('git+https://github.com/google/mozc.git#commit=8b9b14cb0a41c4f353e5d4c76619044522af885a'
        'git+https://github.com/abseil/abseil-cpp.git#commit=4447c7562e3bc702ade25105912dce503f0c4010'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=b514bdc898e2951020cbdca1304b75f5950d1f59'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=7cc670c1809e704ebeba90fb430d50e009f36727'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=e173cd106891d76e73263711036070c2b31d7f9d'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=69d40eed4e9cf016384d9629920fefa199116ea2'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=4f82fc1003403874d9d4dd9adecfeff17f06a1f1'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=95d6e3d24a3e22700b57b162bcd18c87b1d213e9'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=e33ac4ce808fa4253c6c97bf5178e229a4bfb50f'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=d0ad47deea54f3a6818efacd93e20ba5bac93213'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=5d91fc6fdc33f802174398ca208ded7f8c561427'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=384ad926e306d5308839c6dedb63696f11703968'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=662ef1939eb6e9297d91abd18e53bbd0f8690914'
        'https://dumps.wikimedia.org/jawiki/20251001/jawiki-20251001-pages-articles-multistream-index.txt.bz2')
noextract=('jawiki-20251001-pages-articles-multistream-index.txt.bz2')
b2sums=('8ff3b4a900f9b4e71cf5b51c23db3a0c0dd25889a07ee6a3afb2de2669a01f2ce43b5d975c8ff121daaabd6608b8deb610e38d7ad284bcaef8d84fd0735592c1'
        '45ca8cc8c61d9696365d19064e36be9edf38112f57e413063b0f72155fc8a67147768386eae005e1e23e9c95ede95ce1df0c630b1704a84f2d3e05397b0ddade'
        'eb54c87947561d6d985b3a244860a247a6ae41e5667ed6f4687dc864a3f02bc0b52d111c5b16025e06f44a1db31d7731c42eb38725521512b4c102475aebf585'
        '89cbc8965037def33f8c46210b16c35e306fceb437f74aa0133e9a914dbc876d363394f4e7b94485e6d518e78f20db07a832751b0afd7a732e37c22eb1896435'
        'a6de318769bc421794d46b207eceb92920c7610cf107249183b40801fec3b1b079d679565de05e6a24b9970623563d914a8a674c5481a498d9fecf5a23e214ca'
        '7abe2c678b7983fbc86b11b25e6f6f1dfc4dfe75b8db40510849ce8b06f415dc4932c16fa0bae213fa0a466d7a837363d0860024ac0e5bcb87f64dc23561c220'
        'd284ef75e86d80000a65afe5e1d60493a70af47acb664432e8e12e9cf84a33acfebd7751f75b4693d187c36def1bdca1d5f9e336dd2edea6c28120064f7956c3'
        '8d105ce08ca103db180ec99c7845eee08d15abcc3e7cfce51d1b565a4ed5942be40aaefbc78e80e09e84c5583640d6a33feed7d3d9ec572c4a9ebf505ea6a7f5'
        'eb5fa8ba9d72e9c79465c1f1af8228267a5a22263afd62e5fc5123b9daca3fc8c016704904426e14f1b871efd7c762b4915705ac51d3bf0d19df1f062ec52071'
        'f585f3d3463e01669eea5568198cd9bf49492a0a1f5fc3afa7ce3fc2ce744ce02e4fe970cc2ab9b40fa287569c66ed8fb8fec6f580042c2fb76850e3cd93da6c'
        '9bb7d0dc31341b91f31831189ac7a3443cfc845b9f6f2eb970c83490c78c9fc9fe85ed50d64ffac94997062c229a95ba02bf15ce0ced14ba551c89a267e814ce'
        '7a359c989b4316398a243e0191c492360f11c7122d979ad0ddbd74b27929516769f2b4425038ff467145186bc1677cb71738770c906faad65be2c831f6ea98d2'
        'b2a8a919973d1a74e18b69adf7753cf0cacfa038b3c97bb37c57f6ff0749092e323befd56ae58a3eea637cefe2a3f55280f391d25fd4639dbca3ede2e8472f44'
        '23190bc9a2f555c8a3744917417960c9c9b42ebe2fed6d084869dc75da1f49daf84782fc35cec1ad401bb381bf5eef8ba0cf9e8c5150fc0c07b636e9bab10a79'
        'd972e4a113b6a6087d7fd7e6a39609d605771dc8a41b872628562c4593217095f6beb26b9d93e843d5713de9fedcf3e313366eb6ba4973f31ba41cfdf30d4256'
        '3c63f51241bd659e5841f26b11620ce755663aafe2a7c750738bb840df2e50de6b033f6cbf43e8a74258b1d07e86f1487b4caf1954e99354ce8f526ab469623a'
        '471c91bb69846ead9a3bf48cf61433705cc0fbaedc86a2fde45f2527c13b2364598222d4d8dc5196a3ba0c62469a762596c4bf47f173b9c394927c33940002fb'
        'bb2e781571f09d1a69485001193bce370cd47212a363efdc3306da36fb931ffa54a6fcef31ba2d33fb2ca02226a71cd50f305bf13b95c641dc4aecd3dba1b5f2')

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
    sed -i -e "s|jawiki-[a-z0-9]\{6,8\}|${srcdir}/jawiki-20251001|g" merge_dictionaries.py

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
