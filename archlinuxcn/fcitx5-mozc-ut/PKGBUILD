# Maintainer: Nocifer <apmichalopoulos at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>

pkgname=fcitx5-mozc-ut
pkgver=3.33.6089
pkgrel=1
pkgdesc='The Open Source edition of Google Japanese Input (Fcitx5 module)'
arch=('x86_64')
url='https://github.com/fcitx/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('fcitx5' 'mozc>=3.33.6089' 'qt6-base')
makedepends=('git' 'mold' 'python')
optdepends=('fcitx5-configtool')
provides=('fcitx5-mozc=3.33.6089')
conflicts=('fcitx5-mozc')
source=('mozc-fcitx::git+https://github.com/fcitx/mozc.git#commit=e99761585263feec635b26e0dea1025ae12b25b7'
        'git+https://github.com/abseil/abseil-cpp.git#commit=987c57f325f7fa8472fa84e1f885f7534d391b0d'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=52eb8108c5bdec04579160ae17225d66034bd723'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=4fbd1111a292d04746c732573025e3251de0bb9c'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        # Use a local copy of Bazel's module repo (https://bcr.bazel.build/)
        'git+https://github.com/bazelbuild/bazel-central-registry.git#commit=b340ca17233d8a3452184a0bf5f593000cdad9e4'
        # Prefetch Bazel 8.4.1
        'https://github.com/bazelbuild/bazel/releases/download/8.4.1/bazel-8.4.1-linux-x86_64'
        # Prefetch build dependencies
        'https://github.com/abseil/abseil-cpp/releases/download/20250814.0/abseil-cpp-20250814.0.tar.gz'
        'https://github.com/bazelbuild/apple_support/releases/download/1.23.1/apple_support.1.23.1.tar.gz'
        'https://github.com/bazel-contrib/bazel_features/releases/download/v1.30.0/bazel_features-v1.30.0.tar.gz'
        'https://github.com/bazelbuild/bazel-skylib/releases/download/1.8.1/bazel-skylib-1.8.1.tar.gz'
        'https://github.com/astral-sh/python-build-standalone/releases/download/20250610/cpython-3.11.13+20250610-x86_64-unknown-linux-gnu-install_only.tar.gz'
        'https://github.com/bazelbuild/platforms/releases/download/1.0.0/platforms-1.0.0.tar.gz'
        'https://github.com/protocolbuffers/protobuf/releases/download/v32.0/protobuf-32.0.zip'
        'https://github.com/bazelbuild/rules_android_ndk/releases/download/v0.1.3/rules_android_ndk-v0.1.3.tar.gz'
        'https://github.com/bazelbuild/rules_apple/releases/download/4.1.2/rules_apple.4.1.2.tar.gz'
        'https://github.com/bazelbuild/rules_cc/releases/download/0.2.2/rules_cc-0.2.2.tar.gz'
        'https://github.com/bazelbuild/rules_java/releases/download/8.14.0/rules_java-8.14.0.tar.gz'
        'https://github.com/bazelbuild/rules_kotlin/releases/download/v1.9.6/rules_kotlin-v1.9.6.tar.gz'
        'https://github.com/bazelbuild/rules_license/releases/download/1.0.0/rules_license-1.0.0.tar.gz'
        'https://github.com/bazelbuild/rules_pkg/releases/download/1.1.0/rules_pkg-1.1.0.tar.gz'
        'https://github.com/bazel-contrib/rules_python/releases/download/1.5.4/rules_python-1.5.4.tar.gz'
        'https://github.com/bazelbuild/rules_shell/releases/download/v0.3.0/rules_shell-v0.3.0.tar.gz'
        'https://github.com/bazelbuild/rules_swift/releases/download/3.1.2/rules_swift.3.1.2.tar.gz'
        'https://github.com/madler/zlib/releases/download/v1.3.1/zlib-1.3.1.tar.gz'
        'dictionary.png::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/png/action/chrome_reader_mode/materialiconsoutlined/48dp/1x/outline_chrome_reader_mode_black_48dp.png'
        'dictionary.svg::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/src/action/chrome_reader_mode/materialiconsoutlined/24px.svg'
        'properties.png::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/png/action/settings/materialiconsround/48dp/1x/round_settings_black_48dp.png'
        'properties.svg::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/src/action/settings/materialiconsround/24px.svg'
        'tool.png::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/png/action/build/materialicons/48dp/1x/baseline_build_black_48dp.png'
        'tool.svg::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/src/action/build/materialicons/24px.svg')
