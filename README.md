
# License Plate Detector

A License Plate Detector trained in YOLOv8.

## Installation

You can either clone my repository by running the following command in your terminal (remember to open the terminal in the folder you want this project in)

```bash
 git clone https://github.com/PythoneerSamurai/YOLOv8-License-Plate-Detector.git
```

![App Screenshot](https://github.com/PythoneerSamurai/YOLOv8-License-Plate-Detector/assets/112153865/fc99119d-2aa6-4bdd-8de6-4d054f1886a5)

Otherwise, you can just download this project in the form of a ZIP file, by clicking the 'green code button' and then clicking the 'download ZIP' button.

![App Screenshot](https://github.com/PythoneerSamurai/YOLOv8-License-Plate-Detector/assets/112153865/73d95e36-e007-4dc1-b292-0a108f7b049f)
    
## Usage

The usage of the model is fairly simple, you need to have python installed. In addition to that you need a python library called 'ultralytics', you can install it by running the following command in your terminal

```javascript
pip install ultralytics
```

Afterwards, just open the 'main.py' file in the IDE or text editor of your choice, and specifiy the absolute path to the model file (a portion of the path is already written in the main.py file, so that you don't get confused)

![App Screenshot](https://github.com/PythoneerSamurai/YOLOv8-License-Plate-Detector/assets/112153865/7fa89cd0-ee74-412a-a939-226009d356c1)

Then you need to specify the source, it can be any one of the options available in the list of inference sources on the following website:

https://docs.ultralytics.com/modes/predict/#inference-sources

Also, you can choose the inference source to be you webcam, source=0

I have set save_crop = True, so that the model also saves cropped images of the plates it detects.

## Results
Real Images
![App Screenshot](https://github.com/PythoneerSamurai/YOLOv8-License-Plate-Detector/assets/112153865/bc049c3f-d31f-49cc-a4ea-5cb681524ca6)

Model Predictions
![App Screenshot](https://github.com/PythoneerSamurai/YOLOv8-License-Plate-Detector/assets/112153865/15365a89-9c8b-48a6-badc-91c1afbcdc45)

## Acknowledgements

 - [Dataset from Roboflow Universe]
 - [Website for making nice GitHub readme files](https://readme.so/)



## License

No License.

