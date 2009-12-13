from setuptools import setup, find_packages


setup(
    name='nosexcover',
    version='0.1',
    description='Fork of nose.plugins.cover that can output Cobertura-style XML reports',
    long_description=open('README').read(),
    author='Chris Heisel',
    author_email='chris@heisel.org',
    url='http://github.com/cmheisel/nose-xcover/',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['nose', 'coverage'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points = {
        'nose.plugins': [ 'xcover = nosexcover:XCoverage' ]
    },
)
