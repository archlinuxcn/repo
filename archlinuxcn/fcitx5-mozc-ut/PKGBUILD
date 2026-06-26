# Maintainer: Nocifer <apmichalopoulos at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>

pkgname=fcitx5-mozc-ut
pkgver=3.34.6239
pkgrel=2
pkgdesc='The Open Source edition of Google Japanese Input (Fcitx5 module)'
arch=('x86_64')
url='https://github.com/fcitx/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('fcitx5' 'mozc>=3.34.6239' 'qt6-base')
makedepends=('git')
optdepends=('fcitx5-configtool: configuration applet')
provides=('fcitx5-mozc=3.34.6239' 'mozc-engine-module')
conflicts=('fcitx5-mozc')
source=('mozc-fcitx::git+https://github.com/fcitx/mozc.git#commit=35898ee6c4f7424ae73000bbd754510d7ab772d0'
        # Bazel module repo (copy of https://bcr.bazel.build/)
        'git+https://github.com/bazelbuild/bazel-central-registry.git#commit=b0cb0e8ec70689252e3b35f109ffa4a32329b900'
        # Bazel binary
        'https://github.com/bazelbuild/bazel/releases/download/9.0.2/bazel-9.0.2-linux-x86_64'
        # Bazel dependencies
        'https://github.com/abseil/abseil-cpp/releases/download/20260107.1/abseil-cpp-20260107.1.tar.gz'
        'https://github.com/bazelbuild/apple_support/releases/download/2.4.0/apple_support.2.4.0.tar.gz'
        'https://github.com/bats-core/bats-core/archive/v1.10.0.tar.gz'
        'https://github.com/bazel-contrib/bazel_features/releases/download/v1.42.1/bazel_features-v1.42.1.tar.gz'
        'https://github.com/bazel-contrib/bazel-lib/releases/download/v2.22.5/bazel-lib-v2.22.5.tar.gz'
        'https://github.com/bazel-contrib/bazel-lib/releases/download/v3.0.0/bazel-lib-v3.0.0.tar.gz'
        'https://github.com/bazelbuild/bazel-skylib/releases/download/1.9.0/bazel-skylib-1.9.0.tar.gz'
        'https://github.com/astral-sh/python-build-standalone/releases/download/20251031/cpython-3.11.14+20251031-x86_64-unknown-linux-gnu-install_only.tar.gz'
        'https://github.com/bazelbuild/platforms/releases/download/1.0.0/platforms-1.0.0.tar.gz'
        'https://github.com/protocolbuffers/protobuf/releases/download/v34.1/protobuf-34.1.bazel.tar.gz'
        'https://github.com/protocolbuffers/protobuf/releases/download/v34.1/protoc-34.1-linux-x86_64.zip'
        'https://github.com/bazelbuild/rules_android/releases/download/v0.7.1/rules_android-v0.7.1.tar.gz'
        'https://github.com/bazelbuild/rules_android_ndk/releases/download/v0.1.5/rules_android_ndk-v0.1.5.tar.gz'
        'https://github.com/bazelbuild/rules_apple/releases/download/4.5.2/rules_apple.4.5.2.tar.gz'
        'https://github.com/bazelbuild/rules_cc/releases/download/0.2.17/rules_cc-0.2.17.tar.gz'
        'https://github.com/bazel-contrib/rules_go/releases/download/v0.60.0/rules_go-v0.60.0.zip'
        'https://github.com/bazelbuild/rules_java/releases/download/9.3.0/rules_java-9.3.0.tar.gz'
        'https://github.com/bazelbuild/rules_kotlin/releases/download/v2.2.2/rules_kotlin-v2.2.2.tar.gz'
        'https://github.com/bazelbuild/rules_license/releases/download/1.0.0/rules_license-1.0.0.tar.gz'
        'https://github.com/bazelbuild/rules_pkg/releases/download/1.2.0/rules_pkg-1.2.0.tar.gz'
        'https://github.com/bazel-contrib/rules_python/releases/download/1.9.0/rules_python-1.9.0.tar.gz'
        'https://github.com/bazelbuild/rules_shell/releases/download/v0.6.1/rules_shell-v0.6.1.tar.gz'
        'https://github.com/bazelbuild/rules_swift/releases/download/3.5.0/rules_swift.3.5.0.tar.gz'
        'https://github.com/bazel-contrib/tar.bzl/releases/download/v0.5.1/tar.bzl-v0.5.1.tar.gz'
        'https://github.com/madler/zlib/releases/download/v1.3.1/zlib-1.3.1.tar.gz'
        # Mozc dependencies
        'dictionary.png::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/png/action/chrome_reader_mode/materialiconsoutlined/48dp/1x/outline_chrome_reader_mode_black_48dp.png'
        'dictionary.svg::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/src/action/chrome_reader_mode/materialiconsoutlined/24px.svg'
        'properties.png::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/png/action/settings/materialiconsround/48dp/1x/round_settings_black_48dp.png'
        'properties.svg::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/src/action/settings/materialiconsround/24px.svg'
        'tool.png::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/png/action/build/materialicons/48dp/1x/baseline_build_black_48dp.png'
        'tool.svg::https://raw.githubusercontent.com/google/material-design-icons/4.0.0/src/action/build/materialicons/24px.svg')
