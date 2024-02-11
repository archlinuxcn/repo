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
pkgver=2.29.5374.102.20240211
pkgrel=1
pkgdesc='The Open Source edition of Google Japanese Input bundled with the UT dictionary'
arch=('x86_64')
url='https://github.com/google/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-3.0-only AND MIT AND NAIST-2003 AND Unicode-3.0')
depends=('qt6-base')
makedepends=('bazel' 'git' 'python' 'rsync' 'ruby' 'wget')
optdepends=('fcitx5-mozc-ut: Fcitx5 integration'
            'fcitx-mozc-ut: Fcitx integration'
            'ibus-mozc: IBus integration'
            'emacs-mozc: Emacs integration')
provides=('mozc=2.29.5374.102')
conflicts=('mozc')
options=(!distcc !ccache)
source=("${pkgname}-git::git+https://github.com/google/mozc.git#commit=c2fcbf6515c5884437977de46187c16a8cb7bb50"
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=a3d6fc4005aff2092657ebca98b9de226e1c617f'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=4e548e6356b874c76e8db438bf4d8a0b452f2435'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=b2eec665b81214082d61acee1c5a1b5b115baf1a'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=6e08b8c823f3d2d09064ad2080e7a16552a7b473'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=bf9d0d217107f2fb2e7d1a26648ef429d9fdcd27'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=8a500f82c553936cbdd33b85955120e731069d44'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=a847a02e0137ab9e2fdbbaaf120826f870408ca6'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=ee94f6546ce52edfeec0fd203030f52d4d99656f'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=55f61c3fca81dec661c36c73eb29b2631c8ed618'
        'https://dumps.wikimedia.org/jawiki/20240201/jawiki-20240201-all-titles-in-ns0.gz')
noextract=('jawiki-20240201-all-titles-in-ns0.gz')
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
            '6058ffb12f6d090717092d4174b6ab9fbd76a2e9798eb0d8cc09b330a2dc9760')

prepare() {
    cd ${pkgname}-git/src

    git submodule update --init --recursive

    cd "${srcdir}"/merge-ut-dictionaries/src/

    # Use our local copy of the Mozc repo
    sed -i -e "s|https://raw.githubusercontent.com/google/mozc/master/src|${srcdir}/${pkgname}-git/src|" remove_duplicate_ut_entries.rb

    # Use a dated snapshot for the JAWiki dump data
    sed -i -e '/wget/d' count_word_hits.rb
    sed -i -e "s|filename = \"jawiki-|filename = \"${srcdir}/jawiki-|g" count_word_hits.rb
    sed -i -e 's|jawiki-[a-z0-9]\{6,8\}|jawiki-20240201|g' count_word_hits.rb apply_word_hits.rb

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

    install -Dm644 ../LICENSE                                   "${pkgdir}"/usr/share/licenses/mozc/LICENSE
    install -Dm644 data/installer/credits_en.html               "${pkgdir}"/usr/share/licenses/mozc/Submodules

    install -Dm755 bazel-bin/server/mozc_server                 "${pkgdir}"/usr/lib/mozc/mozc_server
    install -Dm755 bazel-bin/gui/tool/mozc_tool                 "${pkgdir}"/usr/lib/mozc/mozc_tool
}
