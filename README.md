
# Guide

## How to run program

1. Get code.
2. Create python env.
   ```
   python -m venv changeconfig-env
   ```
3. Install dependence packages.
   ```
   source changeconfig-env/bin/activate
   pip install -r requirements.txt
   ```
4. Run.
   ```
   python main.py
   ```

## How to deploy program

1. Enter env.
    ```
    source changeconfig-env/bin/activate
    ```
2. Deploy app.
   ```
    ./changeconfig-env/binpyside6-deploy main.py
    ```
3. Codesign app.
    ```
    codesign --deep -s "Developer ID Application: Chengdu Xianlin Sanwei Technology Co., Ltd. (5CR2H22F2S)" -fv ChangeConfig.app
    ```