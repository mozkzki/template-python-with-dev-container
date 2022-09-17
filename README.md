# template-python-with-dev-container

Python開発用テンプレート。VSCodeのRemote Containers での開発用。

#### ファイル構成

- `.devcontainer/devcontainer.json`
    - Remote Containersの設定：[公式のベース](https://github.com/microsoft/vscode-dev-containers/tree/v0.191.0/containers/python-3)を修正
- `.devcontainer/Dockerfile`
    - イメージのビルド設定：[公式のベース](https://github.com/microsoft/vscode-dev-containers/blob/v0.191.0/containers/python-3/.devcontainer/base.Dockerfile)を修正
- `.devcontainer/dotfiles`
    - zshの設定等

#### Shell環境

| kind | tool |
|--|--|
| shell | zsh |
| zsh framework | prezto |
| prompt | powerlevel10k |

#### Python環境

| kind | tool |
|--|--|
| package management | [pip](https://kurozumi.github.io/pip/index.html) |
| testing framework | [pytest](https://docs.pytest.org/en/6.2.x/) |
| linter | [flake8](https://flake8.pycqa.org/en/latest/) |
| formatter | [black](https://github.com/psf/black) |
| type check | [mypy](https://mypy.readthedocs.io/en/stable/) |

※ コンテナなのでPythonの仮想環境 (PoetryとかPipenvとか) は使わない

## 導入方法

※M1 Macでのみ動確

1. ローカルにコンテナ環境を用意 (Macだと[`Rancher Desktop`](https://rancherdesktop.io/)が[簡単](https://knqyf263.hatenablog.com/entry/2022/02/01/225546))
1. VSCodeに「[Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)」プラグインをインストール
1. `git clone`してVSCodeでプロジェクトを開く
1. VSCodeの画面左下の緑ゾーンをクリック
1. `Reopen in Container`をクリック
1. コンテナ内でVSCodeが開いたら準備完了 (初回は時間かかる)

## 開発方法

### とりあえず一通り動確したい時

```sh
make lint
make ut
make start
```

### Run

```sh
python ./main/my/app.py
# もしくは
make start
```

### Unit Test

全部実行

```sh
pytest
pytest -v # verbose
pytest -s # 標準出力を出す (--capture=noと同じ)
pytest -ra # サマリーを表示 (テストをpassしたもの以外)
pytest -rA # サマリーを表示 (テストをpassしたものも含む)
```

指定して実行  
(テストファイル名, パッケージ名, テストクラス名, メソッド名, 割と何でも拾ってくれる。部分一致でも。)

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

マーカーを指定して実行

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

カバレッジレポートも作成

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=main --cov-report=xml --cov-report=term-missing .
# もしくは
make ut
```

VSCodeでコードカバレッジを見るにはプラグイン(Coverage Gutters)が必要(導入済み)。表示されない場合は、コマンドパレットで`Coverage Gutters: Display Coverage`する。


### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./main
# もしくは
make lint
```

### 依存パッケージの追加方法

1. `requirements.txt`に追記
1. `Rebuild Container`

注意：`pip install`で追加すると下記警告が出る場合がある。`--upgrade`すると`bin`以下が消えて既に導入済みのパッケージが使えなくなる。このため上記手順が無難。

```zsh
WARNING: Target directory /home/../. already exists. Specify --upgrade to force replacement.
```

## 参考

- [【2020年1月】令和だし本格的にVSCodeのRemote Containerで、爆速の"開発コンテナ"始めよう - Qiita](https://qiita.com/koinori/items/084a0770c1f9e72e0c14)
- [VSCode Remote Containersに自分のdotfilesを持ち込む - Kesinの知見置き場](https://kesin.hatenablog.com/entry/2020/07/10/083000)
    - Remote Container拡張の設定でdotfilesをコピーする機能があるが使ってない
    - Dockerfileで`COPY`している
- [Configuration — pytest documentation](https://docs.pytest.org/en/6.2.x/customize.html)
- [Usage and Invocations — pytest documentation](https://docs.pytest.org/en/6.2.x/usage.html)
- [VSCodeでカバレッジを表示する（pytest-cov）](https://zenn.dev/tyoyo/articles/769df4b7eb9398)