noextract=('bazel-9.0.2-linux-x86_64'
           'abseil-cpp-20260107.1.tar.gz'
           'apple_support.2.4.0.tar.gz'
           'v1.10.0.tar.gz'
           'bazel_features-v1.42.1.tar.gz'
           'bazel-lib-v2.22.5.tar.gz'
           'bazel-lib-v3.0.0.tar.gz'
           'bazel-skylib-1.9.0.tar.gz'
           'cpython-3.11.14+20251031-x86_64-unknown-linux-gnu-install_only.tar.gz'
           'platforms-1.0.0.tar.gz'
           'protobuf-34.1.bazel.tar.gz'
           'protoc-34.1-linux-x86_64.zip'
           'rules_android-v0.7.1.tar.gz'
           'rules_android_ndk-v0.1.5.tar.gz'
           'rules_apple.4.5.2.tar.gz'
           'rules_cc-0.2.17.tar.gz'
           'rules_go-v0.60.0.zip'
           'rules_java-9.3.0.tar.gz'
           'rules_kotlin-v2.2.2.tar.gz'
           'rules_license-1.0.0.tar.gz'
           'rules_pkg-1.2.0.tar.gz'
           'rules_python-1.9.0.tar.gz'
           'rules_shell-v0.6.1.tar.gz'
           'rules_swift.3.5.0.tar.gz'
           'tar.bzl-v0.5.1.tar.gz'
           'zlib-1.3.1.tar.gz')
