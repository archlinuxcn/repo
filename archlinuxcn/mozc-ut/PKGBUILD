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
pkgver=2.29.5400.102.20240308
pkgrel=1
pkgdesc='The Open Source edition of Google Japanese Input bundled with the UT dictionary'
arch=('x86_64')
url='https://github.com/google/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-2.0-only AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('qt6-base')
makedepends=('bazel' 'git' 'python' 'rsync' 'ruby' 'wget')
optdepends=('fcitx5-mozc-ut: Fcitx5 integration'
            'ibus-mozc: IBus integration'
            'emacs-mozc: Emacs integration')
provides=('mozc=2.29.5400.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=("${pkgname}-git::git+https://github.com/google/mozc.git#commit=e87c83febda07ffd93fcbfc4ea67562f40423005"
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=a3d6fc4005aff2092657ebca98b9de226e1c617f'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=4e548e6356b874c76e8db438bf4d8a0b452f2435'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=16283aa0c2d394a3a000eca4fa3e95eb365698c6'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=bd82687d32ae838f1e163d3d2c6ad18740af53f2'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=bf9d0d217107f2fb2e7d1a26648ef429d9fdcd27'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=6cc099cefc928bc37854c538e030114df3d5b42d'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=a847a02e0137ab9e2fdbbaaf120826f870408ca6'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=ee94f6546ce52edfeec0fd203030f52d4d99656f'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=55f61c3fca81dec661c36c73eb29b2631c8ed618'
        'https://dumps.wikimedia.org/jawiki/20240301/jawiki-20240301-all-titles-in-ns0.gz')
noextract=('jawiki-20240301-all-titles-in-ns0.gz')
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'b6afec2803d9fcd2e994e2e8556a7665d5b32bf17b4d503d15309829fbc5b995')

prepare() {
    cd ${pkgname}-git/src

    git submodule update --init --recursive

    cd "${srcdir}"/merge-ut-dictionaries/src/

    # Use our local copy of the Mozc repo
    sed -i -e "s|https://raw.githubusercontent.com/google/mozc/master/src|${srcdir}/${pkgname}-git/src|" remove_duplicate_ut_entries.rb

    # Use a dated snapshot for the JAWiki dump data
    sed -i -e '/wget/d' count_word_hits.rb
    sed -i -e "s|filename = \"jawiki-|filename = \"${srcdir}/jawiki-|g" count_word_hits.rb
    sed -i -e 's|jawiki-[a-z0-9]\{6,8\}|jawiki-20240301|g' count_word_hits.rb apply_word_hits.rb

    # Compile the UT dictionary
    printf '\nCompiling the UT dictionary...\n\n'

    [[ -e mozcdic-ut.txt ]] && rm mozcdic-ut.txt

    for dict in "${ENABLED_DICTIONARIES[@]}"
    do
        tar -xf "${srcdir}"/mozcdic-ut-${dict}/mozcdic-ut-${dict}.txt.tar.bz2
        cat mozcdic-ut-${dict}.txt >> mozcdic-ut.txt
    done

    ruby remove_duplicate_ut_entries.rb mozcdic-ut.txt
    ruby count_word_hits.rb
    ruby apply_word_hits.rb mozcdic-ut.txt

    # Append the UT dictionary
    cat mozcdic-ut.txt >> "${srcdir}"/${pkgname}-git/src/data/dictionary_oss/dictionary00.txt
}

build() {
    cd ${pkgname}-git/src

    unset ANDROID_NDK_HOME
    unset ANDROID_HOME
    export JAVA_HOME='/usr/lib/jvm/java-11-openjdk/'
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

    install -Dm644 bazel-bin/server/mozc_server "${pkgdir}"/usr/lib/mozc/mozc_server
    install -Dm644 bazel-bin/gui/tool/mozc_tool "${pkgdir}"/usr/lib/mozc/mozc_tool
}
