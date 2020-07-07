# Maintainer: Mikhail f. Shiryaev <mr dot felixoid at gmail dot com>
# shellcheck disable=SC2034
# shellcheck disable=SC2154

pkgname=clickhouse-static
pkgver=20.1.4.14
pkgrel=1
pkgdesc='An open-source column-oriented database management system that allows generating analytical data reports in real time. Static binary'
arch=('i686' 'x86_64')
url='https://clickhouse.yandex/'
license=('Apache')
makedepends=('cmake' 'python' 'ninja')
depends=('readline')
# To get contrib submodules properly run populate-sources.sh with the path to
#   ClickHouse git directory with checked out tag and updated submodules.
# e.g. ./populate-sources.sh ~/workdir/github/ClickHouse/ClickHouse

source=("ClickHouse-${pkgver}-stable.tar.gz::https://github.com/yandex/ClickHouse/archive/v$pkgver-stable.tar.gz"
    arrow.tgz::https://github.com/apache/arrow/archive/b789226cc.tar.gz
    aws-c-common.tgz::https://github.com/awslabs/aws-c-common/archive/736a82d.tar.gz
    aws-c-event-stream.tgz::https://github.com/awslabs/aws-c-event-stream/archive/3bc3366.tar.gz
    aws-checksums.tgz::https://github.com/awslabs/aws-checksums/archive/519d6d9.tar.gz
    aws.tgz::https://github.com/aws/aws-sdk-cpp/archive/45dd8552d3.tar.gz
    base64.tgz::https://github.com/powturbo/Turbo-Base64/archive/5257626.tar.gz
    boost.tgz::https://github.com/ClickHouse-Extras/boost/archive/830e51ed.tar.gz
    brotli.tgz::https://github.com/google/brotli/archive/5805f99.tar.gz
    capnproto.tgz::https://github.com/capnproto/capnproto/archive/a00ccd91.tar.gz
    cctz.tgz::https://github.com/google/cctz/archive/4f9776a.tar.gz
    cppkafka.tgz::https://github.com/ClickHouse-Extras/cppkafka/archive/9b184d8.tar.gz
    curl.tgz::https://github.com/curl/curl/archive/3b8bbbbd1.tar.gz
    double-conversion.tgz::https://github.com/google/double-conversion/archive/cf2f0f3.tar.gz
    fastops.tgz::https://github.com/ClickHouse-Extras/fastops/archive/88752a5.tar.gz
    flatbuffers.tgz::https://github.com/google/flatbuffers/archive/bf9eb67a.tar.gz
    googletest.tgz::https://github.com/google/googletest/archive/703bd9ca.tar.gz
    h3.tgz::https://github.com/uber/h3/archive/6cfd649.tar.gz
    hyperscan.tgz::https://github.com/ClickHouse-Extras/hyperscan/archive/3058c9c.tar.gz
    icudata.tgz::https://github.com/ClickHouse-Extras/icudata/archive/f020820.tar.gz
    icu.tgz::https://github.com/unicode-org/icu/archive/faa2f9f9e1.tar.gz
    jemalloc.tgz::https://github.com/jemalloc/jemalloc/archive/cd2931ad.tar.gz
    libc-headers.tgz::https://github.com/ClickHouse-Extras/libc-headers/archive/9676d26.tar.gz
    libcxxabi.tgz::https://github.com/ClickHouse-Extras/libcxxabi/archive/7aacd45.tar.gz
    libcxx.tgz::https://github.com/ClickHouse-Extras/libcxx/archive/a8c453300.tar.gz
    libgsasl.tgz::https://github.com/ClickHouse-Extras/libgsasl/archive/3b8948a.tar.gz
    libhdfs3.tgz::https://github.com/ClickHouse-Extras/libhdfs3/archive/e2131aa.tar.gz
    librdkafka.tgz::https://github.com/edenhill/librdkafka/archive/6160ec27.tar.gz
    libunwind.tgz::https://github.com/ClickHouse-Extras/libunwind/archive/68cffcb.tar.gz
    libxml2.tgz::https://github.com/GNOME/libxml2/archive/18890f47.tar.gz
    llvm.tgz::https://github.com/ClickHouse-Extras/llvm/archive/778c297.tar.gz
    lz4.tgz::https://github.com/lz4/lz4/archive/3d67671.tar.gz
    mariadb-connector-c.tgz::https://github.com/ClickHouse-Extras/mariadb-connector-c/archive/1801630.tar.gz
    openssl.tgz::https://github.com/ClickHouse-Extras/openssl/archive/c74e7895eb.tar.gz
    orc.tgz::https://github.com/apache/orc/archive/5981208e.tar.gz
    poco.tgz::https://github.com/ClickHouse-Extras/poco/archive/d805cf5ca.tar.gz
    protobuf.tgz::https://github.com/ClickHouse-Extras/protobuf/archive/d6a10dd.tar.gz
    rapidjson.tgz::https://github.com/Tencent/rapidjson/archive/01950eb7.tar.gz
    re2.tgz::https://github.com/google/re2/archive/7cf8b88.tar.gz
    ryu.tgz::https://github.com/ClickHouse-Extras/ryu/archive/5b4a853.tar.gz
    simdjson.tgz::https://github.com/lemire/simdjson/archive/6091631.tar.gz
    snappy.tgz::https://github.com/google/snappy/archive/3f194ac.tar.gz
    sparsehash-c11.tgz::https://github.com/sparsehash/sparsehash-c11/archive/cf0bffa.tar.gz
    thrift.tgz::https://github.com/apache/thrift/archive/010ccf0a.tar.gz
    unixodbc.tgz::https://github.com/ClickHouse-Extras/UnixODBC/archive/b0ad30f.tar.gz
    zlib-ng.tgz::https://github.com/ClickHouse-Extras/zlib-ng/archive/bba56a7.tar.gz
    zstd.tgz::https://github.com/facebook/zstd/archive/25559750.tar.gz
)
# sha256sum ClickHouse-*-stable.tar.gz *tgz | sed 's/  / # /'
sha256sums=(
6c652c30cd152369a3c62d1cc92013bc273db0c4f75245264e0956ef103a04fc # ClickHouse-20.1.4.14-stable.tar.gz
93ee4cfdfaa471fbb8b8b963f9179ba5a7a0b32e20e69cb15125b51fa08ec97a # arrow.tgz
06fd1dc5b3612c70ee507de9393bb6b0cd291f1de2940d3bd531f727a1d8bc2b # aws-c-common.tgz
d900dd46f03585af7af83ea31ec5fe0437a80bf07349be9b7590ad3cffa42327 # aws-c-event-stream.tgz
14b767ad1b315d5cec007757e6bd01b1eae0802a1a71b40b36e06016016e8b8d # aws-checksums.tgz
ed2d5a0ccfcfa5c29ef0c0be5e0895e4db6cb0407fd531ae9ea312132309d770 # aws.tgz
98abb29dc5dfa1a7f4bf1562da600fe4bb3d7f7a0f9d7329162dbfb458743ba3 # base64.tgz
18a057463753f377524d2223b38c32319a704f1f220b1fd307dabeceed6f3bd1 # boost.tgz
fe21f9191db985e3f95956576ac23096b0687e2d272ccb1300872eb4522c3024 # brotli.tgz
54d891645f39682dd6688aa3b3d88a6ef7944a7230e375055fbb9006b4608078 # capnproto.tgz
6c67a1c2c312c578281f8fa4034512904f6a23f0519bb67306165a8e3f2a6584 # cctz.tgz
2390e9f9bbd11a7e47d9fb0ceb65a50480f9dd71e10d4acbf1b404b09b8708a2 # cppkafka.tgz
651f4c5ca6412129b23c29298bfafa2ddcb47ed99970b1b14aeddcf001996172 # curl.tgz
546a1eb8ce6ab886c885a6f68e193142f09483c64a0f182e1a54f682af637b04 # double-conversion.tgz
90076d2436b59a5573a89df0f7fe1e84e3767e0e18eedb336b49da5ec23d893c # fastops.tgz
ba39f5cbd5fcc32912d8b139cf087e686beaae036a076c1542d8934425212305 # flatbuffers.tgz
d17b1b83a57b3933565a6d0616fe261107326d47de20288d0949ed038e1c342d # googletest.tgz
f66fdff8281e5a6fb8d42992369960e2ebdea17709049965cda0806f7b6c42f8 # h3.tgz
e686c68d0026b905bde9f5ddfb349fa509306621821ea60eb976b0eadf25dbfe # hyperscan.tgz
75c7d18b3836eb73d295e72956543b84932ecb0d07e71825c5e6ff622d31644d # icudata.tgz
bb3e4de08079db12a0a6b74b675dd2ce8f322b1446a8159e613224ea7b593b82 # icu.tgz
aa1523658d0b1dbebccdf3f0fabdf7add86f14758d846fa6ba797ee2469c45be # jemalloc.tgz
9adcbfac8f8f177ee9f0f2a2c11e9d71492a06aa85f4db7f301beb00fdbacd97 # libc-headers.tgz
31ae2c7c2f6fe21c1f823c2ff8a3f3de95c2cfbf4e239f8e9a483adc5571c118 # libcxxabi.tgz
87c40d0febece9e5c977134b82da811c600ac6d367d1cf9317b1615728b9d7bc # libcxx.tgz
c41328df4d1b79f9043ad86219320d12af18dedcacbe76aa6115f906c28c6381 # libgsasl.tgz
6744b54d9465db5bdc844a1ccd5e93fc35c804652978d304fd59772ef25ab18d # libhdfs3.tgz
6dd22b23e544c7c2f433e666701f7fa92636194111dccdbe90a54b69ce826e45 # librdkafka.tgz
4fbd4aea4060a2f5a200111a5586274b633fd936af50d0833fcd1dd0a2b704ce # libunwind.tgz
2c3d9a93e651b02fef59489e796546a16df9010288905e62598816eaa2c7eb33 # libxml2.tgz
0f6a6ffff22d34f38ecfac70e97a6779f6c65a1992232b642590e9f0ae6c9186 # llvm.tgz
69172eae97f3672233de339d902b23736d96566836540cc8150865605e8c2127 # lz4.tgz
3316dd42dc0c0d688fe3dbab840c84d157dcd04c9abbc563eb0c98c217a6cf59 # mariadb-connector-c.tgz
3ca3158fe1a9ecde3272a08e1f3dfbe488f6200f8df365746d659a07d25dfbe7 # openssl.tgz
3207d094a85a4b2fed16fd7fda8720449e83931010efe04104986bd1e0053e1c # orc.tgz
0b9460e437d155571d29c31f31530fdd566d2d7ef33426697bee940d07a58df5 # poco.tgz
78e97675bd56926a32c40e530a2fce20d4e25a291287c303bd903843cd71a12c # protobuf.tgz
fcbbd610196f3e4f550ebb3a6bb2359b56cab969a2dce65e33a1bc8504a38168 # rapidjson.tgz
2e1d268c4340fc86206756f265f5910608c6d8e07a3668a955191c486afb072b # re2.tgz
d2c596dad9e95adf7b6b0d5b55908a24df812b4d8ed0d62ac2a9645be8e67a77 # ryu.tgz
e1341709679b998d91efe29228821a25be2049fb6b08a85738ead162010d2303 # simdjson.tgz
5811308e224ae6a405c4f20356388df80a01513af20958e3568791c5444765a3 # snappy.tgz
cd154b2e72af81ddce7963eb7eb2f695c60711f436c1278130f9afd8e3ea1f0e # sparsehash-c11.tgz
ebf4c0ec59f84598953f6ad9fd274230c22fcc6c03916afd4e34186c5207546d # thrift.tgz
5560ff2c30c9e1c571df9a94ec11338075ff8812e729359adb0df8232010a52e # unixodbc.tgz
4336e3c58662364394df244262e6e8bd2722de7ce7fbf078354f752b5a6219da # zlib-ng.tgz
f9f3bb69c7d1cef48bb122b5a82da3d750583f76092f2ec478848da1bc77ca87 # zstd.tgz
)

