## Initial Maintainer: Augusto F. Hack <hack.augusto@gmail.com>
Maintainer='Gilles Hamel <hamelg@laposte.net>'
pkgname=python2-carbon
pkgver=1.0.2
pkgrel=3
pkgdesc='Backend data caching and persistence daemon for Graphite'
arch=('any')
url='https://github.com/graphite-project/carbon'
license=('Apache')
depends=('python2' 'python2-whisper' 'python2-twisted>=13.2.0')
optdepends=('python2-txamqp: AMQP support')
makedepends=('python2-setuptools')
options=(!emptydirs)
source=("https://github.com/graphite-project/carbon/archive/$pkgver.tar.gz" carbon.service carbon.conf)
md5sums=(5dacf9b12c4d76d76ac3b3bc7409e243 5305b294d608a62945d5fc11854e25cd 4b6d054aed3304af567552782b72ea8b)
backup=(etc/carbon/aggregation-rules.conf etc/carbon/blacklist.conf etc/carbon/carbon.amqp.conf etc/carbon/carbon.conf etc/carbon/relay-rules.conf etc/carbon/rewrite-rules.conf etc/carbon/storage-aggregation.conf etc/carbon/storage-schemas.conf etc/carbon/whitelist.conf)

package() {
  cd "$srcdir/carbon-$pkgver"
  python2 setup.py install --root="$pkgdir/" --install-lib=/usr/lib/python2.7/site-packages --install-data=/var/lib/graphite --install-scripts=/usr/bin --optimize=1
  install -D -m644 $srcdir/carbon.service $pkgdir/usr/lib/systemd/system/carbon.service

  # change the directory of the config files
  ls conf | while read conf; do
    install -D -m644 conf/$conf $pkgdir/etc/carbon/${conf/.example}
  done;
  rm -r $pkgdir/var

  # use our config with FHS
  install -D -m644 $srcdir/carbon.conf $pkgdir/etc/carbon/carbon.conf
}

# vim:set ts=2 sw=2 et:
