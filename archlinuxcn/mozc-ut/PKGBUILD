# Maintainer: Nocifer <apmichalopoulos at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>

#NOTE: The UT dictionary's project homepage is at https://utuhiro78.github.io/linuxplayers/mozc-ut.html

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

pkgname=mozc-ut
pkgver=3.33.6089.20260213
pkgrel=1
pkgdesc='The Open Source edition of Google Japanese Input bundled with the UT dictionary'
arch=('x86_64')
url='https://github.com/google/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CC-BY-2.5 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GFDL-1.3-only AND GPL-2.0-only AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('qt6-base')
makedepends=('git' 'mold' 'python')
optdepends=('fcitx5-mozc-ut: Fcitx5 integration'
            'ibus-mozc: IBus integration'
            'emacs-mozc: Emacs integration')
provides=('mozc=3.33.6089')
source=('git+https://github.com/google/mozc.git#commit=a99841e37b7459d08e5736c3613a6bcd393c9e92'
        'git+https://github.com/abseil/abseil-cpp.git#commit=987c57f325f7fa8472fa84e1f885f7534d391b0d'
        'git+https://github.com/google/breakpad.git#commit=216cea7bca53fa441a3ee0d0f5fd339a3a894224'
        'git+https://github.com/google/googletest.git#commit=52eb8108c5bdec04579160ae17225d66034bd723'
        'git+https://github.com/chromium/gyp.git#commit=9ecf45e37677743503342ee4c6a76eaee80e4a7f'
        'git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=e5b3425575734c323e1d947009dd74709437b684'
        'git+https://github.com/protocolbuffers/protobuf.git#commit=4fbd1111a292d04746c732573025e3251de0bb9c'
        'git+https://github.com/microsoft/wil.git#commit=fc5dbf55989fe20351c71d038a8d12de4b397a6d'
        # UT dictionary
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=9c30e6648ccf459ef364529f21b029932ac6c455'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=69d40eed4e9cf016384d9629920fefa199116ea2'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=5e2db4eccab42652ae29e798b267c0f50f101128'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=f7ad6d689be3c5dc33bef6ae1620bb618a0f12fc'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=e33ac4ce808fa4253c6c97bf5178e229a4bfb50f'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=a2e43ea4d2c93ef8730a73df503c046a465294d3'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=3c054fa8e849f6da5b76ec99f8fc28d555ef5c63'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=384ad926e306d5308839c6dedb63696f11703968'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=6c8307cb6c8a935707fd7c39f5d116300e7b8d87'
        'https://dumps.wikimedia.org/jawiki/20260201/jawiki-20260201-pages-articles-multistream-index.txt.bz2'
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
        'https://github.com/hiroyuki-komatsu/japanese-usage-dictionary/archive/refs/tags/2025-01-25.zip'
        'https://github.com/hiroyuki-komatsu/japanpost_zipcode/raw/33524763837473258e7ba2f14b17fc3a70519831/jigyosyo.zip'
        'https://github.com/hiroyuki-komatsu/japanpost_zipcode/raw/33524763837473258e7ba2f14b17fc3a70519831/ken_all.zip')
noextract=('jawiki-20260201-pages-articles-multistream-index.txt.bz2'
           'abseil-cpp-20250814.0.tar.gz'
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
           'zlib-1.3.1.tar.gz'
           '2025-01-25.zip'
           'jigyosyo.zip'
           'ken_all.zip')