noextract=('abseil-cpp-20250814.0.tar.gz'
           'apple_support.1.23.1.tar.gz'
           'bazel_features-v1.30.0.tar.gz'
           'bazel-skylib-1.8.1.tar.gz'
           'cpython-3.11.13+20250610-x86_64-unknown-linux-gnu-install_only.tar.gz'
           'platforms-1.0.0.tar.gz'
           'protobuf-32.0.zip'
           'rules_android_ndk-v0.1.3.tar.gz'
           'rules_apple.4.1.2.tar.gz'
           'rules_cc-0.2.2.tar.gz'
           'rules_java-8.14.0.tar.gz'
           'rules_kotlin-v1.9.6.tar.gz'
           'rules_license-1.0.0.tar.gz'
           'rules_pkg-1.1.0.tar.gz'
           'rules_python-1.5.4.tar.gz'
           'rules_shell-v0.3.0.tar.gz'
           'rules_swift.3.1.2.tar.gz'
           'zlib-1.3.1.tar.gz')
b2sums=('cacc7ca4f8ba12d418295f25e828723113c1b0448226a28f3100451d3127efd9158ac4208c7cda75a421c095d8268a35804709920d313608dbb91e959f685804'
        'cccfb46ba1e756948036ffdca21187d5cd8c095357e45f305a88c96b32084ded297717e5c44cf34971bd2fe6e7ea37099dadf564aa775ef0a55a7fbab965270c'
        'eb54c87947561d6d985b3a244860a247a6ae41e5667ed6f4687dc864a3f02bc0b52d111c5b16025e06f44a1db31d7731c42eb38725521512b4c102475aebf585'
        'e8779958a717e8581a0952ea01728852d37b95713b9e92ce3fb4f5bf03e3fe02083c51daa042c231d708c2b775729000b7355f573069c09e1242bbd6f277145d'
        'a6de318769bc421794d46b207eceb92920c7610cf107249183b40801fec3b1b079d679565de05e6a24b9970623563d914a8a674c5481a498d9fecf5a23e214ca'
        '7abe2c678b7983fbc86b11b25e6f6f1dfc4dfe75b8db40510849ce8b06f415dc4932c16fa0bae213fa0a466d7a837363d0860024ac0e5bcb87f64dc23561c220'
        'ff6761953a4b1b23cece42e42287b9c5344b5c080819a4bfd53778f62148123ec487aa23585bc24de583f27ebf3c6ddf3dc72b098c0dfc76071acfdcfc152088'
        '8d105ce08ca103db180ec99c7845eee08d15abcc3e7cfce51d1b565a4ed5942be40aaefbc78e80e09e84c5583640d6a33feed7d3d9ec572c4a9ebf505ea6a7f5'
        'eb7c908642670c243f3ef1ac34c59029ab631c7ae8eaca3eb0850f68142d8f3e2f8d894896c12229aea320c92c0ed51bf9112e979a61f0c28f5fb6fd8623c02c'
        '50e67de8a5c63f41831a52d5429913185939d6194d0b50d475c554f04c4bc64b4d4ed5e9612a76b4f693d479a58b6e66f46b94f2b2557f24ab4d72c41e4b664c'
        'f60f3604215f64f33fad902637360050061ec62cfa6413cafc4cd3794a1898c7ee67f7b6edf78e5cb7c6b0ed86b8d80338ad4abee3f2664e391c2cfae5997220'
        'c8228fadf527ff4f091082bf71e3c5cf0859aa573b25927dad58c1531bef89334b05cff822d918ce459127c915e267c52448c3f4979812f1fe33f3b0cc6d180a'
        '725739189337b9a4a014d972c9a63ca89c6899ec8fb8773cb7fee1787e3a20042691d700a393d60362e009dd1e3f0fd7c26f6aa13f39b162a900b170ea8b86e6'
        'dd3b506ceb5e3a72636d9071f13e706f229a8012f9e97575f9dd51f1f3e766c64e7509039404c63570c9971592a19239ce2dab1b0db33c9403a404c141bb7d81'
        '8ea831fe64cb31eed977e1a1ff65d318e335c0cc7eddf8f0fffbe75ac349f417b137fd3b318795f7225de5009d915cfcbb6c855cb1d85be0c44fb48b08bc8d8e'
        'eaa82522a86d75669befeaa6023b46fb6c482cd9a0e818d5f99c602a2bf7e359e51ef61298aeda40cea15b7f281eba04cf9a37e637f92fc8c7b5d209693fd8e1'
        '86ecede4efa0116e81cd39421a7a630fae3f6393d08421ab329d8f466ea01a3b5b1c0117f0f4e6a3339619201847b8279e3d95cadd13a9d4d042d1e4c368ba02'
        'bfad0cd27fc9bc2971663a197300794aef7f330659500a69a95a89a0ccdbc547ff4e6760104a1398b3a9981a38facc6a64aeac7b1e55a27bcf44f4eafd19a63c'
        'e56aadd96ea72ef714ead6dca3b020def6f9b7756d713e601afc3ab44568f17d59597d3e74e73945f387a94a3250318c91eb036b28e257cdab7c36837bd134da'
        'a1bd0906d00dba875e2d0bb7ae79738d02e45f3c5276e464ba3434c28a39ed60c5421cfd3c7b34dfe1d7db7a0cd47b6b8a26c2140c4504cf39a11f1b17227410'
        'd643d827277d49df734457f89c13b591d55679bb404518fb240e0536cca79bad8d70de8e723966431e6a41a022b37fc5af4934d56d04b8c817cda50767782cbd'
        '1532ea7cc7807326c948be50cd4942a39f6c04f179690d9b51b41d354bde253581f453a2889048998e8bd381b8baad04315b81523e8cf2159ea33055704f43fb'
        '851db879f93a22fed62872fed37e32c8fe54d882c2d15e0df9f17f332d99c92345c7bd89dbb70a040e455d6033e23035a984a478fd1655a6573c35bd1b84300e'
        '272ada06effe826ce4eae590863423df9c550f97051c0a8b50fc90d2a323a4218359408e2e57f22d74d337457bb8ab1673f5382784652c546cadaac64eef9336'
        '81856a49c2da4d746658fa94524614a6ad5c755121ac00e23dc4c38c0ef9be0f1908226235a9b32578df059a1a4b4ffc32e361809bfe4c93b64797030b894562'
        'ed0740f1e3f637f70e7c2fc76727f54722b767e764dfc0048099b2a16de453e355a1596927461d5abb5d9f2131c12fbbe0bfe6606f3e44c42af8f23eb0454036'
        'fd8f66c6e2605596197fd0a06c6445545067949f30210fdafe5122eac7883e9d782121c5fbc38b9387d7aaa6fa955d4fd3aefb8479ff4071b619403179bd7dc1'
        '872ef9cc41ba57e9809ab5714ffa15cc9d3ef6c4a948c57107f800fc373bcfe2475136407203cb9aa33b189994336f36f2757b7a582e065ad477bfd49260184b'
        'f92fdeae34eff41473c6c9b0f6fb5a3c784b7b98fd6932b03953131f78ab97c961eb94f88e542f593acf0d2af176e28a3d638e50e912aa695de882477117b2d6'
        '24464c7238fc58056c4c9e94f72c9ece8313a09ef1fd57f07b2178dcf78b722fff4965d42ac867c135db969a905306f99e7d6e4f5c028029646b77d6eee3de33'
        '33a12b009e0dff7a46385a59287a8d179ec931e6cd98a5b13480ade870035259928d8655ca578954307a76eca92ea98dbe4ec4f904f2074c21c848b3a2b6f0d7'
        '17f3facef4594c38b94a3be325d7a00d5538c4f098853b5e70254b572305440adbba7e597cee4645ffd1884631cab5ff50dd25a5368b7aff1972290e6ceaab91'
        'e699107fb3d5d8fd202ea8f65908a63b2d9b8c5aa4eaeed0db15a5bc5eb4af4735814f20b8e641736b08fbee2691836a5d5e8b94b4b653aac836f8afa982b791'
        'df5947d23720f168d40403c00dc20e547ae30dd8f92c8448d5675fe28344903a65e139c4739c83fa64db9233b012ddcd3e5ad663d96417a8dcb4b83ba020d4ad')

