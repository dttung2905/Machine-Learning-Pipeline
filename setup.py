from setuptools import setup, find_packages

setup(
        name="mlpipeline",
        version="0.1",
        author="Thanh Tung Dao",
        author_email="dttung2905@gmail.com",
        description="Fast developement of machine learning pipeline",
        packages=find_packages(),
        install_requires=[
            'flake8==3.7.8',
            'matplotlib==3.1.1',
            'numpy==1.22.0',
            'pandas==0.25.1',
            'pytest==5.1.2',
            'python-dateutil==2.8.0',
            'pytest-cov==2.7.1'
            ]

        )
