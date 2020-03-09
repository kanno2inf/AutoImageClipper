# Auto Image Clipper

指定サイズに縮小、クリッピングした画像を生成します
Clusterのワールドサムネ画像など

## トリミングの仕様

2048x1080 -> 1920x1080

画像を中心として両端の余分なピクセルを削除してトリミングします

## 保存ファイル名

ファイル名末尾に`-trim`を付けて保存します

image.png -> image-trim.png

同一ファイル名があった場合上書きします

## 使い方
* Python 3.8.x をインストール
* 必要パッケージをインストール
```bash
$ pip install -r requirements.txt
```

## コマンド
```
# 指定した画像を変換して保存します
$ python auto_clip.py image.png

# サイズ指定も可能
$ python auto_clip.py image.png -W 1920 -H 1080
```

### Windows専用bat
auto_clip.batに画像をドラック&ドロップするだけ

## コマンドヘルプ
```bash
$ python auto_clip.py -h
usage: auto_clip.py [-h] [-W WIDTH] [-H HEIGHT] image_path

positional arguments:
  image_path

optional arguments:
  -h, --help            show this help message and exit
  -W WIDTH, --width WIDTH
  -H HEIGHT, --height HEIGHT
```