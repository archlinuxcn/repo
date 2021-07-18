_name=libsass
pkgname=python-libsass
pkgver=0.21.0
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT License')
depends=('python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
provides=('sassc')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/libsass-0.21.0.tar.gz")
sha256sums=('d5ba529d9ce668be9380563279f3ffe988f27bc5b299c5a28453df2e0b0fbaf2')

build() {
  cd "$srcdir/libsass-0.21.0"
  python3 setup.py build
}

package() {
  cd "$srcdir/libsass-0.21.0"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install any world-writable or root-readable-only files
  # we shouldn't need to fix ownership as we extract tarballs as a non-root user
  # https://github.com/pypa/setuptools/issues/1328
  # https://github.com/LonamiWebs/Telethon/issues/1605
  chmod u=rwX,go=rX -R "$pkgdir"
  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

