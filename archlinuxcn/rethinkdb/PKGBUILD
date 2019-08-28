# Maintainer: Anatol Pomozov <anatol.pomozov@gmail.com>
# Contributor: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# Contributor: Sigmund Lahn <sigmund@lahn.no>

pkgname=rethinkdb
pkgver=2.3.6
_tag=rethinkdb-$pkgver
pkgrel=5
pkgdesc='Distributed powerful and scalable NoSQL database'
arch=(x86_64)
url='https://www.rethinkdb.com/'
license=(APACHE)
depends=(protobuf ncurses curl openssl-1.0)
makedepends=(boost python2 wget)
backup=(etc/rethinkdb/instances.d/default.conf)
install=rethinkdb.install
options=(!emptydirs)
source=(
  https://download.rethinkdb.com/dist/$_tag.tgz
  https://download.rethinkdb.com/dist/$_tag.tgz.asc
  rethinkdb-tmpfile.conf
  rethinkdb.service
  rethinkdb.sysusers
  mksnapshot_crash_fix.patch::https://github.com/rethinkdb/rethinkdb/commit/871bd3705a1f29c4ab07a096d562a4b06231a97c.patch
)
sha512sums=('653177750f7439fa1d61a121e488d578be1eab90f87c7d17ad52b9793d8543f22bbe98f8d501c2ab2d7048c65118096430fe7bde945d87c7a3228905af801af2'
            'SKIP'
            '5996f72b8e08aac80285373e8e1b5a664177e9d0e8d13e5638c6b821fe5b7a0368001fbfa9ef3f6709dabf0616abcabea40adc4808d176572f8f99b7a3255bae'
            '95e352cb941ea37b1dc3ddf4c8eaf0c8ef80b32e7a3cccf0e6fdefb92f0af83cfa47e3e6354d0397d7dc63c3c3cd87a8cb600f7b970c20fa6a65b832be219650'
            '974eda083410f400766833588e775c6f054fa16fd31ca80328dcacd985969db2aadfe71ad6cb91ffac89992de7efe94d90f0b3e960e9ccf4858ac962df663236'
            'f49bc92ecdd6d93bf89bd816268569f839daf0b289c44b7bede195b26ef53c2efd4ab6fb03ef0086d0a9e347210cd385755eff7e44b50d304a400d513addd5bf')
validpgpkeys=('3B87619DF812A63A8C1005C30742918E5C8DA04A') # RethinkDB Packaging <packaging@rethinkdb.com>

prepare() {
  cd $_tag

  # fix for https://github.com/rethinkdb/rethinkdb/issues/5757
  patch -p1 < ../mksnapshot_crash_fix.patch

  sed \
    -e 's|#!/usr/bin/python|#!/usr/bin/python2|' \
    -e 's|#!/usr/bin/env python|#!/usr/bin/env python2|' \
    -i scripts/*.py external/v8_*/tools/*.py
  sed -e 's|exec python|exec python2|g' -i external/v8_*/build/gyp/gyp
  sed -e 's|\bpython\b|python2|g' -i external/v8_*/{Makefile,*/*.gyp,*/*.gypi,*/*/*.gyp}

}

build() {
  cd $_tag
  export PYTHON=/usr/bin/python2
  CXX=g++-5 ./configure --fetch v8 --fetch jemalloc --dynamic all --enable-precompiled-web --prefix=/usr --sysconfdir=/etc --localstatedir=/var CXXFLAGS="$CXXFLAGS -I/usr/include/openssl-1.0" LDFLAGS="$LDFLAGS -L/usr/lib/openssl-1.0"
  make ALLOW_WARNINGS=1
}

check() {
  cd $_tag

  # these tests are flaky and extremely slow in Arch chroot
  # make build/release/rethinkdb-unittest
  # ./build/release/rethinkdb-unittest --gtest_filter=-RDBBtree.*:RDBInterrupt.*
  # some tests might be flaky on btrfs filesystem
}

package() {
  cd $_tag
  make DESTDIR="$pkgdir" install

  install -Dm644 "$srcdir"/rethinkdb.sysusers "$pkgdir"/usr/lib/sysusers.d/rethinkdb.conf
  install -Dm644 "$srcdir"/rethinkdb-tmpfile.conf "$pkgdir"/usr/lib/tmpfiles.d/rethinkdb.conf
  install -Dm644 "$srcdir"/rethinkdb.service "$pkgdir"/usr/lib/systemd/system/rethinkdb@.service

  # create 'default' database instance
  mv "$pkgdir"/etc/rethinkdb/default.conf.sample "$pkgdir"/etc/rethinkdb/instances.d/default.conf
  sed -e 's|# directory=/var/lib/rethinkdb|directory=/var/lib/rethinkdb|' \
      -i "$pkgdir"/etc/rethinkdb/instances.d/default.conf

  # Arch uses systemd, no need for init.d scripts
  rm -r "$pkgdir"/etc/init.d
}
