## Start Machine Learning Project

### Software and account Requirement:

1. [GitHub Account](https://github.com/)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [GIT cli](https://git-scm.com/downloads)

Creating conda environment
```
conda create -p venv python==3.10 -y
```

For activating the environment
```
conda activate venv/
```
OR
```
conda activate venv
```

```
pip install -r requirements.txt
```

Build Docker Image
```
docker build -t <image_name>:<tagname>
```
> Note : Image name for docker must be lowercase

Run Docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_name>
```

it will install all the library in setup
```
python setup.py install
```

To Install ipykernel
```
pip install ipykernel
```