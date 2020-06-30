import setuptools

setuptools.setup(
    name='django-configurations-apps',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
