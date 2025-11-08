# wget

## Self dependency and bootstrapping / rebuilding on soname changes

Upstream (autotools) bootstrap scripts used to prepare the `wget` and the `gnulib` submodule sources both require `wget` to download `po` (translation) files.  
This implies that the `wget` package *(make-)*depends on itself.

While this shouldn't be a problem for regular version bumps, it can lead to issues when bootstrapping the package (e.g. when adding new architectures) and it can have theoretical implications when rebuilding the package in staging due to soname changes (in case `wget` doesn't work until rebuilding for instance).  
To address this, the PKGBUILD contains a custom `$_bootstrap` variable whose value can be modified as needed:

- When set to `0`, the package is built "normally"
- When set to `1`, the package is built by skipping the `po` files download step so the `wget` make-dependency is unused (allowing to bootstrap it or rebuild it after soname changes without issue).

**WARNING:** Building the package with `$_bootstrap=1` therefore results in a `wget` package that does not include po (translation) files, so make sure to rebuild it with `$_bootstrap=0` when the bootstrapping / rebuilding after soname changes is done (see `checkpkg` output).
