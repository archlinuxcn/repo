# $Id: $
# Maintainer: Dmitry Bilunov <kmeaw@yandex-team.ru>

pkgname=clickhouse
pkgver=19.5.3.8
pkgrel=1
pkgdesc='An open-source column-oriented database management system that allows generating analytical data reports in real time'
arch=('i686' 'x86_64')
url='https://clickhouse.yandex/'
license=('Apache')
depends=('cppkafka-git' 'jemalloc-git' 'ncurses' 'readline' 'unixodbc' 'termcap' 'double-conversion' 'capnproto' 're2' 'gtest' 'gsasl' 'libxml2' 'llvm>=8' 'brotli' 'lld' 'clang' 'libdaemon' 'poco' 'snappy')
makedepends=('cmake' 'patchelf')
source=(https://github.com/yandex/ClickHouse/archive/v$pkgver-stable.tar.gz
	https://github.com/apache/arrow/archive/87ac6fd.tar.gz
        https://github.com/google/cctz/archive/4f9776a.tar.gz
        https://github.com/edenhill/librdkafka/archive/8695b9d.tar.gz
        https://github.com/mfontanini/cppkafka/archive/9b184d8.tar.gz
        https://github.com/lz4/lz4/archive/c10863b.tar.gz
        https://github.com/Dead2/zlib-ng/archive/9173b89.tar.gz
        https://github.com/ClickHouse-Extras/boost/archive/471ea20.tar.gz
        https://github.com/ClickHouse-Extras/ssl/archive/ba8de79.tar.gz
        https://github.com/aklomp/base64/archive/a27c565.tar.gz
        https://github.com/ClickHouse-Extras/libhdfs3/archive/e2131aa.tar.gz
        https://github.com/ClickHouse-Extras/protobuf/archive/1273537.tar.gz
        https://github.com/apache/thrift/archive/010ccf0.tar.gz
	https://github.com/ClickHouse-Extras/hyperscan/archive/05dab0e.tar.gz
	https://github.com/facebook/zstd/archive/2555975.tar.gz
        libunwind.patch)
md5sums=('9f9e710b10623453eee7d6be9b778ea8'
         '70cf5232e7053256dea81e7f7b0d1ebe'
         '5323f7ba2565a84a80a93edde95eb4fe'
         '211c6903a4179959f456055dbb054b05'
         'cc75288aa9af1ce714ed184e0f2caaae'
         '7b92f0554687e6a8949adc5c10aeff78'
         '8a7abcc6998e461605ecb2988ff93dfc'
         '8cfc42d6e90721e37e0806d6fb905b09'
         'bf1ee7e88660616c92592dd4c1036f61'
         'e98c6b94f39d6947c83eb554aeb618e2'
         'b84bdd5d5d8c75c2ff5573670e05eaa9'
         'd63e8036385a27113365a40eb6bfe75e'
         '305944814e6124a2b9c2e306fb02ac16'
         '2d17a2f38bd80d68f17ec529f887aa62'
         'aaa86ec9f379ef587cc53f7b96bcc0e7'
         'f3f60b75abf8d6f21de74db6e88e1e7b')
backup=('etc/clickhouse-client/config.xml' 'etc/clickhouse-server/config.xml' 'etc/clickhouse-server/users.xml')
install=$pkgname.install

prepare() {
  cd ClickHouse-$pkgver-stable
  sed -e 's/mysqlxx common\(.*\) \(\${Z_LIB}\)/mysqlxx \2 common\1/' -i libs/libmysqlxx/CMakeLists.txt
  patch -p1 < ../libunwind.patch
  mkdir -p contrib/arrow contrib/cctz contrib/librdkafka contrib/cppkafka contrib/lz4 contrib/base64 contrib/libhdfs3 contrib/protobuf contrib/thrift contrib/hyperscan contrib/zstd
  rm -rf contrib/{arrow,cctz,librdkafka,cppkafka,lz4,zlib-ng,boost,ssl,base64,libhdfs3,protobuf,thrift,hyperscan,zstd}/*
  mv ../arrow-87ac6fd*/* contrib/arrow/
  mv ../librdkafka-8695b9d*/* contrib/librdkafka/
  mv ../cppkafka-9b184d8*/* contrib/cppkafka/
  mv ../cctz-4f9776a*/* contrib/cctz/
  mv ../lz4-c10863b*/* contrib/lz4/
  mv ../zlib-ng-9173b89*/* contrib/zlib-ng/
  mv ../boost-471ea20*/* contrib/boost/
  mv ../ssl-ba8de79*/* contrib/ssl/
  mv ../base64-a27c565*/* contrib/base64/
  mv ../libhdfs3-e2131aa*/* contrib/libhdfs3/
  mv ../protobuf-1273537*/* contrib/protobuf/
  mv ../thrift-010ccf0*/* contrib/thrift/
  mv ../hyperscan-05dab0e*/* contrib/hyperscan/
  mv ../zstd-2555975*/* contrib/zstd/
  for dir in contrib/*/; do
    rmdir $dir &> /dev/null || true
  done
}

