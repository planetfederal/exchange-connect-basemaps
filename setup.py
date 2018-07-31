from setuptools import setup, find_packages

with open('README.rst', 'r') as inp:
    LONG_DESCRIPTION = inp.read()

setup(
    name='exchange-connect-basemaps',
    version='1.0.0',
    author='Boundless Spatial',
    author_email='contact@boundlessgeo.com',
    url='https://github.com/boundlessgeo/exchange-connect-basemaps',
    download_url="https://github.com/boundlessgeo/exchange-connect-basemaps",
    description="Django application to load connect basemaps in Exchange instance.",
    long_description=LONG_DESCRIPTION,
    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: System Administrators',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django :: 1.8',
    ]
)