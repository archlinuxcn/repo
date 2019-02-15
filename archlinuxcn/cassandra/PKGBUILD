# Maintainer: Oden S. <hello@odensc.me>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>
# Contributor: Guillaume ALAUX <guillaume at alaux dot net>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Konstantin Nikiforov <helllamer@gmail.com>
# Contributor: Alper Kanat <alperkanat@raptiye.org>
# Contributor: adam2fours <adam@2fours.com>

# `makepkg` will refuse to build this package unless you either:
# - manually add upstream signing key to your GPG keyring with:
#   `gpg --recv-keys <UPSTREAM_KEY(S)>`
# - set your GPG config to automatically retrieve missing keys by adding
#   `keyserver-options auto-key-retrieve` to your `~/.gnupg/gpg.conf`

pkgname=cassandra
pkgver=3.11.4
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
source=(https://www.apache.org/dist/${pkgname}/${pkgver}/apache-${pkgname}-${pkgver}-bin.tar.gz{,.asc}
        '01_fix_cassandra_home_path.patch'
        'cassandra.service'
        'cassandra-tmpfile.conf'
        'cassandra-user.conf')
validpgpkeys=('A26E528B271F19B9E5D8E19EA278B781FE4B2BDA') # Michael Shuler <michael@pbandjelly.org>
sha256sums=('5d598e23c3ffc4db0301ec2b313061e3208fae0f9763d4b47888237dd9069987'
            'SKIP'
            'bbb5dcc19cac4e19c506210da901280c3063a6a241480bf12bc874e6a5c02657'
            'abc9d54399c84eacf5922811b5480846ea1c88a73c5d214ea1db3d20c7c0422a'
            '7ea0024331734b9755b6fa2ed1881f9bc608b551990b96f14e80406cb6b05eb8'
            '7a87a4369ca2c13558fa8733f6abdcf548c63dda8a16790b5bcc20bae597ee91')

build() {
  cd ${srcdir}/apache-cassandra-${pkgver}

  patch -p0 < ${srcdir}/01_fix_cassandra_home_path.patch
}

package() {
  cd ${srcdir}/apache-cassandra-${pkgver}

  mkdir -p ${pkgdir}/{etc/cassandra,var/log/cassandra}
  mkdir -p ${pkgdir}/{usr/bin,usr/share/cassandra,usr/share/java/cassandra}

  cp -a interface pylib tools ${pkgdir}/usr/share/cassandra/

  mkdir -p ${pkgdir}/usr/share/cassandra/bin/
  for f in bin/*; do
    if [[ ! "${f}" == *.bat && ! "${f}" == *.ps1 && -x ${f} ]]; then
      cp -a ${f} ${pkgdir}/usr/share/cassandra/bin/
      ln -s /usr/share/cassandra/${f} ${pkgdir}/usr/${f}
    fi
  done
  unlink ${pkgdir}/usr/bin/cqlsh.py
  cp -a bin/cassandra.in.sh ${pkgdir}/usr/share/cassandra/

  cp -a lib/* ${pkgdir}/usr/share/java/cassandra/
  ln -s ../java/cassandra ${pkgdir}/usr/share/cassandra/lib

  cp -a conf/* ${pkgdir}/etc/cassandra/
  rm  ${pkgdir}/etc/cassandra/*.ps1
  ln -s /etc/cassandra ${pkgdir}/usr/share/cassandra/conf

  install -Dm644 ${srcdir}/cassandra.service ${pkgdir}/usr/lib/systemd/system/cassandra.service
  install -Dm644 ${srcdir}/cassandra-tmpfile.conf ${pkgdir}/usr/lib/tmpfiles.d/cassandra.conf
  install -Dm644 ${srcdir}/cassandra-user.conf ${pkgdir}/usr/lib/sysusers.d/cassandra.conf
}
