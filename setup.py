from setuptools import setup


install_requires = [
    "anndata",
    "scanpy",
    "networkx",
    "torch",
    "pyro-ppl",
    "scikit-learn",
    "snakemake",
    "statsmodels",
    "joblib",
    "numpy",
    "pandas",
    "scipy",
]


setup(
    name='scquint',
    version='0.2',
    description='scQuint',
    url='http://github.com/songlab-cal/scquint',
    author='Gonzalo Benegas',
    author_email='gbenegas@berkeley.edu',
    license='MIT',
    packages=['scquint'],
    zip_safe=False,
    install_requires=install_requires,
    extras_require = {
        'vae':  ["scvi==0.5.0"],
    }
)