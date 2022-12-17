# Maintainer: Christopher Arndt <aur -at- chrisarndt -dot- de>
# Contributor: Simon Conseil <contact+aur at saimon dot org>

pkgname=pip-tools
pkgver=6.12.1
pkgrel=1
pkgdesc='A set of tools to keep your pinned Python dependencies fresh'
arch=(any)
url='https://github.com/jazzband/pip-tools/'
license=(BSD)
depends=(python-build 'python-click>=7' 'python-pip>=22' python-setuptools python-wheel)
makedepends=(python-installer python-setuptools-scm python-wheel)
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz"
        'pip-tools-bash-completion.sh'
        'pip-tools-zsh-completion.zsh'
        'pip-tools-fish-completion.fish')
sha256sums=('88efb7b29a923ffeac0713e6f23ef8529cc6175527d42b93f73756cc94387293'
            '12d90c4aab717d58a435610a3cdc94aa925b4f89f9f9f700a05c8cfa058f7960'
            '63f8d032a742ae33903040477c777922ec06241383d165c93803f1b41316ff51'
            '9c60407e485e71ded1d695455378fa4f09e76ecb8556d21c31f8610cb47cf525')


build() {
  cd $pkgname-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $pkgname-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  # shell completion
  install -Dm644 "$srcdir"/pip-tools-bash-completion.sh "$pkgdir"/etc/bash_completion.d/pip-tools
  install -Dm644 "$srcdir"/pip-tools-zsh-completion.zsh "$pkgdir"/usr/share/zsh/site-functions/_pip-tools
  install -Dm644 "$srcdir"/pip-tools-fish-completion.fish "$pkgdir"/usr/share/fish/vendor_completions.d/pip-tools.fish
  # license
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
  # documentation
  install -Dm644 CHANGELOG.md CONTRIBUTING.md README.rst \
    -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 img/*.svg -t "$pkgdir"/usr/share/doc/$pkgname/img
  install -Dm644 examples/* -t "$pkgdir"/usr/share/doc/$pkgname/examples

  # Suppress warnings from deprecated Python distutils package
  sed -i -e 's@python$@python -W ignore:Setuptools is replacing distutils.:UserWarning:@' \
    "$pkgdir"/usr/bin/pip-compile
  sed -i -e 's@python$@python -W ignore:Setuptools is replacing distutils.:UserWarning:@' \
    "$pkgdir"/usr/bin/pip-sync
}

# vim:set ts=2 sw=2 et:
