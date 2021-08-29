# template-python-simple-with-dev-container

Python開発用テンプレート。VSCode Remote Container版 (Dockerが必要)。仮想環境は使わない。

| ツール種類 | ツール名 |
|--|--|
| パッケージ管理 | [pip](https://kurozumi.github.io/pip/index.html) |
| テストフレームワーク | [pytest](https://docs.pytest.org/en/6.2.x/) |
| リンター | [flake8](https://flake8.pycqa.org/en/latest/) |
| フォーマッター | [black](https://github.com/psf/black) |
| 型チェック | [mypy](https://mypy.readthedocs.io/en/stable/) |

なお、dev-containerはMSの[これ](https://github.com/microsoft/vscode-dev-containers/tree/v0.191.0/containers/python-3)がベース。

## 開発環境

### 導入

1. VSCodeに機能拡張「Remote - Containers」をインストール
1. `git clone git@github.com:mozkzki/template-python-simple-with-dev-container.git hoge` (※hogeはチェックアウト先ディレクトリ)
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

用途に応じて下記ファイルに追記。

- `requirements.txt`
- `test-requirements.txt`

## 参考

- [【2020年1月】令和だし本格的にVSCodeのRemote Containerで、爆速の"開発コンテナ"始めよう - Qiita](https://qiita.com/koinori/items/084a0770c1f9e72e0c14)
- [VSCode Remote Containersに自分のdotfilesを持ち込む - Kesinの知見置き場](https://kesin.hatenablog.com/entry/2020/07/10/083000)
  - Remote Container拡張の設定でdotfilesをコピーする機能があるが使ってない
  - Dockerfileで`git clone`している
- [Configuration — pytest documentation](https://docs.pytest.org/en/6.2.x/customize.html)
- [Usage and Invocations — pytest documentation](https://docs.pytest.org/en/6.2.x/usage.html)