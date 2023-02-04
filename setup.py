import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'freqit',
  packages = setuptools.find_packages(),
  version = '1.0',
  license='MIT',
  description = 'Better frequency and crosstab tables.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Lauren McNamara',
  author_email = 'lauren.mcnamara@gmail.com',
  url = 'https://github.com/la-mcnamara/freqit',
  keywords = ['FREQUENCY', 'TABLE', 'CROSSTAB'],
  install_requires=[
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8'
  ],
)