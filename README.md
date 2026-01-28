# 論文のテンプレート

## What's this?

[Typst](https://typst.app/)向けの論文のテンプレートです。
諸々の設定は[Overleaf](https://overleaf.com/)を模倣しています。

そもそも論文の形式は細かく定まっていないため、時と場合に応じて修正する必要はあると思います。
typstで論文を書き始めるブートストラップ的な何かだと思ってください。

## Typst

Typstを利用するには、次の手順を取ると簡単です(個人の感想):

1. [rustup](https://rust-lang.org/ja/tools/install/)でcargoをインストール
2. `cargo install --locked typst-cli`

## Font

以下のフォントをシステムにインストールしてください。
ただし、以下に示されていない同じフォントファミリのフォントはなるべくインストールしないでください。
例えば、Noto Sans CJK JP Boldがインストールされていると期待しない結果を得ます。

- Noto Serif CJK JP Regular
- Noto Sans CJK JP Medium
- Latin Modern Roman 10 Regular
- Latin Modern Roman 10 Bold
