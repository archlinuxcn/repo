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
pkgver=3.34.6239.20260626
pkgrel=1
pkgdesc='The Open Source edition of Google Japanese Input bundled with the UT dictionary'
arch=('x86_64')
url='https://github.com/google/mozc'
license=('Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CC-BY-2.5 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GFDL-1.3-only AND GPL-2.0-only AND GPL-2.0-or-later AND MIT AND NAIST-2003 AND Unicode-3.0 AND LicenseRef-Okinawa-Dictionary')
depends=('qt6-base')
makedepends=('git' 'python')
optdepends=('fcitx5-mozc-ut: Fcitx5 integration'
            'ibus-mozc: IBus integration'
            'emacs-mozc: Emacs integration')
provides=('mozc=3.34.6239')
conflicts=('mozc')
source=('git+https://github.com/google/mozc.git#commit=76887c679e1e4f156102e4bc62ea9cf9174678a3'
        # UT dictionary
        'git+https://github.com/utuhiro78/merge-ut-dictionaries.git#commit=15c1c64502b43e31d328012860376c03c3eaf633'
        'git+https://github.com/utuhiro78/mozcdic-ut-alt-cannadic.git#commit=08e033f4558b7a0b03d8ad6920216d9473f15627'
        'git+https://github.com/utuhiro78/mozcdic-ut-edict2.git#commit=d7279ba285fd5ddfe158b0bfd0c4fcda1f7b08c3'
        'git+https://github.com/utuhiro78/mozcdic-ut-jawiki.git#commit=b50cabaecaf32c03d102db55fc5d0b98e334ec9e'
        'git+https://github.com/utuhiro78/mozcdic-ut-neologd.git#commit=d8307abf02b830b185c9320822cffa0d0787c54e'
        'git+https://github.com/utuhiro78/mozcdic-ut-personal-names.git#commit=5896ebef5f39d5772f4575fa05eb24436ce5a5f1'
        'git+https://github.com/utuhiro78/mozcdic-ut-place-names.git#commit=6f9d9bda14f0bd2c10c1563d2aed9150ea95095c'
        'git+https://github.com/utuhiro78/mozcdic-ut-skk-jisyo.git#commit=7c02e535bd6d999a715a53b58c3366f2401bfb7f'
        'git+https://github.com/utuhiro78/mozcdic-ut-sudachidict.git#commit=7def3da408b1854801bd5b559273f9fb8001ef5b'
        'https://dumps.wikimedia.org/jawiki/20260601/jawiki-20260601-pages-articles-multistream-index.txt.bz2'
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
        'https://github.com/hiroyuki-komatsu/japanese-usage-dictionary/archive/refs/tags/2025-01-25.zip'
        'https://github.com/hiroyuki-komatsu/japanpost_zipcode/raw/621d059fbcbfae17bfca15b439692bae934268c3/jigyosyo.zip'
        'https://github.com/hiroyuki-komatsu/japanpost_zipcode/raw/621d059fbcbfae17bfca15b439692bae934268c3/ken_all.zip')
noextract=('jawiki-20260601-pages-articles-multistream-index.txt.bz2'
           'bazel-9.0.2-linux-x86_64'
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
           'zlib-1.3.1.tar.gz'
           '2025-01-25.zip'
           'jigyosyo.zip'
           'ken_all.zip')
