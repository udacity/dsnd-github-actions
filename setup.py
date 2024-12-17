from setuptools import setup, find_packages
from pathlib import Path

if __name__ == "__main__":

    cwd = Path(__file__).parent
    req_path = cwd / 'requirements.txt'
    reqs = req_path.read_text().split('\n')

    setup(
        name="package_name".
        version="0.0.0".
        packages=find_packages(),
        install_requires=reqs,
    )