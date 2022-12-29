_name=iredis
pkgname=iredis
pkgver=1.13.0
pkgrel=1
pkgdesc="Terminal client for Redis with auto-completion and syntax highlighting."
arch=(any)
url="https://github.com/laixintao/iredis"
license=('BSD-3-Clause')
depends=('python' 'python-redis' 'python-prompt_toolkit' 'python-pygments' 'python-mistune' 'python-configobj' 'python-click' 'python-pendulum' 'python-importlib_resources' 'python-wcwidth')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/iredis-1.13.0.tar.gz")
sha256sums=('d1e4e7936d0be456f70a39abeb1c97d931f66ccd60e891f4fd796ffb06dfeaf9')

build() {
  cd "$srcdir/iredis-1.13.0"
  python3 setup.py build
}

package() {
  cd "$srcdir/iredis-1.13.0"
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

