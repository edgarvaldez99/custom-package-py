from setuptools import setup, find_packages

setup(
    name='custom_package_py',
    packages=find_packages(),
    package_dir={'custom_package_py': '.'},
    version='0.0.0',
    description='',
    author='Edgar Valdez',
    author_email='edgarvaldez99@gmail.com',
    url='https://github.com/edgarvaldez99/custom-package-py',
    include_package_data=True,
    install_requires=[
        'lxml',
        'SQLAlchemy',
        'pyOpenSSL',
        'zeep',
        'requests',
        'pytz',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
