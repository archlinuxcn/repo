# Maintainer: Nocifer <apmichalopoulos at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>

pkgname='fcitx5-mozc-ut'
pkgver=2.29.5400.102
pkgrel=3
pkgdesc='Mozc module for Fcitx5'
arch=('x86_64')
url='https://github.com/fcitx/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('fcitx5' 'mozc>=2.29.5400.102')
makedepends=('bazel' 'git' 'python' 'qt6-base')
optdepends=('fcitx5-configtool')
provides=('fcitx5-mozc=2.29.5400.102')
conflicts=('fcitx5-mozc')
options=(!distcc !ccache)
source=("${pkgname}-git::git+https://github.com/fcitx/mozc.git#commit=05fa21362019671046a7bd7c366b21123a7d0bde")
sha256sums=('SKIP')

prepare() {
    cd ${pkgname}-git/src

    git submodule update --init --recursive
}

build() {
    cd ${pkgname}-git/src

    unset ANDROID_NDK_HOME
    unset ANDROID_HOME
    export JAVA_HOME='/usr/lib/jvm/java-11-openjdk/'
    bazel build unix/fcitx5:fcitx5-mozc.so unix/icons --config oss_linux --compilation_mode opt
}

package() {
    cd ${pkgname}-git/src

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

    install -Dm644 bazel-bin/unix/fcitx5/fcitx5-mozc.so "${pkgdir}"/usr/lib/fcitx5/fcitx5-mozc.so
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

    install -Dm644 mozc.png                                     "${pkgdir}"/usr/share/icons/hicolor/128x128/apps/org.fcitx.Fcitx5.fcitx-mozc.png
    install -Dm644 alpha_full.svg                               "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-alpha-full.svg
    install -Dm644 alpha_half.svg                               "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-alpha-half.svg
    install -Dm644 direct.svg                                   "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-direct.svg
    install -Dm644 hiragana.svg                                 "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-hiragana.svg
    install -Dm644 katakana_full.svg                            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-katakana-full.svg
    install -Dm644 katakana_half.svg                            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-katakana-half.svg
    install -Dm644 outlined/dictionary.svg                      "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-dictionary.svg
    install -Dm644 outlined/properties.svg                      "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-properties.svg
    install -Dm644 outlined/tool.svg                            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx-mozc-tool.svg

    ln -s org.fcitx.Fcitx5.fcitx-mozc.png                       "${pkgdir}"/usr/share/icons/hicolor/128x128/apps/fcitx-mozc.png
    ln -s org.fcitx.Fcitx5.fcitx-mozc-alpha-full.svg            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-alpha-full.svg
    ln -s org.fcitx.Fcitx5.fcitx-mozc-alpha-half.svg            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-alpha-half.svg
    ln -s org.fcitx.Fcitx5.fcitx-mozc-direct.svg                "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-direct.svg
    ln -s org.fcitx.Fcitx5.fcitx-mozc-hiragana.svg              "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-hiragana.svg
    ln -s org.fcitx.Fcitx5.fcitx-mozc-katakana-full.svg         "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-katakana-full.svg
    ln -s org.fcitx.Fcitx5.fcitx-mozc-katakana-half.svg         "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-katakana-half.svg
    ln -s org.fcitx.Fcitx5.fcitx-mozc-dictionary.svg            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-dictionary.svg
    ln -s org.fcitx.Fcitx5.fcitx-mozc-properties.svg            "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-properties.svg
    ln -s org.fcitx.Fcitx5.fcitx-mozc-tool.svg                  "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx-mozc-tool.svg
}
