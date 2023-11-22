from setuptools import setup, find_packages

if __name__ == "__main__":
    with open("README.md") as f:
        long_description = f.read()

    setup(
        long_description=long_description,
    )
