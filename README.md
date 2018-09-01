## API Specification

| 이름            | WeatherID                                                    |
| --------------- | ------------------------------------------------------------ |
| 역할            | 날씨 정보 출력                                               |
| Method          | GET                                                          |
| URI             | /weather                                                     |
| reponse example | "{\"coord\":{\"lon\":126.52,\"lat\":33.51},\"weather\":[{\"id\":500,\"main\":\"Rain\",\"description\":\"light rain\",\"icon\":\"10n\"}],\"base\":\"stations\",\"main\":{\"temp\":296.15,\"pressure\":1010,\"humidity\":88,\"temp_min\":296.15,\"temp_max\":296.15},\"visibility\":6000,\"wind\":{\"speed\":7.7,\"deg\":90},\"clouds\":{\"all\":90},\"dt\":1535808120,\"sys\":{\"type\":1,\"id\":7655,\"message\":0.005,\"country\":\"KR\",\"sunrise\":1535749678,\"sunset\":1535795954},\"id\":1846266,\"name\":\"Jeju\",\"cod\":200}" |

## 

| 이름            | WeatherList                                                  |
| --------------- | ------------------------------------------------------------ |
| 역할            | 날씨 종류 출력                                               |
| Method          | GET                                                          |
| URI             | /weatherlist                                                 |
| reponse example | {%"data%": [%"%안%개%", %"%폭%염%", %"%폭%우%", %"%폭%설%", %"%폭%풍%", %"%미%세%먼%지%", %"%맑%음%", %"%혹%한%", %"%강%풍%", %"%뇌%우%", %"%혹%한%", %"%화%창%한%날%", %"%보%슬%비 %내%리%는 %날%"]}" |

## 

| 이름            | Place                                                        |
| --------------- | ------------------------------------------------------------ |
| 역할            | 장소 출력                                                    |
| Method          | GET                                                          |
| URI             | /place or /place/<key>                                       |
| reponse example | "{%"%오%설%록%티%뮤%지%엄%": {%"address%": %"%제%주%특%별%자%치%시 %서%귀%포%시 %안%덕%면 1234-12%", %"category%": %"%일%반%음%식%점%", %"desc%": %"%오%설%록 %티%뮤%지%엄 %짱%이%에%요!!!%", %"holiday%": %"%매%주 %일%요%일 %휴%무%", %"id%": 1, %"img%": %"https://firebasestorage.googleapis.com/v0/b/madjoy-9e80b.appspot.com/o/5253258529_e07cb5db5c_b.jpg?alt=media&token=a7f96a6b-3006-436e-b1f0-ab3403acadcf%", %"like%": 29, %"parking%": %"%주%차 %완%비%", %"phone%": %"064-794-5321%", %"price%": %"%아%메%리%카%노:6000,%제%주%감%귤%차:7000%", %"title%": %"%오%설%록%티%뮤%지%엄%", %"weather-id%": 1}, %"%주%상%절%리%": {%"address%": %"%제%주%특%별%자%치%도 %서%귀%포%시 %이%어%도%로 36-30%", %"category%": %"%명%소%", %"desc%": %"%주%상%절%리 %멋%있%네%요%", %"holiday%": %"%없%음%", %"id%": 2, %"img%": %"https://firebasestorage.googleapis.com/v0/b/madjoy-9e80b.appspot.com/o/jusangjeolli-725186_960_720.jpg?alt=media&token=81d485ea-25b7-4d55-8714-7f2d2f960e22%", %"like%": 24, %"parking%": %"%주%차 %완%비%", %"phone%": %"064-760-6351%", %"price%": %"%입%장%료:2000%", %"title%": %"%주%상%절%리%", %"weather-id%": 6}}" |

## 

| 이름            | Search                                                       |
| --------------- | ------------------------------------------------------------ |
| 역할            | 장소 검색                                                    |
| Method          | POST body{keyword: \<location>}                              |
| URI             | /search                                                      |
| reponse example | "{%"%주%상%절%리%": {%"address%": %"%제%주%특%별%자%치%도 %서%귀%포%시 %이%어%도%로 36-30%", %"category%": %"%명%소%", %"desc%": %"%주%상%절%리 %멋%있%네%요%", %"holiday%": %"%없%음%", %"id%": 2, %"img%": %"https://firebasestorage.googleapis.com/v0/b/madjoy-9e80b.appspot.com/o/jusangjeolli-725186_960_720.jpg?alt=media&token=81d485ea-25b7-4d55-8714-7f2d2f960e22%", %"like%": 24, %"parking%": %"%주%차 %완%비%", %"phone%": %"064-760-6351%", %"price%": %"%입%장%료:2000%", %"title%": %"%주%상%절%리%", %"weather-id%": 6}}" |


