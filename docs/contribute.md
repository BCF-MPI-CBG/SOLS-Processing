# Contributing

Before contributing code to this repository, please read through this section to be compliant with the general code guidelines for this repository. If you want to contribute a function here, please make sure to follow the following implementation steps:

## Implementing the function

The basic functionality shall be put under `root/src/napari_sols_processing/_functions.py`. When adding a function, please make sure to follow the syntax example as demonstrated by the demo function `some_processing_function`:

```python
def some_processing_function(
        input_image: Image,
        threshold: int = 128) -> Labels:
    """
    A placeholder function to demonstrate the structure of the module.
    
    Parameters
    ----------
    data : any
        The data to be processed.
    
    Returns
    -------
    processed_data : any
        The processed data.
    """
    # Perform some processing on the data, for instance thresholding:

    binary = input_image.data > threshold

    return Labels(binary.astype(int), name='binary_labels')
```

The important parts here are, among others, *the input and return type annotations*. These tell napari how to generate graphical user interfaces (GUIs) directly from the code itself and provide a standardized template for processing functions. By choosing [napari layers](https://napari.org/stable/guides/layers.html) as input and output types, we can make sure that we can pass along metadata (e.g., pixel sizes, world coordinates, affine transformations) along with the data.

```python
input_image: Image,
```

Once your function is there, make sure to add it in the `/src/napari_sols_processing/__init__.py` file so that it can be imported from elsewhere like this

```python
import napari_sols_processing as nsp
result = nsp.some_processing_function(...)
```

Lastly, make sure to add a function that tests your contributed function under `/src/napari_sols-processing/_tests`.

## Making the function available in napari

In order to make the function available as a GUI in the napari viewer, add your function to the `/src/napari_sols_processing/napari.yaml` according to [this reference](https://napari.org/stable/plugins/building_a_plugin/guides.html). That's it - your function is now available as a GUI in napari.

## Documentation

As a member of the `napari_sols_processing` package, the function should automatically be added to the API reference here in the documentation. You can build the documentation locally to see whether it works like this: Firstly, install jupyter-book:

```bash
pip install jupyter-book
```

Then, build the docs like this (Make sure you have the plugin installed in your environment):

```bash
jupyter-book build docs/
```

Finally, add your name (and email, if you want) to the list of authors in the package metadata (`pyproject.toml`)