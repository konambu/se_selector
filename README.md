# SE Selector

ローカルで何度も使える、SE 比較ツールです。

## 起動

`E:\work\se_selector\se_selector.bat`

起動すると `http://127.0.0.1:8765/se_selector.html` を開きます。

## 想定用途

- `slash_a.mp3` / `slash_b.mp3`
- `hit_a.mp3` / `hit_b.mp3`
- `magic_left.wav` / `magic_right.wav`

のような A/B 比較用ファイルを並べて、聞き比べしながら残す方を選びます。

## 操作

- `フォルダを選ぶ`
  - 比較したい SE フォルダを選択
- `A を採用` / `B を採用`
  - 負けた方のファイルを削除
  - あわせて `*.import` も削除
- `Pool`
  - 両方とも `_pool` フォルダへ移動
- `Skip`
  - 今のペアを後回し

## ショートカット

- `Q`: A を再生
- `W`: B を再生
- `1`: A を採用
- `2`: B を採用
- `P`: Pool
- `S`: Skip
- `Space`: 停止

## お気に入り

一度フォルダを選んでから `今のフォルダをお気に入り登録` を押すと、
ブラウザ側にフォルダ権限つきで保存します。

次回からはお気に入りを押すだけで再オープンできます。

## 注意

- Chrome / Edge 系ブラウザ前提です
- ブラウザの File System Access API を使うので、最初だけ権限確認が出ます
- ペア認識は今のところ以下です
  - `_a / _b`
  - `-a / -b`
  - `_left / _right`
  - `-left / -right`
  - `_01 / _02`
