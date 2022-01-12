# Plotting the Oura Ring Data

## Getting and understanding the data

https://support.ouraring.com/hc/en-us/articles/360025441594-Export-and-Share-Your-Oura-Data
https://cloud.ouraring.com/docs/sleep
https://pandas.pydata.org/docs/index.html



## Prerequisites: Howto setup Jupyter notebook for WSL2 (pyenv, pip)

Command line: Choose the python env you wish to use, then:

```bash
pyenv install 3.10.0
pyenv virtualenv 3.10.0 jupyters
pyenv local jupyters
python -m pip install jupyterlab  (or pip install jupyterlab)
python -m jupyterlab --no-browser (or jupyter-lab --no-browser)
```

optional: pip install pandas mlplot




