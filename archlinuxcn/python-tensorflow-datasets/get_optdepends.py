from packaging.requirements import Requirement
import setuptools

# HACK: prevent the actual setup() from running and terminating the program
def fake_setup(*args, **kwargs):
    pass
setuptools.setup = fake_setup

from setup import DATASET_EXTRAS

KNOWN_PKGS = {
    'bs4': 'python-beautifulsoup4',
    'opencv-python': 'python-opencv',
}

def main():
    optdepends = {}
    for dataset, deps in DATASET_EXTRAS.items():
        for dep in deps:
            # https://peps.python.org/pep-0508/#names
            dep = Requirement(dep).name
            dep = dep.lower().replace('_', '-')
            dep = KNOWN_PKGS.get(dep, f'python-{dep}')
            optdepends.setdefault(dep, []).append(dataset)
    for dep, datasets in optdepends.items():
        print(f"'{dep}: for {', '.join(datasets)}'")

    print(f"# {' '.join(optdepends.keys())}")

if __name__ == '__main__':
    main()
