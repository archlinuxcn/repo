# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>
# Contributor: Guillaume ALAUX <guillaume at alaux dot net>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Konstantin Nikiforov <helllamer@gmail.com> 
# Contributor: Alper Kanat <alperkanat@raptiye.org>
# Contributor: adam2fours <adam@2fours.com>

# check() function is used to verify GPG signature. check() imports 3 keys into your GPG keyring at first build.
# See http://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html for reason of this step.
# If you have problems with gpg, you can remove check() function, and all will be ok.

pkgname=cassandra
pkgver=3.10
pkgrel=1
pkgdesc='Apache Cassandra NoSQL database'
arch=('any')
url='http://cassandra.apache.org/'
license=('APACHE')
depends=('java-runtime')
makedepends=('gnupg')
checkdepends=('wget')
optdepends=('python: to use Python CLI administration scripts')
backup=(etc/cassandra/cassandra-env.sh
        etc/cassandra/cassandra-rackdc.properties
        etc/cassandra/cassandra-topology.properties
        etc/cassandra/cassandra.yaml
        etc/cassandra/commitlog_archiving.properties
        etc/cassandra/logback.xml
        etc/cassandra/logback-tools.xml)
install=cassandra.install
_url_tgz="http://www.apache.org/dist/${pkgname}/${pkgver}/apache-${pkgname}-${pkgver}-bin.tar.gz"
source=("${_url_tgz}"
        '01_fix_cassandra_home_path.patch'
        'cassandra.install'
        'cassandra.service'
        'cassandra-tmpfile.conf'
        'cassandra-user.conf')
sha256sums=('c09c3f92d4f80d5639e3f1624c9eec45d25793bbb6b3e3640937b68a9c6d107f'
            'bbb5dcc19cac4e19c506210da901280c3063a6a241480bf12bc874e6a5c02657'
            '971d6d0f21963b2d9443039431e5225191771454728c6eda4aab9175ee478ce4'
            'abc9d54399c84eacf5922811b5480846ea1c88a73c5d214ea1db3d20c7c0422a'
            '7ea0024331734b9755b6fa2ed1881f9bc608b551990b96f14e80406cb6b05eb8'
            '7a87a4369ca2c13558fa8733f6abdcf548c63dda8a16790b5bcc20bae597ee91')

build() {
  cd ${srcdir}/apache-cassandra-${pkgver}

  patch -p0 < ${srcdir}/01_fix_cassandra_home_path.patch
}

## to check gpg signature
check() {
  msg "Checking GPG signature..."
  msg2 "(To disable gpg-check: build with '--nocheck')"

  _url_keys='https://www.apache.org/dist/cassandra/KEYS'
  msg "Importing GPG keys from ${_url_keys} ..."
  wget --quiet -O - ${_url_keys} | gpg --import -

  # no need to add signature to package dependences
  echo "${_url_tgz}.asc"
  wget --quiet -O - "${_url_tgz}.asc" | gpg --verify - "apache-${pkgname}-${pkgver}-bin.tar.gz"
  msg2 "Detached GPG signature is valid."
}

package() {
  cd ${srcdir}/apache-cassandra-${pkgver}

  mkdir -p ${pkgdir}/{etc/cassandra,var/log/cassandra}
  mkdir -p ${pkgdir}/{usr/bin,usr/share/cassandra,usr/share/java/cassandra}

  cp -a interface pylib tools ${pkgdir}/usr/share/cassandra/

  mkdir -p ${pkgdir}/usr/share/cassandra/bin/
  for f in bin/*; do
    if [[ ! "${f}" == *.bat && -x ${f} ]]; then
      cp -a ${f} ${pkgdir}/usr/share/cassandra/bin/
      ln -s /usr/share/cassandra/${f} ${pkgdir}/usr/${f}
    fi
  done
  cp -a bin/cassandra.in.sh ${pkgdir}/usr/share/cassandra/

  cp -a lib/* ${pkgdir}/usr/share/java/cassandra/
  ln -s ../java/cassandra ${pkgdir}/usr/share/cassandra/lib

  cp -a conf/* ${pkgdir}/etc/cassandra/
  ln -s /etc/cassandra ${pkgdir}/usr/share/cassandra/conf

  install -Dm644 ${srcdir}/cassandra.service ${pkgdir}/usr/lib/systemd/system/cassandra.service
  install -Dm644 ${srcdir}/cassandra-tmpfile.conf ${pkgdir}/usr/lib/tmpfiles.d/cassandra.conf
  install -Dm644 ${srcdir}/cassandra-user.conf ${pkgdir}/usr/lib/sysusers.d/cassandra.conf
}

# vim:set ts=2 sw=2 et:
