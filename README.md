
# Change Config

Use to change json config.

## How to run program

1. Get code.
   ```
   git clone git@github.com:346285234/ChangeConfig.git
   ```
2. Create python env, use python 3.12 to create env as nuitka 2.4.11 support 3.4~3.12.
   ```
   python -m venv env
   ```
3. Install dependence packages.
   ```
   source env/bin/activate
   pip install -r requirements.txt
   ```
4. Run.
   ```
   python main.py
   ```

## How to deploy program

1. Enter env.
    ```
    source env/bin/activate
    ```
2. Create pyside deploy config.
   ```
    ./env/bin/pyside6-deploy --init
    ```
3. Modify deploy config.
   ```
   title = ChangeConfig
   packages = Nuitka==2.4.11
   ``` 
4. deploy.
   ```
   ./env/bin/pyside6-deploy main.py
   ```
5. Codesign app.
    ```
    codesign --deep -s "Developer ID Application: Chengdu Xianlin Sanwei Technology Co., Ltd. (5CR2H22F2S)" -fv ChangeConfig.app
    ```