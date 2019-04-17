# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Vladimir Tsanev <tsachev@gmail.com>
# Contributor: MoeRT09 <https://aur.archlinux.org/account/MoeRT09>
# Contributor: jlkon13 <internet@devpi.de>

pkgname=coturn
pkgver=4.5.1.1
pkgrel=3
pkgdesc='Open-source implementation of TURN and STUN server'
arch=(i686 x86_64 armv7h)
url=https://github.com/coturn/coturn
license=(BSD)
depends=(libevent postgresql-libs libmariadbclient hiredis sqlite)
conflicts=(coturn-git)
install=turnserver.install
backup=(etc/turnserver/turnserver.conf)
source=($url/archive/$pkgver.tar.gz
        turnserver.service
        turnserver.sysusers.d
        turnserver.tmpfiles.d)
sha512sums=('a5e1aecdab5a7060ffbc73cc8dd294cafa701f2e0d2a827e40901cb6001af5a2c5ecbafdf14662410713818aad0ad259133f0dc9b34730bf7911863e1e255f70'
            '47af7bbf28f8a5fc674b90d1370026405ccb43623f05e47cf915c594e7e35865f4dce64d2b3001bc609a843a54661d1a1172790153f0b8ba9186db48c42b0024'
            '32596f741e561c707f69c1ea90adf75c83742906d33c50e1fa5ec0899eeb607d96a48c36fcbb6facb62947beedcace9f6c3fb748c4d67f058bf3f72413766f82'
            '1d47fd988c36e443aa723d048072eb8be8bb59c2845eb1bbd47eae7d955b6bbda7e5526e00f6ee2f54c5121657413058011aa4c130214a83b9f396a35fb45888')

build() {
  cd coturn-$pkgver
  ./configure \
    --prefix=/usr \
    --manprefix=/usr/share \
    --examplesdir=/usr/share/turnserver/examples \
    --disable-rpath
  make
}

check() {
  cd coturn-$pkgver
  make check
}

package() {
  install -Dm 644 turnserver.service "$pkgdir"/usr/lib/systemd/system/turnserver.service
  install -Dm 644 turnserver.sysusers.d "$pkgdir"/usr/lib/sysusers.d/turnserver.conf
  install -Dm 644 turnserver.tmpfiles.d "$pkgdir"/usr/lib/tmpfiles.d/turnserver.conf

  cd coturn-$pkgver

  make DESTDIR="$pkgdir" install
  install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/coturn

  cd "$pkgdir"

  # Create needed directories
  mkdir -p {etc/turnserver,var/log/turnserver}

  # Have the config file use more appropriate directories
  mv {usr/etc/turnserver.conf.default,etc/turnserver/turnserver.conf}
  sed \
    -e '/^#log-file=\/var\/tmp\/turn.log$/c log-file=\/var\/log\/turnserver\/turn.log' \
    -e '/^#pidfile="\/var\/run\/turnserver.pid"$/c pidfile=\/var\/run\/turnserver\/turnserver.pid' \
    -i etc/turnserver/turnserver.conf
  rmdir usr/etc

  # Remove executable bits from files that erroneously have them
  find {etc,usr/include,usr/lib,usr/share,var} -type f ! -name '*.sh' ! -name '*.pl' -exec chmod 644 {} +
}
