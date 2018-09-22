from lilaclib import *

build_prefix = 'extra-x86_64'
depends = [
  ('rust-nightly', 'rust-std-nightly-x86_64-unknown-linux-gnu'),
  ('rust-nightly', 'rust-nightly'),
  ('rust-nightly', 'cargo-nightly'),
]
update_on = [{
  'github': 'BurntSushi/ripgrep',
}]

pre_build = vcs_update

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
