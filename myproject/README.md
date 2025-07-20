# Multi-API Logging System with Docker Compose

ระบบนี้ประกอบด้วย API 2 ตัว: API1 และ API2  
API1 รับ request จาก user แล้วเรียก API2 ต่อ และส่งผลลัพธ์กลับมา  
ทั้งสอง API มีระบบ logging แสดงรายละเอียด request

## การใช้งาน

1. clone หรือดาวน์โหลด repo นี้

2. เข้าโฟลเดอร์ project

```bash
cd myproject
