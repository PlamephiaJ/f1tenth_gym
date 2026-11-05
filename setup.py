from setuptools import setup, find_packages

setup(name='f110_gym',
      version='0.3.0',
      author='Hongrui Zheng, Jonas Kuehne',
      author_email='billyzheng.bz@gmail.com, jonaskuehne92@gmail.com',
      url='https://f1tenth.org',
      packages=find_packages(where='gym'),
      package_dir={'': 'gym'},
      install_requires=['gymnasium==0.29.1',
		            'numpy>=1.18.0',
                        'Pillow>=9.0.1',
                        'scipy>=1.7.3',
                        'numba>=0.55.2',
                        'pyyaml>=5.3.1',
                        'pyglet==1.5.20',
                        'pyopengl']
      )
