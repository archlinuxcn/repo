# Maintainer: Jiachen YANG <farseerfc@gmail.com>
_srcname=srcML
pkgname=srcml
pkgver=0.9.5
pkgrel=1
pkgdesc="commandline and library for srcML, an XML representation for source code"
arch=(x86_64)
url="https://www.srcml.org/"
license=('GPL')
depends=(libxml2 libxslt libarchive boost-libs curl openssl antlr2 python2)
makedepends=(cmake boost man2html docbook2x)
optdepends=()
source=("$pkgname-$pkgver.tar.gz::http://131.123.42.38/lmcrs/beta/srcML-src.tar.gz")
md5sums=('e5c4223f7556b57984b20d70606f50ab')

prepare() {
	cd "$_srcname-src"
	# add runantlr2 command
	sed -i "s|runantlr|runantlr runantlr2|" CMake/config.cmake

	# undefine TRUE and FALSE and NULLPTR
	sed -i "22a #undef TRUE" src/parser/bitset_bucket_sorter.hpp
	sed -i "22a #undef FALSE" src/parser/bitset_bucket_sorter.hpp
	sed -i "22a #undef NULLPTR" src/parser/bitset_bucket_sorter.hpp
	sed -i "23a #undef TRUE" src/libsrcml/srcml_types.hpp
	sed -i "23a #undef FALSE" src/libsrcml/srcml_types.hpp
	sed -i "23a #undef NULLPTR" src/libsrcml/srcml_types.hpp
	sed -i "186a #undef TRUE" src/parser/srcMLParser.g
	sed -i "186a #undef FALSE" src/parser/srcMLParser.g
	sed -i "186a #undef NULLPTR" src/parser/srcMLParser.g
	sed -i "130a #undef TRUE" src/parser/srcMLParser.g
	sed -i "130a #undef FALSE" src/parser/srcMLParser.g
	sed -i "130a #undef NULLPTR" src/parser/srcMLParser.g
	sed -i "123a #undef TRUE" src/parser/srcMLParser.g
	sed -i "123a #undef FALSE" src/parser/srcMLParser.g
	sed -i "123a #undef NULLPTR" src/parser/srcMLParser.g
	sed -i "29a #undef TRUE" src/parser/srcMLOutput.hpp
	sed -i "29a #undef FALSE" src/parser/srcMLOutput.hpp
	sed -i "29a #undef NULLPTR" src/parser/srcMLOutput.hpp
	sed -i "29a #undef TRUE" src/libsrcml/srcml_translator.hpp
	sed -i "29a #undef FALSE" src/libsrcml/srcml_translator.hpp
	sed -i "29a #undef NULLPTR" src/libsrcml/srcml_translator.hpp
	sed -i "54a #undef TRUE" src/libsrcml/srcml.h
	sed -i "54a #undef FALSE" src/libsrcml/srcml.h
	sed -i "54a #undef NULLPTR" src/libsrcml/srcml.h
	
	# fix syntax error of compare boost::option with int
	sed -i "s|if(archive->language != 0) {|if(archive->language) {|" src/libsrcml/srcml_reader_handler.hpp

	# adding link flags for "other" target
	sed -i "46d" src/CMakeLists.txt
	sed -i '46a set_target_properties(${LIB_NAME} PROPERTIES OUTPUT_NAME srcml LINK_FLAGS "${CMAKE_LD_FLAGS}")' src/CMakeLists.txt
	sed -i '46a set_target_properties(${LIB_NAME} PROPERTIES OUTPUT_NAME libsrcml LINK_FLAGS "${CMAKE_LD_FLAGS}")' src/CMakeLists.txt

	# changing install prefix
        sed -i 's|set(CMAKE_INSTALL_PREFIX "/usr/local")|set(CMAKE_INSTALL_PREFIX "/usr")|' CMake/install.cmake
}

build() {
	cd "$_srcname-src"
	mkdir build
	cd build
	export ANTLR_LIBRARY="/usr/lib/libantlr.a"
	cmake .. \
		-DCMAKE_INSTALL_PREFIX="/usr" 
	make
}

package() {
	cd "$_srcname-src"
	cd build
	make DESTDIR="$pkgdir/" install
}