provides=('clickhouse')
conflicts=('clickhouse')
install="${pkgname}.install"

prepare() {
  for contrib_tar in *.tgz; do
    local contrib=${contrib_tar/.tgz/}
    echo "Populate contrib/${contrib}"
    local contrib_src=$(tar tf "${contrib_tar}" --exclude='*/*' --exclude='./*/*')
    cp -al "${contrib_src}/." "ClickHouse-${pkgver}-stable/contrib/${contrib}"
  done
}

build() {
  cd ClickHouse-$pkgver-stable || exit
  cmake .
  cmake --build . --target clickhouse
}

package() {
  cd ClickHouse-$pkgver-stable || exit
  mkdir -p "${pkgdir}/etc/clickhouse-client"
  mkdir -p "${pkgdir}/etc/clickhouse-server"
  mkdir -p "${pkgdir}/usr/bin"
  mkdir -p "${pkgdir}/usr/lib/systemd/system"
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  cp LICENSE "${pkgdir}/usr/share/licenses/${pkgname}"
  cp dbms/programs/server/config.xml dbms/programs/server/users.xml "${pkgdir}/etc/clickhouse-server/"
  cp dbms/programs/client/clickhouse-client.xml "${pkgdir}/etc/clickhouse-client/config.xml"
  cp dbms/programs/clickhouse "${pkgdir}/usr/bin/"
  cp debian/clickhouse-server.service "${pkgdir}/usr/lib/systemd/system/"
  local ch_binaries
  ch_binaries=$(./dbms/programs/clickhouse 2>&1 | awk '/^clickhouse/ {print $2}')
  for bin in $ch_binaries; do
    ln -s clickhouse "${pkgdir}/usr/bin/clickhouse-${bin}"
  done
}
