# MyProject - Two APIs with Logging and Docker Compose

## Overview
โปรเจกต์นี้ประกอบด้วย API 2 ตัว:
- **API1** รับคำขอจากผู้ใช้ที่พอร์ต 5050 (mapped จากพอร์ต 5000 ภายใน container)
- **API2** รับคำขอจาก API1 ที่พอร์ต 5001

API1 จะรับ request แล้วเรียก API2 ต่อ จากนั้นส่งผลลัพธ์กลับให้ผู้ใช้  
ทั้งสอง API มีการพิมพ์ log บน console เพื่อบอกสถานะการทำงาน

---

## การติดตั้งและใช้งาน

### ขั้นตอนที่ 1: เตรียมระบบ
- ติดตั้ง [Docker Desktop](https://www.docker.com/products/docker-desktop) และเปิดให้ทำงาน

### ขั้นตอนที่ 2: Clone โปรเจกต์
```bash
git clone https://github.com/your-username/myproject.git
cd myproject