b2sums=('907420f4311313e2c7621229f63878b97d47a3631efbbbceb62103024435c6bd6d7d2864ed5f8054bd37e03f6e21e0a02f1f41242304eb74b6d41d6e6e26d5e0'
        '0fa68a06d930796445f215ecb16a7dba7bf9cae1004318c766269fd403ba3a44bc46035672949fc3731cf9cf778630291a078fda98ef46dce1f1c27f08b02bbb'
        '83457d476468763e9e94ce6ea3ee7abf9ad123887e24c304067993922f0b4430786da797c27bf5b15acba57a30c5c7472fd0ff285089368b9b51ce085f33c254'
        '1c0814eefb6181a82437128c9d3c08dec0540c2353b8a317204c49b1510b311173897de4a737da6f0cc034bf1b23717dea54f0338e3794f6a56f7292f53937bc'
        '3b6fc965bc2b129fbf65308cfd0c64177fe6cb51ca1f1a96dcd99023e973ed8199a5f457849070b85eed2bfd9248d74a2280cb1dcf33103700483b3b8b499e7c'
        '4d9e07f4b3da1cfadfd0ecbe00d611bc9a6ff8a6b55dba58e8ba4647e10265564d0cd64eb82a2b3ba483bc307b909f25913416057dc54ba8224c92cbff39c70e'
        '28eb673ec695ab77ff067e20479edaba4d423b3f7f66dc00c1d30eee9a89ddc808aa1fa5e1167b679eb21ca4be941186171e79da24520d8391048b689aaac8ce'
        'a5c49f97b8dc10d5f599f1c297e13bfb519f9d9152a0b75b68acdbcf0e4a956f1090b8e5b7aed3bf05949a0103252087affc4bd340d931d956c6a921bd1d84e5'
        '5dc042786b3cd846203944f2c352cfbe5da1c097665c5b034ba2ff981cabc49d5ada53b0a26088b4a0974c535861493b7e66046285f1341a92add57d325624f3'
        '166cf54bab522359889ce857774bee15cad1e683a9859cafa2b7514684ea42c4ecba58d3a685de2fb3f90e86c707bb23d6c84a8ee1d8971176fc68486c09b546'
        'ae3b89c4502fd65fcb6af9472579990fc89d8d8f9683bf0e187e56ef83bdf995f6bbd6eeef46dc78cad532ad7901f888a9cadfd7b7ad7b3c256254f850c40e77'
        'eaa82522a86d75669befeaa6023b46fb6c482cd9a0e818d5f99c602a2bf7e359e51ef61298aeda40cea15b7f281eba04cf9a37e637f92fc8c7b5d209693fd8e1'
        'add9afe2bdaa6a5a251d031d8a1a3d93df84e0503a627a7a11320a2ef23202eadfa951222778fecd436cd3b22f0fe99b52a880c3085a0752ab43d4ee76898fe9'
        '4a718d42ffd14486365eb96f5da2e773101f567ffd8ddbe1ced6ccfde6ffc60e071e00c6e88fec4ef7a51a957346b07fb18c1bbc6ed61d7524b74856fdfab7b1'
        'b36375b7545af1e599eeb6ed6a03b6f63cae90e119cdebf5e84e09e732c5045c7630156e7a0620113aab4f99f551ac484f9c83635f7fbdb1ce59d87f56a55437'
        '170ccbb71f36b464b2abf66a2657d1a001dee2920a4b36615f3258f2b3a7d35ca1bf2cae984140f0474ba2501f11aa62b790cbae330ad60a814aa2981762349b'
        '2df18efe363b0b07aab701020a3cb836fe305293f2cede2827c72f9e63de7362ae68465130364fc2c48c248b27d4277102f88a55fb13bd701f0c36d69569518d'
        '92a5293228af9545e750a9b518fba7cbd5d0e5bfd42dadb55d128ffaa89c71f0aa73373ca43b60408300b3da26ddf1b0ba0b5a2be894e4b78a4b05f841256905'
        'bade7f719dbdf1d3b9e36e88421efb3f61e69a7bab7ea46bfc171c414b4bfaae8e45edf0e58157df69216d3e8601598ba2316a8432828d6e4d4e9f9ddc398a85'
        '87c79856289558fc28726f5f2a01ff166c9d6a78314f10c08af8a699c8c366830d886b777e11baf2e21942f0c41eadab4190e93f0196e939c48a02561b416ae6'
        'dec315b20d14d7257fb8bbbf5c1cd7b1943b0817a2ca9a0e2667f5bf22d8b81aba517f93d44bc4c7664dbbc638508c88454bc981ce4924ac56ea417d3e7a116a'
        '851db879f93a22fed62872fed37e32c8fe54d882c2d15e0df9f17f332d99c92345c7bd89dbb70a040e455d6033e23035a984a478fd1655a6573c35bd1b84300e'
        'e5e8ed95d17380e1b980e74db97c837aab8b79dca2e59694a99db5a2b8d49db500bb7487caf7052eaeccd8dc454acb3b292e704a705123ac94afb91f54020fd3'
        '69a5edd6923fc030b4b0c27bfa293e6b88d776c66d80b403ba0fa81765b671b7b76b9d12a2800030ebedd42f072bd56631b86bde65e87655931553dca3adf76a'
        '4daa2247f5e21acf2ede0502e3239481dbcad1d2cffeec3e5fbe7887e711d56f1cf681ccb371ebff2e4abdd2a9b54906d706e11f1cae1e9523466bfa5417f450'
        '0d91d9bf8461a7f0f6eaae6208c0aea10d7651cc8ef607403ba4894821f3c8ad28618ca25a0ad74c106a69db1212ae8c568de5a8a38fcc65057a62b6ce5afce6'
        '9cf34bd92efe7889582e2196a185ef7c95e0c82a9ffa5bd9402b34b84169e3de16108a852ce654bd5bab572e203d15078763e16e3793a3b56b9ec1be85dbf957'
        '872ef9cc41ba57e9809ab5714ffa15cc9d3ef6c4a948c57107f800fc373bcfe2475136407203cb9aa33b189994336f36f2757b7a582e065ad477bfd49260184b'
        'f92fdeae34eff41473c6c9b0f6fb5a3c784b7b98fd6932b03953131f78ab97c961eb94f88e542f593acf0d2af176e28a3d638e50e912aa695de882477117b2d6'
        '24464c7238fc58056c4c9e94f72c9ece8313a09ef1fd57f07b2178dcf78b722fff4965d42ac867c135db969a905306f99e7d6e4f5c028029646b77d6eee3de33'
        '33a12b009e0dff7a46385a59287a8d179ec931e6cd98a5b13480ade870035259928d8655ca578954307a76eca92ea98dbe4ec4f904f2074c21c848b3a2b6f0d7'
        '17f3facef4594c38b94a3be325d7a00d5538c4f098853b5e70254b572305440adbba7e597cee4645ffd1884631cab5ff50dd25a5368b7aff1972290e6ceaab91'
        'e699107fb3d5d8fd202ea8f65908a63b2d9b8c5aa4eaeed0db15a5bc5eb4af4735814f20b8e641736b08fbee2691836a5d5e8b94b4b653aac836f8afa982b791'
        'df5947d23720f168d40403c00dc20e547ae30dd8f92c8448d5675fe28344903a65e139c4739c83fa64db9233b012ddcd3e5ad663d96417a8dcb4b83ba020d4ad')

