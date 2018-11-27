import codecs
import os
import re
import sys

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


long_description = read('README.rst')

setup(
    name="pip",
    version=find_version("src", "pip", "__init__.py"),
    description="The PyPA recommended tool for installing Python packages.",
    long_description=long_description,

    license='MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    url='https://pip.pypa.io/',
    keywords='distutils easy_install egg setuptools wheel virtualenv',

    author='The pip developers',
    author_email='pypa-dev@groups.google.com',

    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    package_data={
        "pip._vendor.certifi": ["*.pem"],
        "pip._vendor.requests": ["*.pem"],
        "pip._vendor.distlib._backport": ["sysconfig.cfg"],
        "pip._vendor.distlib": ["t32.exe", "t64.exe", "w32.exe", "w64.exe"],
    },
    entry_points={
        "console_scripts": [
            "pip=pip._internal:main",
            "pip%s=pip._internal:main" % sys.version_info[:1],
            "pip%s.%s=pip._internal:main" % sys.version_info[:2],
        ],
    },

    zip_safe=False,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',

    extras_require={
        # NOTE: These are the optional requirements for enabling TUF + in-toto.
        'tuf-in-toto': [
            # At the time of writing (Oct 9 2018), this was the latest version
            # of these libraries. We also constraint pip to install only the
            # latest, stable, backwards-compatible release line of TUF
            # (0.11.x).
            'tuf >= 0.11.2.dev1, < 0.12',
            'in-toto >= 0.2.3, < 0.3',
            # Make sure TUF and in-toto use the same version of this library,
            # which they both use in common. At the time of writing (Oct 9
            # 2018), this was the latest version of the library.
            'securesystemslib [crypto, pynacl] >= 0.11.3, < 0.12',
            # Maintain harmony with https://github.com/DataDog/integrations-core/blob/8e3a8aa6d07e2ece7314a39ed05409bbcb6f4979/datadog_checks_base/datadog_checks/base/data/agent_requirements.in
            "asn1crypto==0.24.0",
            "cryptography==2.3",
            "cffi==1.11.5",
            "enum34==1.1.6",
            "ipaddress==1.0.22",
            "pycparser==2.18",
            "requests==2.20.1",
            "six==1.11.0",
        ]
    },
)