build() {
  cd ClickHouse-$pkgver-stable
  COMP=""
  if ! pacman -Q clang | grep '^clang 7'; then
    COMP="-D ENABLE_EMBEDDED_COMPILER=False"
  fi
  cmake -D CMAKE_BUILD_TYPE:STRING=Release -D USE_STATIC_LIBRARIES:BOOL=False -D SPLIT_SHARED_LIBRARIES:BOOL=True -D ENABLE_TESTS:BOOL=False -D UNBUNDLED:BOOL=False -D USE_INTERNAL_DOUBLE_CONVERSION_LIBRARY:BOOL=False -D USE_INTERNAL_CAPNP_LIBRARY:BOOL=False -D USE_INTERNAL_POCO_LIBRARY:BOOL=True -D USE_INTERNAL_RE2_LIBRARY:BOOL=False -D USE_INTERNAL_LIBGSASL_LIBRARY:BOOL=False -D USE_INTERNAL_GTEST_LIBRARY:BOOL=False -D USE_INTERNAL_LIBXML2_LIBRARY:BOOL=False -D USE_INTERNAL_LLVM_LIBRARY:BOOL=False -D USE_INTERNAL_BROTLI_LIBRARY:BOOL=False -D NO_WERROR=1 -D DOUBLE_CONVERSION_ROOT_DIR=/usr -D USE_INTERNAL_PARQUET_LIBRARY:BOOL=False -D USE_INTERNAL_ZSTD_LIBRARY:BOOL=False -D USE_INTERNAL_RDKAFKA_LIBRARY:BOOL=True -D USE_RDKAFKA:BOOL=True -D USE_INTERNAL_LZ4_LIBRARY:BOOL=True -D ENABLE_JEMALLOC:BOOL=True -D USE_INTERNAL_JEMALLOC_LIBRARY:BOOL=False -D USE_BASE64:BOOL=True -D USE_INTERNAL_HDFS3_LIBRARY:BOOL=True -D ENABLE_MYSQL:BOOL=True -D USE_INTERNAL_MYSQL_LIBRARY:BOOL=False -D USE_INTERNAL_DOUBLE_CONVERSION_LIBRARY:BOOL=False -D USE_INTERNAL_PROTOBUF_LIBRARY:BOOL=True -D USE_INTERNAL_PROTOBUF_LIBRARY:BOOL=True -D PARQUET_INCLUDE_DIR:STRING=/usr/include -D USE_INTERNAL_POCO_LIBRARY:BOOL=False $COMP .
  cmake --build . --target clickhouse
}

package() {
  cd ClickHouse-$pkgver-stable
  mkdir -p $pkgdir/etc/clickhouse-server/ $pkgdir/etc/clickhouse-client/
  mkdir -p $pkgdir/usr/bin/
  mkdir -p $pkgdir/usr/lib/systemd/system
  ln -s clickhouse-client $pkgdir/usr/bin/clickhouse-server
  cp dbms/programs/server/config.xml dbms/programs/server/users.xml $pkgdir/etc/clickhouse-server/
  cp dbms/programs/clickhouse $pkgdir/usr/bin/clickhouse-client
  patchelf --remove-rpath $pkgdir/usr/bin/clickhouse-client
  patchelf --replace-needed libz.so.1 libz-ng.so.1 $pkgdir/usr/bin/clickhouse-client
  cp dbms/programs/client/clickhouse-client.xml $pkgdir/etc/clickhouse-client/config.xml
  compiler="libclickhouse-compiler.so"
  if ! pacman -Q clang | grep '^clang 7'; then
    compiler=""
  fi
  for lib in libclickhouse{-{benchmark,{clien,forma,performance-tes}t,{co{mpresso,pie},obfuscato,serve}r,extract-from-config,local}-lib,{_{aggregat,tabl}e,}_functions,_{com{mon_{config,io,zookeeper},pression},dictionaries{,_embedded},parsers,storage{_kafka,s_system}}}.so $compiler; do
    libsrc=$(find dbms/ -name "$lib")
    libdst=$lib.$pkgver
    cp ${libsrc:?$lib not found} $pkgdir/usr/lib/$libdst
    patchelf --remove-rpath $pkgdir/usr/lib/$libdst
    patchelf --replace-needed $lib $lib.$pkgver $pkgdir/usr/bin/clickhouse-client
  done
  for lib in lib{b{ase64,oost_{{file,}system,program_options}_internal},c{ctz,ommon},daemon,{dbm,string_util}s,mysqlxx,pocoext}.so; do
    libsrc=$(find contrib/ libs/ dbms/ -name "$lib")
    libdst=libclickhouse-${lib#lib}.$pkgver
    cp ${libsrc:?$lib not found} $pkgdir/usr/lib/$libdst
    patchelf --remove-rpath $pkgdir/usr/lib/$libdst
    patchelf --replace-needed $lib $libdst $pkgdir/usr/bin/clickhouse-client
  done
  cp contrib/zlib-ng/libz.so.1 $pkgdir/usr/lib/libz-ng.so.1
  cp contrib/protobuf/cmake/libprotobuf.so.3.6.1 $pkgdir/usr/lib/libprotobuf.so.3.6.1
  sed -e 's:/opt/clickhouse:/var/lib/clickhouse:g' -i $pkgdir/etc/clickhouse-server/config.xml
  sed -e '/listen_host/s%::<%::1<%' -i $pkgdir/etc/clickhouse-server/config.xml
  cp debian/clickhouse-server.service $pkgdir/usr/lib/systemd/system
}

# vim:set ts=2 sw=2 et:
