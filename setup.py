from setuptools import setup, find_packages

setup(
    name='MjPy',
    version='0.0.0',
    python_requires='>=3.0',
    # install_requires=[],
    packages=find_packages()+['.'],
    include_package_data=True,
    url='https://github.com/ASafarzadeh/mjpy',
    license='GPL-2.0',
    description='Python Unofficial Midjourney Client',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='midjourney midjourney-api midjourney-client',
    entry_points={
        'console_scripts': [
            'mjpy = mjpy:main',
        ],
    },
    long_description = "MjPy is an unofficial python midjourney client. See more info at Github: [https://github.com/ASafarzadeh/mjpy](https://github.com/ASafarzadeh/mjpy)",
    long_description_content_type='text/markdown',
)
