try:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:
    from pip.req import parse_requirements
    from pip.download import PipSession

from distutils.core import setup
from setuptools import find_packages

inst_req = parse_requirements('requirements.txt', session=PipSession())
REQUIREMENTS = [str(r.req) for r in inst_req]

setup(
    name='exchange-connect-basemaps',
    version='1.0.0',
    author='Boundless Spatial',
    author_email='contact@boundlessgeo.com',
    url='https://github.com/boundlessgeo/exchange-connect-basemaps',
    download_url="https://github.com/boundlessgeo/exchange-connect-basemaps",
    description="Django application to load connect layers in Exchange.",
    long_description=open('README.rst').read(),
    license='GPLv3',
    install_requires=REQUIREMENTS,
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