prepare() {
    chmod u+x bazel-8.4.1-linux-x86_64

    cd mozc-fcitx/src

    git submodule init
    git config submodule.src/third_party/abseil-cpp.url                 "${srcdir}"/abseil-cpp
    git config submodule.src/third_party/breakpad.url                   "${srcdir}"/breakpad
    git config submodule.src/third_party/gtest.url                      "${srcdir}"/googletest
    git config submodule.src/third_party/gyp.url                        "${srcdir}"/gyp
    git config submodule.src/third_party/japanese_usage_dictionary.url  "${srcdir}"/japanese-usage-dictionary
    git config submodule.src/third_party/protobuf.url                   "${srcdir}"/protobuf
    git config submodule.src/third_party/wil.url                        "${srcdir}"/wil
    git -c protocol.file.allow=always submodule update

    # Mozc: BSD-3-Clause
    printf '1. Mozc\n\n' > MOZC_LICENSE
    sed -n 67,94p data/installer/credits_en.html >> MOZC_LICENSE
    printf '\n---\n\n' >> MOZC_LICENSE
    # Breakpad: BSD-3-Clause
    printf '2. Breakpad\n\n' >> MOZC_LICENSE
    sed -n 317,344p data/installer/credits_en.html >> MOZC_LICENSE
    printf '\n---\n\n' >> MOZC_LICENSE
    # IPAdic: NAIST-2003
    printf '3. IPAdic\n\n' >> MOZC_LICENSE
    sed -n 355,424p data/installer/credits_en.html >> MOZC_LICENSE
    printf '\n---\n\n' >> MOZC_LICENSE
    # Japanese Usage Dictionary: BSD-2-Clause
    printf '4. Japanese Usage Dictionary\n\n' >> MOZC_LICENSE
    sed -n 435,457p data/installer/credits_en.html >> MOZC_LICENSE
    printf '\n---\n\n' >> MOZC_LICENSE
    # Okinawa Dictionary: Public Domain Data
    printf '5. Okinawa Dictionary\n\n' >> MOZC_LICENSE
    sed -n 468,470p data/installer/credits_en.html >> MOZC_LICENSE
    printf '\n---\n\n' >> MOZC_LICENSE
    # Protobuf: BSD-3-Clause
    printf '6. Protobuf\n\n' >> MOZC_LICENSE
    sed -n 481,513p data/installer/credits_en.html >> MOZC_LICENSE
    printf '\n---\n\n' >> MOZC_LICENSE
    # Tamachi Phonetic Kanji Alphabet: MIT
    printf '7. Tamachi Phonetic Kanji Library\n\n' >> MOZC_LICENSE
    sed -n 698,704p data/installer/credits_en.html >> MOZC_LICENSE
    printf '\n---\n\n' >> MOZC_LICENSE
    # Fcitx: BSD-3-Clause
    printf '8. Fcitx\n\n' >> MOZC_LICENSE
    sed -n 1,29p unix/fcitx5/fcitx_key_translator.h >> MOZC_LICENSE
    sed -i -e 's|^\/\/[ ]\?||g' MOZC_LICENSE
}

