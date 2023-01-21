### jupyter kernel
- Check jupyter kernels:  
```jupyter kernelspec list```
- Install ipykernel (if not yet installed):  
```conda install -c anaconda ipykernel```
- Add ipykernel (name=`env`):  
```python -m ipykernel install --user --name=env```
- Remove unwanted ipykernel (name=`env`):  
```jupyter kernelspec uninstall env```