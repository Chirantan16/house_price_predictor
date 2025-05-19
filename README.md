This project is a basic demonstration of a ML Prediction Model 
to predict the price of houses based on few parameters.

The Project Directory Tree:

```
house_price_predictor/
├── static/
│   ├── bg.jpg
│   ├── bghead.jpg
│   ├── description.jpg
│   ├── house.jpg
│   ├── logo.jpg
│   └── predict.jpg
├── templates/
│   ├── after.html
│   └── index.html
├── app.py
├── kafka-env/           # (created after running venv)
├── housing_desc.txt
├── housing.pkl
├── housing.py
├── requirements.txt
├── test.csv
└── train.csv
```

To Run the Project in Ubuntu a virtual environment needs to be created.

python3 -m venv kafka-env
source kafka-env/bin/activate
pip install -r requirements.txt