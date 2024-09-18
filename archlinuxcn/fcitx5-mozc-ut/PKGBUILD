# Maintainer: Nocifer <apmichalopoulos at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>

pkgname='fcitx5-mozc-ut'
pkgver=2.30.5595.102
pkgrel=1
pkgdesc='Mozc module for Fcitx5'
arch=('x86_64')
url='https://github.com/fcitx/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('fcitx5' 'mozc>=2.30.5595.102')
makedepends=('bazel' 'git' 'python' 'qt6-base')
optdepends=('fcitx5-configtool')
provides=('fcitx5-mozc=2.30.5595.102')
conflicts=('fcitx5-mozc')
options=(!distcc !ccache)
source=('mozc-fcitx::git+https://github.com/fcitx/mozc.git#commit=ce08bdfa567d1e1d7dd740f684c37344681a6b3d'
        'git+https://github.com/abseil/abseil-cpp.git#commit=4447c7562e3bc702ade25105912dce503f0c4010'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=b514bdc898e2951020cbdca1304b75f5950d1f59'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=7cc670c1809e704ebeba90fb430d50e009f36727'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d')
sha256sums=('e669aa16bf19939dcfaa86893d9bb662eb989c2f641e5b291daa1e3ccdf7c383'
            'e131bbdd4e207d6cc2930bca9db82d6da9e347175c1125d9d1f2e09a36652278'
            '5168bb8ea19e2f696eeecbdee991f28e496aea206a473fd7cb49b547f5d0c5af'
            'c081295f2c22705e07fc430e152a30b36f949a179075d47d3e12ff3109d43c6a'
            '8a136786407526c64686c3f9990d6416d62c7e2d474ef4a75ced337ecfc58cef'
            '10a13d356071f2b0c2b6dcab1d841fae451f6a2020ee9b901533533fc7ac3008'
            '578ead09a4a3fbf2f70b6af56e0b385ca136c79a4f4a62c777cb13e7a6f733f5'
            'abb86ac4d546c98d7d9a10fdeb1059d6e3395e892d5397fb03179361f37c98fe')

prepare() {
    cd mozc-fcitx/src

    git submodule init
    git config submodule.src/third_party/abseil-cpp.url "$srcdir/abseil-cpp"
    git config submodule.src/third_party/breakpad.url "$srcdir/breakpad"
    git config submodule.src/third_party/gtest.url "$srcdir/googletest"
    git config submodule.src/third_party/gyp.url "$srcdir/gyp"
    git config submodule.src/third_party/japanese_usage_dictionary.url "$srcdir/japanese-usage-dictionary"
    git config submodule.src/third_party/protobuf.url "$srcdir/protobuf"
    git config submodule.src/third_party/wil.url "$srcdir/wil"
    git -c protocol.file.allow=always submodule update
}

build() {
    cd mozc-fcitx/src

    unset ANDROID_NDK_HOME
    unset ANDROID_HOME
    export JAVA_HOME='/usr/lib/jvm/java-21-openjdk/'

    bazel build unix/fcitx5:fcitx5-mozc.so unix/icons --config oss_linux --compilation_mode opt --copt='-Wno-maybe-uninitialized' --host_copt='-Wno-maybe-uninitialized'
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
    sed -n 762,782p data/installer/credits_en.html > Windows-Implementation-Library
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