build() {
    cd mozc-fcitx/src

    "${srcdir}"/bazel-8.4.1-linux-x86_64 build unix/fcitx5:fcitx5-mozc.so \
        --subcommands \
        --verbose_failures \
        --registry file://"${srcdir}"/bazel-central-registry \
        --distdir="${srcdir}" \
        --config oss_linux \
        --config stable_channel \
        --config release_build \
        --copt '-U_FORTIFY_SOURCE' \
        $(echo "${CFLAGS}"|xargs -n1 echo "--conlyopt") \
        $(echo "${CXXFLAGS}"|xargs -n1 echo "--cxxopt") \
        --linkopt '-fuse-ld=mold' \
        $(echo "${LDFLAGS}"|xargs -n1 echo "--linkopt") \
        --subcommands \
        --verbose_failures
}

package() {
    cd mozc-fcitx/src

    install -Dm755 bazel-bin/unix/fcitx5/fcitx5-mozc.so "${pkgdir}"/usr/lib/fcitx5/fcitx5-mozc.so
    install -Dm644 unix/fcitx5/mozc-addon.conf          "${pkgdir}"/usr/share/fcitx5/addon/mozc.conf
    install -Dm644 unix/fcitx5/mozc.conf                "${pkgdir}"/usr/share/fcitx5/inputmethod/mozc.conf

    install -Dm644 MOZC_LICENSE                         "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE

    for pofile in unix/fcitx5/po/*.po
    do
        filename=`basename "${pofile}"`
        lang="${filename/.po/}"
        mofile="${pofile/.po/.mo}"
        msgfmt "${pofile}" -o "${mofile}"
        install -Dm644 "${mofile}" "${pkgdir}"/usr/share/locale/"${lang}"/LC_MESSAGES/fcitx5-mozc.mo
    done

    msgfmt --xml -d unix/fcitx5/po/ --template unix/fcitx5/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml.in -o unix/fcitx5/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml
    install -Dm644 unix/fcitx5/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml "${pkgdir}"/usr/share/metainfo/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml

    install -Dm644 data/images/icon.svg                 "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc.svg
    install -Dm644 data/images/full_ascii.svg           "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_alpha_full.svg
    install -Dm644 data/images/half_ascii.svg           "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_alpha_half.svg
    install -Dm644 data/images/direct.svg               "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_direct.svg
    install -Dm644 data/images/hiragana.svg             "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_hiragana.svg
    install -Dm644 data/images/full_katakana.svg        "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_katakana_full.svg
    install -Dm644 data/images/half_katakana.svg        "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_katakana_half.svg
    install -Dm644 "${srcdir}"/dictionary.svg           "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_dictionary.svg
    install -Dm644 "${srcdir}"/properties.svg           "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_properties.svg
    install -Dm644 "${srcdir}"/tool.svg                 "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc_tool.svg

    ln -s org.fcitx.Fcitx5.fcitx_mozc.svg               "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_alpha_full.svg    "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_alpha_full.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_alpha_half.svg    "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_alpha_half.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_direct.svg        "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_direct.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_hiragana.svg      "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_hiragana.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_katakana_full.svg "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_katakana_full.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_katakana_half.svg "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_katakana_half.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_dictionary.svg    "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_dictionary.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_properties.svg    "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_properties.svg
    ln -s org.fcitx.Fcitx5.fcitx_mozc_tool.svg          "${pkgdir}"/usr/share/icons/hicolor/scalable/apps/fcitx_mozc_tool.svg
}
