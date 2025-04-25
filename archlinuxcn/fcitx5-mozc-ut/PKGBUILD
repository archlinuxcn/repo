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

pkgname='fcitx5-mozc-ut'
pkgver=2.31.5810.102.20250425
pkgrel=1
pkgdesc='Fcitx5 module for Mozc (the Open Source edition of Google Japanese Input) bundled with the UT dictionary'
arch=('x86_64')
url='https://github.com/google/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND CC0-1.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-2.0-only AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('fcitx5' 'qt6-base')
makedepends=('bazel' 'git' 'python')
provides=('fcitx5-mozc=2.31.5810.102')
conflicts=('emacs-mozc' 'fcitx-mozc' 'fcitx5-mozc' 'ibus-mozc' 'mozc' 'mozc-ut')
options=(!distcc !ccache)
source=('git+https://github.com/fcitx/mozc.git#commit=5fa14f5f5836318ebf934190a53551f6f1f9a725'
        'git+https://github.com/abseil/abseil-cpp.git#commit=4447c7562e3bc702ade25105912dce503f0c4010'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=b514bdc898e2951020cbdca1304b75f5950d1f59'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=7cc670c1809e704ebeba90fb430d50e009f36727'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=98a124f9ce6b282531fe5ca1b0fb93a3763aa9db'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=bf26bcbb1846f2e9cf35cbfcafcc91c015a1fb22'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=663f3ad0fd4c2350b655aef994e320f0756d0e14'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=02af54077293d4721d3079df03616b54cc699cb6'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=e33ac4ce808fa4253c6c97bf5178e229a4bfb50f'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=db98bba0542cce073a609af468e949d26c39d3cf'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=5b3f01cd3ccf0e0aa9855c48b6587cbf6e13c94c'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=e5c5573cd35a62f779c391f0bb48fef79e63f384'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=170e3704f7927ba76619e869e7047ea7ed4c8d49'
        'https://dumps.wikimedia.org/jawiki/20250420/jawiki-20250420-pages-articles-multistream-index.txt.bz2')
sha256sums=('086f49231951f7c5f3a6db223cbbb895292efc6854ea666c3ed38e19269e393f'
            'e131bbdd4e207d6cc2930bca9db82d6da9e347175c1125d9d1f2e09a36652278'
            '5168bb8ea19e2f696eeecbdee991f28e496aea206a473fd7cb49b547f5d0c5af'
            'c081295f2c22705e07fc430e152a30b36f949a179075d47d3e12ff3109d43c6a'
            '8a136786407526c64686c3f9990d6416d62c7e2d474ef4a75ced337ecfc58cef'
            '10a13d356071f2b0c2b6dcab1d841fae451f6a2020ee9b901533533fc7ac3008'
            '578ead09a4a3fbf2f70b6af56e0b385ca136c79a4f4a62c777cb13e7a6f733f5'
            'abb86ac4d546c98d7d9a10fdeb1059d6e3395e892d5397fb03179361f37c98fe'
            'e3bb664660fc0d919759f5c3730ddf8edd9c8da9857980996d7f2dd9c331c3e9'
            '81ed16f6b59f64e08482ea7ab676913584d95ecac00255e981374f02df2188e9'
            'e7771bf0a0c94872ba60d5857c6a98c3089c5cf3cdfed5073266b4acd17c6d00'
            'b8492936c29fa9f4f5b9732640d505c83d318e82b0249a71640bf5d8ecc76e75'
            '2bb007c54db6bb70d1771bffaeb05217c0e768cb176b9343ec0a25e9756d9f67'
            '3908ee4e9e553ffe7f3449074847f05c89e4dcaea39c6f11b1180c87e9cc238e'
            'c4128d15511efde50a2b1ecccdd8bb28aca3b0e5d57cc494f8370c8d8d12c97e'
            'cef5015c77bfd25ac44468ba6850fffc99a907cb9fbbaf3e8f33b8ef91cf9c70'
            'dd18b4f8c15e4e69246ceb89937c130524e30bb2c5fda0bb6cacf1cbbe72234f'
            '8f846a480801f1b8f1441153dadfc80cd25fcdaba732594966729b82a3712233')

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
    sed -i -e "s|jawiki-[a-z0-9]\{6,8\}|${srcdir}/jawiki-20250420|g" merge_dictionaries.py

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

    bazel build server:mozc_server gui/tool:mozc_tool unix/fcitx5:fcitx5-mozc.so unix/icons --config oss_linux --compilation_mode opt
}

package() {
    cd mozc/src

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

    install -Dm755 bazel-bin/server/mozc_server "${pkgdir}"/usr/lib/mozc/mozc_server
    install -Dm755 bazel-bin/gui/tool/mozc_tool "${pkgdir}"/usr/lib/mozc/mozc_tool

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
