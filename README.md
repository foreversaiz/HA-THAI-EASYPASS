HOME ASSUSTANT THAI EASYPASS

![alt text](https://github.com/foreversaiz/HA-THAI-EASYPASS/blob/main/show.png)

ดึงยอดเงินคงเหลือของบัตร Easypass ครับ จากเดิม คุณ wit จาก line group เขียนเป็น python ผมเลยนำมาแปลงเป็น custom_component ครับ


<p><a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=foreversaiz&amp;repository=HA-THAI-EASYPASS&amp;category=integration" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Open your Home Assistant instance and open a repository inside the Home Assistant Community Store."></a></p>


เพิ่ม configuration ที่ configuration.yaml
```
sensor:
  - platform: easypass
    name: "easypass_balance"
    offset: "1"
    username: "user@gmail.com"
    password: "password"
    scan_interval: 300
```

offset คืออันดับของการ์ดที่มี ถ้ามีอันเดียวให้ใส่ 1 แต่กรณีมีหลายอันให้ใส่แบบนี้
```
sensor:
  - platform: easypass
    name: "easypass_balance_1"
    offset: "1"
    username: "user@gmail.com"
    password: "password"
    scan_interval: 300
    name: "easypass_balance_2"
    offset: "2"
    username: "user@gmail.com"
    password: "password"
    scan_interval: 300
```
ด้วยวิธีด้านบนจะได้ entity 2 ตัว
