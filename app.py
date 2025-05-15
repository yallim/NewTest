import json
import html

with open('game-avalon-world.bytes', 'rb') as f:
    byte_data = f.read()

# cp949로 디코딩
decoded_str = html.unescape(byte_data.decode('cp949'))  # 또는 'euc-kr'

# JSON 파싱
json_data = json.loads(decoded_str)

print(json_data)

