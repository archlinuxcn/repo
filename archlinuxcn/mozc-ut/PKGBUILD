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
pkgver=2.30.5520.102.20240712
pkgrel=1
pkgdesc='The Open Source edition of Google Japanese Input bundled with the UT dictionary'
arch=('x86_64')
url='https://github.com/google/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-2.0-only AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('qt6-base')
makedepends=('bazel' 'git' 'python')
optdepends=('fcitx5-mozc-ut: Fcitx5 integration'
            'ibus-mozc: IBus integration'
            'emacs-mozc: Emacs integration')
provides=('mozc=2.30.5520.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=("${pkgname}-git::git+https://github.com/google/mozc.git#commit=d2fc9c7d9269cc84b9a4a680cafc382a55e90f42"
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=6c5f28bbeba0aed95d1b56d7d027723cc1ef00cf'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=9e71156adf8cbaf148fe76bc12539f55b461e163'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=38f7f74726d36b4ece85adadd3739b6177592108'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=afd4a37c1ba1fcd4302043cde73525e84b2c0eec'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=3aa888db141db910e4161598fcd929e49794533d'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=e1049584984ac9376685937661ae18c968e25c48'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=faaf64ed7b8eac6775be9ad2269aa10d7fb992c3'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=e1f26b891ea80f52f846791959fa8e4acf36fa99'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=3ad17aa28c2e817acecbba30040c776fa9619fd4'
        'https://dumps.wikimedia.org/jawiki/20240701/jawiki-20240701-all-titles-in-ns0.gz')
noextract=('jawiki-20240701-all-titles-in-ns0.gz')
sha256sums=('195f1218deae0daa22a6ae0e2b2f42eb900e314e3442ef549b6f9d666aa68644'
            '365909baf4ebc914899e73d02d93f6ce1372461c73668f1d7cadfe041c8a7526'
            'bf5c1313d9f1d67ed0eb414fda622be9a8460be645dbcc2fbf2612b786746977'
            'b9bc9db94ddc27a5558a3a8867ebb2a27d714d7ac625d31c8c52ccf0d5f72839'
            'e6ebf5f006c76d13a6685215d1a32c80b2e4f1a6b47fc42016907af6c778c872'
            'f4afc1ef8ffc94523e6b5144ca76add31aeaa8a8388739cb90475a6d87d0f720'
            'ce1341bbcfe4488f95e5c2d4bf9e4157817ed834d2e25a476ba6f3591b65fba3'
            '98bf831147dd64871737d71cbdfb92474e3dc1a5baf7bd622399276e1631d72c'
            '1b60bcec3a3f6c853464231a83378e0f4423dc57cbeda681e3ed5a0a6ed73489'
            'f65c9dbca49b60801af6b781751257cd8f5371c1847962c760e3cb6cd09d9222'
            'b6c426a38d5c9f41547e48c8c5a8a7955e012119d231e701ae5437bf700a622a')

prepare() {
    cd ${pkgname}-git/src

    git submodule update --init --recursive

    cd "${srcdir}"/merge-ut-dictionaries/src/

    # Use our local copy of the Mozc repo
    sed -i -e "s|https://raw.githubusercontent.com/google/mozc/master/src|file://${srcdir}/${pkgname}-git/src|" remove_duplicate_ut_entries.py

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
    cat mozcdic-ut.txt >> "${srcdir}"/${pkgname}-git/src/data/dictionary_oss/dictionary00.txt
}

build() {
    cd ${pkgname}-git/src

    unset ANDROID_NDK_HOME
    unset ANDROID_HOME
    export JAVA_HOME='/usr/lib/jvm/java-21-openjdk/'

    # Temp fix for GCC 14
    sed -i -e '/Werror/d' third_party/protobuf/build_defs/cpp_opts.bzl

    bazel build server:mozc_server gui/tool:mozc_tool --config oss_linux --compilation_mode opt
}

package() {
    cd ${pkgname}-git/src

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
