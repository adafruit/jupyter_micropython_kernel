# Jupyter MicroPython Kernel

Jupyter kernel to interact with a MicroPython or CircuitPython board over its serial REPL.  Note this is _highly_ experimental and still alpha/beta quality.  Try it out but don't be surprised if it behaves in odd or unexpected ways!

## Installation

Create and activate a virtualenv

``` console
$ python3 -m venv jupytermp
$ source jupytermp/bin/activate
(jupytermp) $
```

Install this package using pip

``` console
(jupytermp) $ pip install https://github.com/dwighthubbard/jupyter_micropython_kernel/zipball/master
...
Installing collected packages: wcwidth, six, prompt-toolkit, pyzmq, decorator, ipython-genutils, traitlets, jupyter-core, python-dateutil, tornado, jupyter-client, ptyprocess, pexpect, pickleshare, simplegeneric, backcall, parso, jedi, pygments, ipython, ipykernel, jupyter-console, jsonschema, nbformat, pandocfilters, entrypoints, testpath, webencodings, html5lib, bleach, mistune, MarkupSafe, jinja2, nbconvert, terminado, Send2Trash, notebook, qtconsole, widgetsnbextension, ipywidgets, jupyter, pyserial, jupyter-micropython-kernel
  Running setup.py install for tornado ... done
  Running setup.py install for simplegeneric ... done
  Running setup.py install for backcall ... done
  Running setup.py install for pandocfilters ... done
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for jupyter-micropython-kernel ... done
Successfully installed MarkupSafe-1.0 Send2Trash-1.5.0 backcall-0.1.0 bleach-2.1.3 decorator-4.3.0 entrypoints-0.2.3 html5lib-1.0.1 ipykernel-4.8.2 ipython-6.4.0 ipython-genutils-0.2.0 ipywidgets-7.2.1 jedi-0.12.0 jinja2-2.10 jsonschema-2.6.0 jupyter-1.0.0 jupyter-client-5.2.3 jupyter-console-5.2.0 jupyter-core-4.4.0 jupyter-micropython-kernel-0.1.1 mistune-0.8.3 nbconvert-5.3.1 nbformat-4.4.0 notebook-5.5.0 pandocfilters-1.4.2 parso-0.2.1 pexpect-4.6.0 pickleshare-0.7.4 prompt-toolkit-1.0.15 ptyprocess-0.5.2 pygments-2.2.0 pyserial-3.4 python-dateutil-2.7.3 pyzmq-17.0.0 qtconsole-4.3.1 simplegeneric-0.8.1 six-1.11.0 terminado-0.8.1 testpath-0.3.1 tornado-5.0.2 traitlets-4.3.2 wcwidth-0.1.7 webencodings-0.5.1 widgetsnbextension-3.2.1
(jupytermp) $
```

Install the jupyter kernel

``` console
(jupytermp) $ python -m jupyter_micropython_kernel.install
DEBUG:__main__:Putting kernel in virtualenv share directory '/tmp/mpnotebook/share/jupyter'
INFO:__main__:Writing jupyter kernel to '/tmp/mpnotebook/share/jupyter/kernels/micropython/kernel.json'
(jupytermp) $
```

Now run Jupyter notebook:

``` console
(jupytermp) $ jupyter notebook
```

In the notebook click the New button in the upper right, you should see your
MicroPython kernel display name listed.  Click it to create a notebook using
that board connection (make sure the board is connected first!).
