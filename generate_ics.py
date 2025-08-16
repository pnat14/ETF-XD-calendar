import os

ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//ETF XD Calendar//EN
BEGIN:VEVENT
SUMMARY:QQQI XD Date
DTSTART;VALUE=DATE:20250910
DESCRIPTION:Estimated ex-dividend date for QQQI
END:VEVENT
BEGIN:VEVENT
SUMMARY:SPYI XD Date
DTSTART;VALUE=DATE:20250912
DESCRIPTION:Estimated ex-dividend date for SPYI
END:VEVENT
BEGIN:VEVENT
SUMMARY:JEPQ XD Date
DTSTART;VALUE=DATE:20250914
DESCRIPTION:Estimated ex-dividend date for JEPQ
END:VEVENT
BEGIN:VEVENT
SUMMARY:MSTY XD Date
DTSTART;VALUE=DATE:20250916
DESCRIPTION:Estimated ex-dividend date for MSTY
END:VEVENT
END:VCALENDAR
"""

# ✅ สร้างโฟลเดอร์ public ถ้ายังไม่มี
os.makedirs("public", exist_ok=True)

# ✅ สร้างไฟล์ .ics ข้างใน public
with open("public/xd_calendar.ics", "w") as f:
    f.write(ics_content)

print("ICS file generated at public/xd_calendar.ics")