b2sums=('f55e3633cf0e688d9bbb4701b3bdefdd62b857ddf0866fcba525c3ab6c4666f338d17f59438b3f8121a63d5a294968fbddade4a4a8f850041ea8ad6882120cea'
        '84150b8d743335d4b2801d15b74640380da0cfb95815bfc32a98f48f0fc7ac25b98ab417afee715c87a70dd8127568bd999e8e6a2c17da09d2a560fcdba030d3'
        'f320adaf559ad3b51cb323c19f1ac0155f33f1b59939bfc34577f429cfc64d589271c5b6a9fe481fa7be6b97e7043832b0b7bf339e0559a836fa5a1b62101f5d'
        'e9555a886657f237a55552f8f8aec769f0522cb54b4765f805ec1cd06dc80d8e8f735c35099132471bb46bda8219cf2991f6357b2cca5df24ff38f63c5d8f331'
        '55a45669af70fa125127f27298f161180e7e6c4869611f6dc7a89416f0e82ed99453bdf87f674f5cd860acd174ab0ee14d3551d02fc1c2aa6ee8c38abb993a92'
        '2eca0fd11c44091b2cf0a59de232a8d9b30e6c0a16cb4ece11d8a9f54457fe14b7ec9dd58aa1e67828df113d83a46b077a80b683333dc23a28617fbb3fe13fd0'
        '83746b7d3b3cfe66e5f3b931abaf907fd37071a003d22e4d0cb065f91f554f33533104ed3b4dbe58840cdcb438dfa69882ea099fcfbfd0e8df0cf28417ae60a7'
        'a93db79ae5e75ede45217f6a3feaf2982f2c948dfe4a0695854339f6baceda1358bf98f6118c4b7291fe2a11670e4e0e4c4164328fa03e9bad6aa7fd20bf54a5'
        '1add7e57200df1899f48e0a0ba03351523c121eee95068aa7e332c3a3967089d78c4146ffd4528f0513b2228fbd2cfb72661b41427a6e3330b275edb83e23bbd'
        '602388543678e45d4703e6165d718265a2a9e1a6f4c5359aa090ccd6eaa901d2f329da72814fc0064e9b08b936f70a0291d29da09b5d1ef68aa272058f589d44'
        'cd4c02ee67d98084b6e4909eea77ca464d3cca838595538c5219710927aa42630fa67110f45297252c11f8e8c84d5a3c346a378b848d86ca14b4eb84505c1f74'
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
        '8a0813fa8a6b179be96894e011635e905b876cd4e54917fcb00b12b81f3f7463392a2f37c6c58279fddc6681c5df95bd2f7eb266f02557537f22705002050091'
        'bf9d30d8a985f4dfcce44f4d8424781c3f9d4ca18618167208c9a005712ead336ecab6b353fe98e96de495edae1e9dd323d303294aeaf63425e722e697d91165'
        '0f29f7e23c64db10ee8622197e5474c5842cb47dd61ab81b70ddf5559d33e154f761a5f60e63a40949822713f7de609aadf7ca8b6f26d87d7f7e42a6de2264cd')

prepare() {
    chmod u+x bazel-9.0.2-linux-x86_64

    cd mozc/src

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

    cd "${srcdir}"/merge-ut-dictionaries/src/merge/

    # Use fixed local snapshots for the Mozc repo and the jawiki dump data
    sed -i -e "s|mozc-master/src/data/dictionary_oss|${srcdir}/mozc/src/data/dictionary_oss|g ;
               84s|ZipFile(f'mozc-{date_str}\.zip') as zip_ref|open('merge_dictionaries\.py') as dummy_ref| ;
               86s|zip_ref\.|| ;
               96s|zip_ref\.namelist()|os\.listdir(path='${srcdir}/mozc/src/data/dictionary_oss')| ;
               104s|zip_ref\.|| ;
               169s|jawiki_index_file = .*|jawiki_index_file = '${srcdir}/jawiki-20260601-pages-articles-multistream-index.txt.bz2'| ;
               152,168d;89,90d;80,83d;67,79d ;
               7i import os" merge_dictionaries.py

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

    "${srcdir}"/bazel-9.0.2-linux-x86_64 build server:mozc_server gui/tool:mozc_tool \
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
    cd mozc/src

    install -Dm755 -t "${pkgdir}"/usr/lib/mozc bazel-bin/server/mozc_server
    install -Dm755 -t "${pkgdir}"/usr/lib/mozc bazel-bin/gui/tool/mozc_tool

    install -Dm644 -t "${pkgdir}"/usr/share/licenses/mozc-ut LICENSE
}
