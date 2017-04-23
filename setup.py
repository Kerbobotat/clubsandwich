from setuptools import setup, find_packages

setup(
    name='clubsandwich',
    version='0.1.0a1',
    author='Steve Johnson',
    author_email='steve@steveasleep.com',
    license='MIT',
    packages=find_packages(exclude=["docs"]),
    url='https://github.com/irskep/clubsandwich',
    install_requires=[
        'bearlibterminal',
    ],
    entry_points='''
        [console_scripts]
        babysit=clubsandwich.babysit:cli
    ''',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)