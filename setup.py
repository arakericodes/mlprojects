from setuptools import find_packages,setup # type: ignore

def get_requriements(file_path):
    reuirements = []
    with open(file_path) as f:
        reuirements = f.readlines()
        reuirements = [x.replace('\n', '') for x in reuirements]
        for x in reuirements:
            if x == '-e .':
                reuirements.remove(x)
            else:
                continue
    return reuirements

        


setup(
    name='mlproject',
    version='0.0.1',
    author='anirudh_arakeri',
    author_email='anirudharakeri73@gmail.com',
    packages=find_packages(),
    install_requires = get_requriements('requirements.txt')
)

