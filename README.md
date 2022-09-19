# アミノ酸コドン統計
アミノ酸のコドンを統計するプログラムです。  

このプログラムは[National Library of Medicine](https://www.ncbi.nlm.nih.gov/nuccore/) からダウンロードした塩基配列の記録であるCoding Sequenceのtxtファイルを読み込んで、塩基配列を三つ組塩基（コドン）に分かれる。ファイルの中のすべてのコドンがどのアミノ酸に対応するのかを判断し、コドンごとの対応するアミノ酸に含まれる割合を計算する仕組みです。

line4 ```f = open("")``` のところで読み込むファイル名を入力。

***コドン表の例***  

![コドン表の例](https://www.toho-u.ac.jp/sci/biomol/glossary/bio/j5mt8h000000dkv7-img/codon.jpg)
