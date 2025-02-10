from setuptools import setup, find_packages


setup(
    name='Resume Parser',  
    version='0.1.0', 
    author='M SHIVA RAMA KRISHNA REDDY',
    author_email='msrkreddy111@gmail.com',
    description='This project is designed to extract key information from resumes in PDF or DOC format, save this information to a MySQL database, and offer a web service to manage the extracted data.',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    url='https://github.com/msrkreddy0928/NLP-Project',
    packages=find_packages(),  
    install_requires=[
        'transformers'
        'spacy'
        'datetime'
        'flask'
        'sklearn'
        'mysqldb'
        'pymupdf'
        'pdfplumber'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10.16',
        'Operating System :: OS Independent',
    ],
    python_requires='3.10.16',  
)