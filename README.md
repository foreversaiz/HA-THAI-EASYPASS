# Custom Home Assistant Component for Thailand's Easy Pass Tollway

![หน้าจอ Home Assistant แสดงยอด Easy Pass](https://github.com/foreversaiz/HA-THAI-EASYPASS/blob/main/show.png)

Integration/Custom Component สำหรับ Home Assistant เพื่อดึงยอดจาก Easy Pass ดัดแปลงจากโค้ดของคุณ wit จาก LINE กลุ่ม


<p><a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=foreversaiz&amp;repository=HA-THAI-EASYPASS&amp;category=integration" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Open your Home Assistant instance and open a repository inside the Home Assistant Community Store."></a></p>

## วิธีการใช้งาน

เพิ่ม configuration ที่ `configuration.yaml`
```
sensor:
  - platform: easypass
    name: "easypass_balance"
    offset: "1"
    username: "user@gmail.com"
    password: "password"
    scan_interval: 300
```

`offset` คืออันดับของบัตรที่ดึงมาแสดงจากชื่อผู้ใช้-รหัสผ่านที่ให้ หากมีบัตรใบเดียวให้ใส่เป็น `"1"` เสมอ

หรือการตั้งค่ากรณีมีหลายใบ ซึ่งจะทำให้ได้ entity แยกกันสำหรับบัตรทั้งสองใบ

```
sensor:
  - platform: easypass
    name: "easypass_balance_1"
    offset: "1"
    username: "user@gmail.com"
    password: "password"
    scan_interval: 300
  - platform: easypass
    name: "easypass_balance_2"
    offset: "2"
    username: "user@gmail.com"
    password: "password"
    scan_interval: 300
```
