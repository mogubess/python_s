import io
import requests
import zipfile

# with open('/tmp/a.txt', 'w') as f:
#     f.write('test test')

# with open('/tmp/a.txt', 'r') as f:
#     print(f.read())

# 一時展開するストリームを生成して、文字列を操作している
f = io.StringIO()
# f = io.BytesIO()
f.write('string io test')
# f.write(b'string io test')
f.seek(0)

print(f.read())

# ファイルをメモリ上に一時展開する処理
url = ('http://www.nomadworks.co.jp/htmlsample/archive/win/sec2/'
       'info01.zip')

f = io.BytesIO()

r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('info01.html') as r:
        print(r.read().decode('shift-jis'))