prepare() {
    chmod u+x bazel-9.0.2-linux-x86_64

    cd mozc-fcitx/src

    # Mozc: BSD-3-Clause
    printf '1. Mozc\n\n' > LICENSE
    sed -n 67,94p data/installer/credits_en.html >> LICENSE
    printf '\n---\n\n' >> LICENSE
    # IPAdic: NAIST-2003
    printf '2. IPAdic\n\n' >> LICENSE
    sed -n 317,386p data/installer/credits_en.html >> LICENSE
    printf '\n---\n\n' >> LICENSE
    # Japanese Usage Dictionary: BSD-2-Clause
    printf '3. Japanese Usage Dictionary\n\n' >> LICENSE
    sed -n 397,419p data/installer/credits_en.html >> LICENSE
    printf '\n---\n\n' >> LICENSE
    # Okinawa Dictionary: Public Domain Data
    printf '4. Okinawa Dictionary\n\n' >> LICENSE
    sed -n 430,432p data/installer/credits_en.html >> LICENSE
    printf '\n---\n\n' >> LICENSE
    # Protobuf: BSD-3-Clause
    printf '5. Protobuf\n\n' >> LICENSE
    sed -n 443,475p data/installer/credits_en.html >> LICENSE
    printf '\n---\n\n' >> LICENSE
    # Tamachi Phonetic Kanji Alphabet: MIT
    printf '6. Tamachi Phonetic Kanji Library\n\n' >> LICENSE
    sed -n 660,666p data/installer/credits_en.html >> LICENSE
    # Fcitx: BSD-3-Clause
    printf '7. Fcitx\n\n' >> LICENSE
    sed -n 1,29p unix/fcitx5/fcitx_key_translator.h >> LICENSE
    sed -i -e 's|^\/\/[ ]\?||g' LICENSE
}

build() {
    cd mozc-fcitx/src

    "${srcdir}"/bazel-9.0.2-linux-x86_64 build unix/fcitx5:fcitx5-mozc.so \
        --registry file://"${srcdir}"/bazel-central-registry \
        --distdir="${srcdir}" \
        --config stable_channel \
        --config release_build \
        --copt '-U_FORTIFY_SOURCE' \
        $(echo "${CFLAGS}" | xargs -n1 echo "--conlyopt") \
        $(echo "${CXXFLAGS}" | xargs -n1 echo "--cxxopt") \
        --features='-supports_start_end_lib' \
        --linkopt '-fuse-ld=bfd' \
        $(echo "${LDFLAGS}" | xargs -n1 echo "--linkopt") \
        --subcommands \
        --verbose_failures
}

package() {
    cd mozc-fcitx/src

    install -Dm755 bazel-bin/unix/fcitx5/fcitx5-mozc.so "${pkgdir}"/usr/lib/fcitx5/fcitx5-mozc.so
    install -Dm644 unix/fcitx5/mozc-addon.conf          "${pkgdir}"/usr/share/fcitx5/addon/mozc.conf
    install -Dm644 unix/fcitx5/mozc.conf                "${pkgdir}"/usr/share/fcitx5/inputmethod/mozc.conf

    install -Dm644 LICENSE                              "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE

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
