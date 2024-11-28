from setuptools import setup, find_packages

setup(
    name='market-simulation',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'matplotlib>=3.4.0',
        'scipy>=1.7.0'
    ],
    author='Leon de Vries',
    description='A market simulation model with strategic pricing',
    long_description=open('docs/README.md').read(),
    python_requires='>=3.8',
)