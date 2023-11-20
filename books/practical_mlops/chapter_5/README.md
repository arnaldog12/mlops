# Setup
```sh
python3 -m venv venv
source venv/bin/activate
```

# Ludwig 

```sh
pip install ludwig
ludwig experiment --dataset reuters-allcats.csv --config config.yaml
```

# flaml

```sh
pip install "flaml[automl]"

python main_flaml.py
``