import setuptools

setuptools.setup(
    name='django-configurations-apps',
    version='2020.7.2',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
