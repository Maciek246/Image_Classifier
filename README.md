# IMAGE CLASSIFIER

## INFO
<ul>
    <li>Python 3.5.4</li>
    <li>TensorFlow 1.7.0</li>
    <li>PIL 5.1.0 // <i>for script "prepare_data.py"</i></li>
</ul>

**Resource**
<div>
DataSet: <a href='https://www.kaggle.com/olgabelitskaya/traditional-decor-patterns/data'>
https://www.kaggle.com/olgabelitskaya/traditional-decor-patterns/data
</a><br/>
Tutorial: <a href='https://codelabs.developers.google.com/codelabs/tensorflow-for-poets'>
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets
</a>
</div>

## How to run it

### 1. Create Virtual Environment

**Windows:**

		python -m venv tensorenv
	
	
**Linux:**
	
		python3 -m venv myvenv
	
	
### 2. Enable Virtual Environment

**Windows:**
	
		env\Scripts\activate
	
**Linux:**
	
		env/bin/activate
	
	
### 3. Install TensorFlow and other dependencies

	pip3 install -r requirements.txt
	
	
### 4. Clone repository from GitHub
	
	git clone https://github.com/googlecodelabs/tensorflow-for-poets-2
	
	
### 5. Download the training images and extract in main directory of project

That should look like this:
	
	.
	├── tensorflow-for-poets-2
	│   ├── android
	│   ├── ios
	│   ├── scripts
	│   ├── tf_files
	│   ├── .gitignore
	│   ├── CONTRIBUTING.md
	│   ├── LICENSE
	│   └── README.md
	├── traditional-decor-patterns
	│   ├── decor //directory with images
	│   ├── decor.csv
	│   ├── decor.zip
	│   └── DecorColorImages.h5
    ├── requirements.txt
	
### 6. Paste and run script ("prepare_data.py") which prepare data for alghoritm or you can do it manually (if you have too many time :D )
	
	python prepare_data.py
	
That should look like this:
	
	.
	├── tensorflow-for-poets-2
	│   ├── android
	│   ├── ios
	│   ├── scripts
	│   ├── tf_files
	│   │   └── decor
	│   ├── .gitignore
	│   ├── CONTRIBUTING.md
	│   ├── LICENSE
	│   └── README.md
	├── traditional-decor-patterns
	│   ├── decor
	│   ├── decor.csv
	│   ├── decor.zip
	│   └── DecorColorImages.h5
	├── prepare_data.py

### 7. Set environment variables

**Windows:**
        
	set IMAGE_SIZE=224
	set ARCHITECTURE=mobilenet_0.50_%IMAGE_SIZE%
**Linux:**

    IMAGE_SIZE=224
    ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"
		
	
### 8. Go to tensorflow-for-poets-2 directory and run the retrain script

**Windows:**

	cd tensorflow-for-poets-2
	python -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps=500 --model_dir=tf_files\models --summaries_dir=tf_files\training_summaries\%ARCHITECTURE% --output_graph=tf_files\retrained_graph.pb --output_labels=tf_files\retrained_labels.txt --architecture=%ARCHITECTURE% --image_dir=tf_files\decor
**Linux:**

    cd tensorflow-for-poets-2 
    python -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps=500 --model_dir=tf_files/models/ --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --architecture="${ARCHITECTURE}" --image_dir=tf_files/decor
		
### 9. Using the Retrained Model

**Windows:**

		python -m scripts.label_image --graph=tf_files\retrained_graph.pb --image=<Path to image>
**Linux:**

		python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=<Path to image>
		
## TEST:

RUN:
	
	python -m scripts.label_image --graph=tf_files\retrained_graph.pb --image="tf_files\decor\Wzory kaszubskie\02_07_2_008.jpg" 
	
RESULT:	
	
	Evaluation time (1-image): 0.261s
	
	wzory kaszubskie 0.9939978
	wycinanki lowickie 0.0035613931
	gorodets 0.0023427997
	iznik 7.733403e-05
	gzhel 1.7852544e-05
	