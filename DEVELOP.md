
## Setup

Enable table of content for notebook
```shell
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable toc2/main
```

Embed Turtle Output in your Jupyter Notebook
```shell
pip install ipyturtle
jupyter nbextension enable --py --sys-prefix ipyturtle
```
