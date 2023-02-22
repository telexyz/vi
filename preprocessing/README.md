```
cd dps/
pip install pyspark==3.2.1 fire==0.3.1 pyyaml bs4 html2text python-stdnum
sudo python3 setup.py install
python3 bin/sparkapp.py sample_job --config_path=./configs/sample_job.yaml
```