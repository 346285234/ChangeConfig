
## How to deploy

```
# 进入虚拟环境
cd .qtcreator/Python_3_12_0venv/bin
source activate

# 生成app
pyside6-deploy ../../../main.py

# 签名app
codesign --deep -s "Developer ID Application: Chengdu Xianlin Sanwei Technology Co., Ltd. (5CR2H22F2S)" -fv ChangeConfig.app
```