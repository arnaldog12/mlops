# Local
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# download model from https://github.com/onnx/models/tree/main/text/machine_comprehension/roberta
mv roberta-sequence-classification-9.onnx webapp/

cd webapp
python app.py

curl -X POST  -H "Content-Type: application/JSON" \
      --data '["Containers are more or less interesting"]' \
      http://0.0.0.0:5000/predict
```

# Container
```sh
docker build -t mlops-book/chapter4 . 
docker run -it -p 5000:5000 --rm mlops-book/chapter4

curl -X POST  -H "Content-Type: application/json" \
    --data '["espresso is too strong"]' \
    http://0.0.0.0:5000/predict
```