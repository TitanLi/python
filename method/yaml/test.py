# pip3 install pyyaml
# 檔名不可以叫yaml否則會有問題
import yaml

with open('./demo.yaml', 'r') as stream:
    try:
        data = yaml.safe_load(stream)
        print(data)
    except yaml.YAMLError as exc:
        print(exc)