b2sums=('374862cb26ac2e866c6bce13e4dc43cd061f4bf641a03745a832240e38fa9557458451edb665d163c29f241dbe7c8a4ad83ba77ffe925d18e165ab180ee1c7ac'
        'cccfb46ba1e756948036ffdca21187d5cd8c095357e45f305a88c96b32084ded297717e5c44cf34971bd2fe6e7ea37099dadf564aa775ef0a55a7fbab965270c'
        'eb54c87947561d6d985b3a244860a247a6ae41e5667ed6f4687dc864a3f02bc0b52d111c5b16025e06f44a1db31d7731c42eb38725521512b4c102475aebf585'
        'e8779958a717e8581a0952ea01728852d37b95713b9e92ce3fb4f5bf03e3fe02083c51daa042c231d708c2b775729000b7355f573069c09e1242bbd6f277145d'
        'a6de318769bc421794d46b207eceb92920c7610cf107249183b40801fec3b1b079d679565de05e6a24b9970623563d914a8a674c5481a498d9fecf5a23e214ca'
        '7abe2c678b7983fbc86b11b25e6f6f1dfc4dfe75b8db40510849ce8b06f415dc4932c16fa0bae213fa0a466d7a837363d0860024ac0e5bcb87f64dc23561c220'
        'ff6761953a4b1b23cece42e42287b9c5344b5c080819a4bfd53778f62148123ec487aa23585bc24de583f27ebf3c6ddf3dc72b098c0dfc76071acfdcfc152088'
        '8d105ce08ca103db180ec99c7845eee08d15abcc3e7cfce51d1b565a4ed5942be40aaefbc78e80e09e84c5583640d6a33feed7d3d9ec572c4a9ebf505ea6a7f5'
        '33ebf652dd279f3fe3158f45a2aaf6acfc3d57bc5508b007165496dd5c0ad19f034def1318db487e2f7135c9e62c2a2d7f6ea167c5ee0d678bd188448bbbf791'
        'f585f3d3463e01669eea5568198cd9bf49492a0a1f5fc3afa7ce3fc2ce744ce02e4fe970cc2ab9b40fa287569c66ed8fb8fec6f580042c2fb76850e3cd93da6c'
        'c4399dac69c80bab116fd9ffd680b930b5211e3dab6be1f4cc240fb5d2a4b16acb611a6f0ae1c283a594d5bde61163692a46d9db442f33395fce92b34d9b1ef4'
        '092bf2517d1f8b6b6c9b4778ec76ec0334f042a04e16ec4ed717629a4e7a7aef5849699eebc59d4c22c00002d2301445b777be8ca9762cbe6c90158c2bbbd65f'
        'b2a8a919973d1a74e18b69adf7753cf0cacfa038b3c97bb37c57f6ff0749092e323befd56ae58a3eea637cefe2a3f55280f391d25fd4639dbca3ede2e8472f44'
        '27eec1206090428bef1bf810f2734bdbac9b546d43a85348f0631dc27aabb9a8d820f45c049c5392e8136bc9744bc88f130ea969433a9c2d416103de7b7def53'
        '241db1aec847f49dae19ba51e2239e92b6aec32756b52e0933600743c41aeac2ae0a3e62b0ca31294fcd743481b0e5b862e535422802c802b91bb66844bcef0e'
        '3c63f51241bd659e5841f26b11620ce755663aafe2a7c750738bb840df2e50de6b033f6cbf43e8a74258b1d07e86f1487b4caf1954e99354ce8f526ab469623a'
        'afe2917e93aa170b60fe7d6a2d71a43b233b9774f0ab26a291c384766da76aa3bd9c987a8b27b8385bbb05bd1f5b973f0380fa55ddc404b29553564724e1ad23'
        '51ef710b3dadd11cabeacc5a19d4d4a0ad5eb28576c5a9b888c8051a9df3a68353609b3f05db57c81bdc01cbe91ef918b4e0830de8156bc05ce08755ffdb4cdc'
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
        '8a0813fa8a6b179be96894e011635e905b876cd4e54917fcb00b12b81f3f7463392a2f37c6c58279fddc6681c5df95bd2f7eb266f02557537f22705002050091'
        '46cb54e9d9ee183031dbda9cecbbcf24a341488a0320286f264fb2f9e44638373f432463bbfd2fadaa65f64dba9afce9ca4ae01b8315f3853dcf6b8361e1339d'
        '03879037406a9d95c33d14bbde6fdd33acae0e6fda328e960c9f10aad74f2f34353d8b03e98ea247659587821d839783be2f031c3e756eac292ec52094c7ede6')

prepare() {
    chmod u+x bazel-8.4.1-linux-x86_64

    cd mozc/src

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

    cd "${srcdir}"/merge-ut-dictionaries/src/merge/

    # Use a dated snapshot for the jawiki dump data
    sed -i -e '124,127d' merge_dictionaries.py
    sed -i -e "s|jawiki-[a-z0-9]\{6,8\}|${srcdir}/jawiki-20260201|g" merge_dictionaries.py

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

    "${srcdir}"/bazel-8.4.1-linux-x86_64 build server:mozc_server gui/tool:mozc_tool \
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
    cd mozc/src

    install -Dm755 bazel-bin/server/mozc_server     "${pkgdir}"/usr/lib/mozc/mozc_server
    install -Dm755 bazel-bin/gui/tool/mozc_tool     "${pkgdir}"/usr/lib/mozc/mozc_tool

    install -Dm644 MOZC_LICENSE                     "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE
}
