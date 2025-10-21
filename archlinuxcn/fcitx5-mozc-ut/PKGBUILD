# Maintainer: Nocifer <apmichalopoulos at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>

pkgname='fcitx5-mozc-ut'
pkgver=2.32.5981.102
pkgrel=1
pkgdesc='Mozc module for Fcitx5'
arch=('x86_64')
url='https://github.com/fcitx/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('fcitx5' 'mozc>=2.32.5981.102')
makedepends=('bazel' 'git' 'python' 'qt6-base')
optdepends=('fcitx5-configtool')
provides=('fcitx5-mozc=2.32.5981.102')
conflicts=('fcitx5-mozc')
options=(!distcc !ccache)
source=('mozc-fcitx::git+https://github.com/fcitx/mozc.git#commit=29e2b953deacc1b6aa35c28ffedb692399ee4c05'
        'git+https://github.com/abseil/abseil-cpp.git#commit=4447c7562e3bc702ade25105912dce503f0c4010'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=b514bdc898e2951020cbdca1304b75f5950d1f59'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=7cc670c1809e704ebeba90fb430d50e009f36727'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d')
b2sums=('463c1fb3d6c4fb3c19b3f334c1af1fa5b4f6b42af71cb4ff31d45a3ea19945f054546d9412ccd10f1caf3a7b375da0729d56eb9a8323d5c535ef214f636d25f0'
        '45ca8cc8c61d9696365d19064e36be9edf38112f57e413063b0f72155fc8a67147768386eae005e1e23e9c95ede95ce1df0c630b1704a84f2d3e05397b0ddade'
        'eb54c87947561d6d985b3a244860a247a6ae41e5667ed6f4687dc864a3f02bc0b52d111c5b16025e06f44a1db31d7731c42eb38725521512b4c102475aebf585'
        '89cbc8965037def33f8c46210b16c35e306fceb437f74aa0133e9a914dbc876d363394f4e7b94485e6d518e78f20db07a832751b0afd7a732e37c22eb1896435'
        'a6de318769bc421794d46b207eceb92920c7610cf107249183b40801fec3b1b079d679565de05e6a24b9970623563d914a8a674c5481a498d9fecf5a23e214ca'
        '7abe2c678b7983fbc86b11b25e6f6f1dfc4dfe75b8db40510849ce8b06f415dc4932c16fa0bae213fa0a466d7a837363d0860024ac0e5bcb87f64dc23561c220'
        'd284ef75e86d80000a65afe5e1d60493a70af47acb664432e8e12e9cf84a33acfebd7751f75b4693d187c36def1bdca1d5f9e336dd2edea6c28120064f7956c3'
        '8d105ce08ca103db180ec99c7845eee08d15abcc3e7cfce51d1b565a4ed5942be40aaefbc78e80e09e84c5583640d6a33feed7d3d9ec572c4a9ebf505ea6a7f5')

prepare() {
    cd mozc-fcitx/src

    git submodule init
    git config submodule.src/third_party/abseil-cpp.url "${srcdir}/abseil-cpp"
    git config submodule.src/third_party/breakpad.url "${srcdir}/breakpad"
    git config submodule.src/third_party/gtest.url "${srcdir}/googletest"
    git config submodule.src/third_party/gyp.url "${srcdir}/gyp"
    git config submodule.src/third_party/japanese_usage_dictionary.url "${srcdir}/japanese-usage-dictionary"
    git config submodule.src/third_party/protobuf.url "${srcdir}/protobuf"
    git config submodule.src/third_party/wil.url "${srcdir}/wil"
    git -c protocol.file.allow=always submodule update
}

build() {
    cd mozc-fcitx/src

    unset ANDROID_NDK_HOME
    unset ANDROID_HOME
    export JAVA_HOME='/usr/lib/jvm/java-21-openjdk/'

    bazel build unix/fcitx5:fcitx5-mozc.so unix/icons --config oss_linux --compilation_mode opt
}

package() {
    cd mozc-fcitx/src

    # BSD-3-Clause
    sed -n 1,29p unix/fcitx5/fcitx_key_translator.h > Fcitx5
    sed -i -e 's|^\/\/[ ]\?||g' Fcitx5
    install -Dm644 Fcitx5 "${pkgdir}"/usr/share/licenses/${pkgname}/Fcitx5
    # BSD-3-Clause
    sed -n 67,94p data/installer/credits_en.html > Mozc
    install -Dm644 Mozc "${pkgdir}"/usr/share/licenses/${pkgname}/Mozc
    # BSD-3-Clause
    sed -n 317,344p data/installer/credits_en.html > Breakpad
    install -Dm644 Breakpad "${pkgdir}"/usr/share/licenses/${pkgname}/Breakpad
    # NAIST-2003
    sed -n 355,424p data/installer/credits_en.html > IPAdic
    install -Dm644 IPAdic "${pkgdir}"/usr/share/licenses/${pkgname}/IPAdic
    # BSD-2-Clause
    sed -n 435,457p data/installer/credits_en.html > Japanese-Usage-Dictionary
    install -Dm644 Japanese-Usage-Dictionary "${pkgdir}"/usr/share/licenses/${pkgname}/Japanese-Usage-Dictionary
    # Public Domain Data
    sed -n 468,470p data/installer/credits_en.html > Okinawa-Dictionary
    install -Dm644 Okinawa-Dictionary "${pkgdir}"/usr/share/licenses/${pkgname}/Okinawa-Dictionary
    # BSD-3-Clause
    sed -n 481,513p data/installer/credits_en.html > Protocol-Buffers
    install -Dm644 Protocol-Buffers "${pkgdir}"/usr/share/licenses/${pkgname}/Protocol-Buffers
    # MIT
    sed -n 698,704p data/installer/credits_en.html > Tamachi-Phonetic-Kanji-Alphabet
    install -Dm644 Tamachi-Phonetic-Kanji-Alphabet "${pkgdir}"/usr/share/licenses/${pkgname}/Tamachi-Phonetic-Kanji-Alphabet
    # MIT
    sed -n 715,735p data/installer/credits_en.html > Windows-Implementation-Library
    sed -i -e 's|^[ \t]*||g' Windows-Implementation-Library
    install -Dm644 Windows-Implementation-Library "${pkgdir}"/usr/share/licenses/${pkgname}/Windows-Implementation-Library

    install -Dm755 bazel-bin/unix/fcitx5/fcitx5-mozc.so "${pkgdir}"/usr/lib/fcitx5/fcitx5-mozc.so
    install -Dm644 unix/fcitx5/mozc-addon.conf "${pkgdir}"/usr/share/fcitx5/addon/mozc.conf
    install -Dm644 unix/fcitx5/mozc.conf "${pkgdir}"/usr/share/fcitx5/inputmethod/mozc.conf

    for pofile in unix/fcitx5/po/*.po
    do
        filename=`basename ${pofile}`
        lang=${filename/.po/}
        mofile=${pofile/.po/.mo}
        msgfmt ${pofile} -o ${mofile}
        install -Dm644 ${mofile} "${pkgdir}"/usr/share/locale/${lang}/LC_MESSAGES/fcitx5-mozc.mo
    done

    msgfmt --xml -d unix/fcitx5/po/ --template unix/fcitx5/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml.in -o unix/fcitx5/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml
    install -Dm644 unix/fcitx5/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml "${pkgdir}"/usr/share/metainfo/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml

    cd bazel-bin/unix

    unzip -o icons.zip

    install -Dm644 mozc.png                                     "${pkgdir}"/usr/share/icons/hicolor/128x128/apps/org.fcitx.Fcitx5.fcitx_mozc.png
    install -Dm644 alpha_full.svg                               "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_alpha_full.svg
    install -Dm644 alpha_half.svg                               "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_alpha_half.svg
    install -Dm644 direct.svg                                   "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_direct.svg
    install -Dm644 hiragana.svg                                 "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_hiragana.svg
    install -Dm644 katakana_full.svg                            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_katakana_full.svg
    install -Dm644 katakana_half.svg                            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_katakana_half.svg
    install -Dm644 outlined/dictionary.svg                      "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_dictionary.svg
    install -Dm644 outlined/properties.svg                      "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_properties.svg
    install -Dm644 outlined/tool.svg                            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_tool.svg

    ln -s org.fcitx.Fcitx5.fcitx_mozc.png                       "${pkgdir}"/usr/share/icons/hicolor/128x128/apps/fcitx_mozc.png
    ln -s org.fcitx.Fcitx5.fcitx_mozc_alpha_full.svg            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_alpha_full.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_alpha_half.svg            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_alpha_half.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_direct.svg                "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_direct.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_hiragana.svg              "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_hiragana.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_katakana_full.svg         "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_katakana_full.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_katakana_half.svg         "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_katakana_half.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_dictionary.svg            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_dictionary.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_properties.svg            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_properties.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_tool.svg                  "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_tool.svg
}
