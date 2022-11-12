_name=libsass
pkgname=python-libsass
pkgver=0.22.0
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT License')
depends=('python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
provides=('sassc')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/libsass-0.22.0.tar.gz")
sha256sums=('3ab5ad18e47db560f4f0c09e3d28cf3bb1a44711257488ac2adad69f4f7f8425')

build() {
  cd "$srcdir/libsass-0.22.0"
  python3 setup.py build
}

package() {
  cd "$srcdir/libsass-0.22.0"
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

