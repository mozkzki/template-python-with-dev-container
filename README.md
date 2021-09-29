# template-python-with-dev-container

- Python開発用テンプレート
  - Dockerコンテナでの開発版
  - VSCode Remote Containerの使用を想定
    - 設定ファイル: `.devcontainer/devcontainer.json`
  - Pythonの仮想環境 (PoetryとかPipenvとか)は使わない

| ツール種類 | ツール名 |
|--|--|
| パッケージ管理 | [pip](https://kurozumi.github.io/pip/index.html) |
| テストフレームワーク | [pytest](https://docs.pytest.org/en/6.2.x/) |
| リンター | [flake8](https://flake8.pycqa.org/en/latest/) |
| フォーマッター | [black](https://github.com/psf/black) |
| 型チェック | [mypy](https://mypy.readthedocs.io/en/stable/) |

なお、devcontainerはMSの[これ](https://github.com/microsoft/vscode-dev-containers/tree/v0.191.0/containers/python-3)がベース。

## 開発環境

### 導入

1. VSCodeに機能拡張「Remote - Containers」をインストール
1. `git clone git@github.com:mozkzki/template-python-with-dev-container.git hoge` (※hogeはチェックアウト先ディレクトリ)
1. このプロジェクトを開く
1. VSCodeの画面左下の緑ゾーンをクリック
1. `Reopen in Container`をクリック
1. コンテナ内でVSCodeが開いたら準備完了 (初回はビルドがあるので時間かかる)

### Shell

- zsh, preztoセットアップ済み
- プロンプトでpowerlevel10kを使う場合は下記で設定する

```zsh
prompt -s powerlevel10k
p10k configure
```

### dotfiles

- 下記を配置済み
  - https://github.com/mozkzki/settings/tree/master/devcontainer/dotfiles

## 開発方法

※ 以降のコマンドは、devcontainer (Dockerコンテナ) を起動し、そこで実行

### とりあえず一通り動確したい時

```sh
make lint
make ut
make start
```

### 実行

```sh
python ./main/my/app.py
# もしくは
make start
```

※ Poetryはタスクランナー機能がないのでmakeで代用

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

VSCodeでコードカバレッジを見るには、Coverage Gutters (プラグイン) を入れる。表示されない場合は、コマンドパレットで`Coverage Gutters: Display Coverage`する。

- [VSCodeでカバレッジを表示する（pytest-cov）](https://zenn.dev/tyoyo/articles/769df4b7eb9398)

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./main
# もしくは
make lint
```

### 依存パッケージ追加

下記ファイルに追記して`Rebuild Container`する。

- `requirements.txt`

`pip install`で追加すると下記の警告が出る場合がある。`--upgrade`すると`bin`以下が消えて既に導入済みのパッケージが使えなくなる。このため上記手順が無難。

```zsh
WARNING: Target directory /home/../. already exists. Specify --upgrade to force replacement.
```

## 参考

- [【2020年1月】令和だし本格的にVSCodeのRemote Containerで、爆速の"開発コンテナ"始めよう - Qiita](https://qiita.com/koinori/items/084a0770c1f9e72e0c14)
- [VSCode Remote Containersに自分のdotfilesを持ち込む - Kesinの知見置き場](https://kesin.hatenablog.com/entry/2020/07/10/083000)
  - Remote Container拡張の設定でdotfilesをコピーする機能があるが使ってない
  - Dockerfileで`git clone`している
- [Configuration — pytest documentation](https://docs.pytest.org/en/6.2.x/customize.html)
- [Usage and Invocations — pytest documentation](https://docs.pytest.org/en/6.2.x/usage.html)
