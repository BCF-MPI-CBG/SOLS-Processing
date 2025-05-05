import numpy as np
import napari_sols_processing as nsp

def test_something():
    from napari.layers import Image, Labels

    test_data = np.random.rand(100, 100)

    image = Image(test_data)

    result = nsp.some_processing_function(image, threshold=0.5)
    
