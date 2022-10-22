# Reproducible Research

- Author: MinDong Sung
- Date: 2022-10-21
- For: DHLab

---

## VSCode for Data Science

- Remote SSH
  - <kbd>Ctrl</kbd> + <kbd>R</kbd>: 최근 workspace 목록 확인
  - [참고] 비밀번호 입력하기 힘들면 **SSH key** 생성하기
- Shortcut
  - <kbd>F5</kbd>: Run
  - <kbd>Ctrl</kbd> or <kbd>CMD</kbd> + <kbd>F5</kbd>: Run without debugging
  - <kbd>Ctrl</kbd> or <kbd>CMD</kbd> + <kbd>D</kbd>: multi cursor
  - <kbd>Ctrl</kbd> or <kbd>CMD</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>: palette
- Duplicate workspace
- Jupyter notebook in VScode
  - #%%
  - <kbd>Shift</kbd> + <kbd>Enter</kbd>로 jupyter notebook 실행
    : ![](figure/jupyter_shift_enter.png)
    (setting.json)
    ```
    "jupyter.sendSelectionToInteractiveWindow": true
    ```
- Path set
  - Python script
    ```
    #.env
    PYTHONPATH=.
    ```
    ```
    # setting.json
    "python.envFile": "${workspaceFolder}/.env"
    ```
  - Python notebook
    ```
    # setting.json
    "jupyter.notebookFileRoot": "${workspaceFolder}"
    ```

## Project Management

- envioronment 관리

  - pyenv: python version 관리
  - poetry: python library 관리
    - `poetry init -n`
    - `poetry add`
    - `poetry install`
  - using R in vscode - VSCode-R
  - `renv`: R library 관리
  - library(here)

- project structure

  - `data/`
    - `raw/`
    - `processed/`
  - `src/`
  - `figure/`
  - `README.md`
  - Snakefile/Makefile: for **workflow**

- git - code backup and version control
  - `git init`
  - `git add`
  - `git commit`
  - `git push`

![](https://www.devguide.at/wp-content/uploads/2019/06/git-basic-commands-768x569.png)

- DVC - Data backup and version control
  - AWS-cli prerequisite
  - `poetry add 'dvc[s3]'`
  - `dvc init`
  - `dvc remote add -d data s3://data-folder`
  - `dvc remote modify --local data access_key_id '[mykey]'`
  - `dvc remote modify --local bikes secret_access_key '[mysecret]'`
  - `dvc add`
  - `dvc push`
  - `dvc commit`
  - `dvc pull`
