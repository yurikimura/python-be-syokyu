# 環境構築

## 概要

Python Railway の問題を解くために必要な下記ツールのインストール方法と環境構築の手順を解説します。
- Python 3.12
- Docker
- Visual Studio Code
- Git

上記のうち、Visual Studio Code と Git についてのインストール方法は、
[Railway 準備編](https://www.notion.so/techbowl/Railway-ceba695d5014460e9733c2a46318cdec) をご確認いただき、挑戦の準備をしてください。

その他リポジトリの更新の仕方や、トラブルシューティングについても上記の Railway 準備編にございます。
何かあった際は、まずそちらを確認しましょう。

## 手順
1. Pythonのインストール
    1. Mac ユーザーの場合、 Homebrew でインストールを行います。
       1. `brew install python@3.12`
    2. インストール実行が正常に完了後、ターミナルで以下コマンドを実行し、バージョンが正常に表示されればインストールが行えています。
       1. `python3.12 -V`
2. Docker Desktopのインストール
    - 自身のMacに搭載されているCPUを確認し、[Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/) からDocker Desktopをダウンロードし、インストールします。
    - Docker Desktopをインストールした後、一度PCを再起動してからDocker Desktopを起動してください。
    - これにより、Dockerが正しく動作するか確認できます。
3. Visual Studio Codeのインストール
    - [Visual Studio Code](https://code.visualstudio.com/) から自分のOSに適したVisual Studio Codeをダウンロードします。
4. Visual Studio CodeにTechTrain Railwayのクリア条件を判定するツールをインストール
    - Visual Studio Codeを開き、拡張機能 ( Extensions ) から「TechTrain Railway」という拡張機能を検索してインストールします。これにより、Railwayのクリア条件を簡単に判定できるようになります。
    ![TechTrain Railwayの拡張機能をインストール](./images/install-extensions.gif)
5. GitHubリポジトリのフォークとダウンロード
    1. GitHubリポジトリのフォーク
        - [TechBowl-japan/python-stations4 | GitHub](https://github.com/TechBowl-japan/python-stations4) にアクセスし、右上の"Fork"ボタンをクリックして、リポジトリを自分のGitHubアカウントにフォークします。
        ※以下動画は今回フォークするものとは異なるリポジトリの表示になっていますが、操作手順は同じになりますので、気にせず進めてください。
        ![GitHubリポジトリのフォーク](./images/fork-repository.gif)
    2. Gitのインストール
        - GitHubからリポジトリをクローンするためには、Gitが必要です。
        - インストールされていない場合は、[Gitの公式サイト](https://git-scm.com/download/mac) で提示された選択肢から1つ選び、ダウンロードします。
    3. GitHubリポジトリのダウンロード
        - フォークが完了したら、自分のGitHubアカウント上でフォークされたリポジトリを選択し、"Code"ボタンをクリックして、リポジトリのURLをコピーします。
        - そして、ターミナルを開いて以下のコマンドを実行してリポジトリをダウンロードします。
        ```bash
        git clone https://github.com/{{あなたのGitHubID}}/python-stations4.git
        ```
6. Visual Studio Code (略して VSCode と呼びます。) でダウンロードしたリポジトリを開く
    - リポジトリをダウンロードしたディレクトリで右クリックし、"Open with Code"または"Visual Studio Code で開く"を選択します。
    - または、コマンドラインで以下のコマンドを実行して、リポジトリのディレクトリをVisual Studio Codeで開きます。
    ```bash
    code ダウンロードしたリポジトリのディレクトリ
    ```
    - Visual Studio Codeが起動したら、左上のファイル -> フォルダを開くを選択して、ダウンロードしたリポジトリのディレクトリを選択します。
7. ローカルPython環境の仮想環境を作成し、VSCodeで開いているプロジェクトに適用する。
    - VSCodeでコードを編集する際は、ローカル環境上となり、VSCodeの構文解析等を有効に働かせるためにローカル環境でもPython環境を準備します。
    - リポジトリをVSCodeで開いた後、VSCode上でターミナルを開くとプロジェクト直下をカレントディレクトリとしてターミナルが開きます。
    - その状態で以下コマンドを実行します。
        ```bash
        python3.12 -m venv .venv
        ```
        このコマンドを実行すると、プロジェクト直下に `.venv` ディレクトリが作成されます。
    - VSCodeにて 「 Cmd + Shift + P 」 でVSCodeのコマンドパレットを開きます。コマンドパレットにて 「 `Python: インタープリターを選択` 」を選択します。

        以下のように途中まで入力すると選択肢が絞られていって見つけやすくなると思います。
        ![](./images/vscode_select_python_interpreter.png)
    - 選択後、インタープリターの一覧が表示されますが、以下の`./.venv/bin/python` がパスとして表示されているものを選択してください。
        ![](./images/vscode_python_interpreter_list.png)
    - 上記で対応完了となります。現在どこのPythonインタープリターが選択されているかは、VSCodeで`.py`ファイルを開くと、VSCodeのウィンドウ最下部に表示されます。
        ![](./images/vscode_current_python_interpreter.png)
    - また、`.venv`配下のPythonインタープリターを選択していると、VSCode上でターミナルを新規で開いた時に予めターミナル上でもvenvの仮想環境が有効になった状態でターミナルが起動されます。
    ![](./images/vscode_terminal_with_venv.png)
8. 利用するPythonパッケージをPython仮想環境配下にインストール
    - 上記の手順にて VSCodeのターミナルで venvが有効になっている状態で立ち上がる旨説明しました。
    - venvが有効かされている状態のターミナルで以下を実行し、仮想環境下で必要なPythonパッケージをインストールします。
        ```bash
        pip install -r ./infra/docker/app/requirements/dev.txt
        ```
9.  Visual Studio Codeからターミナルを起動しアプリケーションの実行環境を構築する
    - 左上のターミナル -> 新しいターミナルを選択して、ターミナルを起動します。
    - 以下のコマンドを実行し、アプリケーションの環境固有 ( データベースへの接続情報等 ) の設定や機密情報を格納する `.env` ファイルを作成します。
    ```bash
    cp .env.example .env
    ```
    - 以下のコマンドを実行し、Dockerコンテナのビルドを行います。
    ```bash
    docker compose build --no-cache
    ```
    ※ Dockerコンテナのビルドおよび起動には時間がかかる場合があります。コマンドが正常に完了するまで待ってください。
10. Dockerコマンドでコンテナを起動
    - ターミナルでリポジトリのディレクトリに移動し、以下のコマンドを実行してDockerコンテナを起動します。
    ```bash
    docker compose up -d
    ```
    ※ Dockerコンテナのビルドおよび起動には時間がかかる場合があります。コマンドが正常に完了するまで待ってください。
11. Dockerコマンドでコンテナの起動を確認
    - 以下のコマンドを実行し、手順7.で起動したDockerコンテナのプロセスが起動しているかを確認してください。
    ```bash
    docker compose ps
    ```
    ※ Dockerが使用するポートが他のアプリケーションと競合していないか確認してください。
12. ローカルサーバが立ち上がっていることを確認
    - [http://localhost:18008/docs](http://localhost:18008/docs) にアクセスし、ローカルサーバが立ち上がっていることを確認します。
13. 環境構築完了後の確認
    - 環境構築が正常に終了したことを確認するために、Visual Studio Codeでリポジトリを開いてから、ファイルの変更や追加ができるか確認してください。
    - また、TechTrain Railwayの拡張機能が正しく機能しているかも確認してください。
---
以上でPython Backend Railwayに取り組むための環境が整いました。
Visual Studio Codeを使用してコードを編集し、「TechTrain Railway」という拡張機能から「できた!」と書かれた青いボタンをクリックすると判定が始まります。
