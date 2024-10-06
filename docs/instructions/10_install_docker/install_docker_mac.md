# Docker Desktop セットアップ - Mac 編

この手順では macOS 環境下における `Docker Desktop` のインストール手順を説明しています。

## Docker Desktop インストール
1. 自身の Mac に搭載されている CPU を確認し、[Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/) から Docker Desktop をダウンロードし、インストールします。
    ![Docker Desktopをインストール](../../images/install-docker-desktop.gif)
2. Docker Desktop をインストールした後、一度PCを再起動してから Docker Desktop を起動してください。
3. これにより、 Docker が正しく動作するか確認できます。

## Docker　実行環境の準備
Docker をインストールしたら、続いて今回の Railway で利用する Docker 環境のセットアップを行います。

Docker では実行環境としてコンテナというものを用意します。

以下の手順にて、今回の Railway で使用する Docker コンテナを作成 ( コンテナをビルド ) します。

1.  Visual Studio Codeにて、今回の Railway で使用する、 Clone 済みのテンプレートリポジトリのフォルダを開きます。
2.  Visual Studio Codeからターミナルを起動しアプリケーション実行環境を構築します。
    1. 左上のターミナル -> 新しいターミナルを選択して、ターミナルを起動します。
    2. 以下のコマンドを実行し、アプリケーションの環境固有 ( データベースへの接続情報等 ) の設定や機密情報を格納する `.env` ファイルを作成します。
    ```bash
    cp .env.example .env
    ```
    3. 以下のコマンドを実行し、Dockerコンテナのビルドを行います。
    ```bash
    docker compose build --no-cache
    ```
   ※ Dockerコンテナのビルドおよび起動には時間がかかる場合があります。コマンドが正常に完了するまで待ってください。
