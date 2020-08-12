import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'pictures',         
  packages = ['pictures'],   
  version = '0.5',     
  license='MIT',        
  description = 'Useful for Image processing', 
  long_description=long_description,
  long_description_content_type='text/markdown'  ,
  author = 'SALMAN_FAROZ',                   
  author_email = 'farozsts@gmail.com',      
  url = 'https://github.com/stsfaroz/pictures',  
  download_url = 'https://github.com/stsfaroz/pictures/archive/0.5.tar.gz',    
  keywords = ['imagetogif', 'gif show',"images to gif", "img2gif"],   
  install_requires=["pillow","ipython"],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',
  ],
)
