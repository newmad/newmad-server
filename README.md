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
| reponse example | "{\"data\": [\"안개\", \"폭염\", \"폭우\", \"폭설\", \"폭풍\", \"미세먼지\", \"맑음\", \"혹한\", \"강풍\", \"뇌우\", \"혹한\", \"화창한날\", \"보슬비 내리는 날\"]}" |

## 

| 이름            | Place                                                        |
| --------------- | ------------------------------------------------------------ |
| 역할            | 장소 출력                                                    |
| Method          | GET                                                          |
| URI             | /place or /place/<key>                                       |
| reponse example | "{\"오설록티뮤지엄\": {\"address\": \"제주특별자치시 서귀포시 안덕면 1234-12\", \"category\": \"일반음식점\", \"desc\": \"오설록 티뮤지엄 짱이에요!!!\", \"holiday\": \"매주 일요일 휴무\", \"id\": 1, \"img\": \"https://firebasestorage.googleapis.com/v0/b/madjoy-9e80b.appspot.com/o/5253258529_e07cb5db5c_b.jpg?alt=media&token=a7f96a6b-3006-436e-b1f0-ab3403acadcf\", \"like\": 26, \"parking\": \"주차 완비\", \"phone\": \"064-794-5321\", \"price\": \"아메리카노:6000,제주감귤차:7000\", \"title\": \"오설록티뮤지엄\", \"weather-id\": 1}, \"주상절리9\": {\"address\": \"제주특별자치도 서귀포시 이어도로 36-30\", \"category\": \"명소\", \"desc\": \"주상절리 멋있네요\", \"holiday\": \"없음\", \"id\": 11, \"img\": \"https://firebasestorage.googleapis.com/v0/b/madjoy-9e80b.appspot.com/o/jusangjeolli-725186_960_720.jpg?alt=media&token=81d485ea-25b7-4d55-8714-7f2d2f960e22\", \"like\": 24, \"parking\": \"주차 완비\", \"phone\": \"064-760-6351\", \"price\": \"입장료:2000\", \"title\": \"주상절리\", \"weather-id\": 6}}" |

## 

| 이름            | Search                                                       |
| --------------- | ------------------------------------------------------------ |
| 역할            | 장소 검색                                                    |
| Method          | GET                                                          |
| URI             | /search?keyword=오설록                                       |
| reponse example | "{\"오설록티뮤지엄\": {\"address\": \"제주특별자치시 서귀포시 안덕면 1234-12\", \"category\": \"일반음식점\", \"desc\": \"오설록 티뮤지엄 짱이에요!!!\", \"holiday\": \"매주 일요일 휴무\", \"id\": 1, \"img\": \"https://firebasestorage.googleapis.com/v0/b/madjoy-9e80b.appspot.com/o/5253258529_e07cb5db5c_b.jpg?alt=media&token=a7f96a6b-3006-436e-b1f0-ab3403acadcf\", \"like\": 26, \"parking\": \"주차 완비\", \"phone\": \"064-794-5321\", \"price\": \"아메리카노:6000,제주감귤차:7000\", \"title\": \"오설록티뮤지엄\", \"weather-id\": 1}}" |

## 

| 이름            | SearchById                                                    |
| --------------- | ------------------------------------------------------------ |
| 역할            | 장소 검색                                                       |
| Method          | GET                                                          |
| URI             | /searchid?keyword=1                                          |
| reponse example | "{\"오설록티뮤지엄\": {\"address\": \"제주특별자치시 서귀포시 안덕면 1234-12\", \"category\": \"일반음식점\", \"desc\": \"오설록 티뮤지엄 짱이에요!!!\", \"holiday\": \"매주 일요일 휴무\", \"id\": 1, \"img\": \"https://firebasestorage.googleapis.com/v0/b/madjoy-9e80b.appspot.com/o/5253258529_e07cb5db5c_b.jpg?alt=media&token=a7f96a6b-3006-436e-b1f0-ab3403acadcf\", \"like\": 26, \"parking\": \"주차 완비\", \"phone\": \"064-794-5321\", \"price\": \"아메리카노:6000,제주감귤차:7000\", \"title\": \"오설록티뮤지엄\", \"weather-id\": 1}}" |

