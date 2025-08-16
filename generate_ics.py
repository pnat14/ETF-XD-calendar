import yfinance as yf
from datetime import datetime

tickers = ["QQQI", "SPYI", "JEPQ", "MSTY"]

def create_ics(events):
    ics = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n"
    for ev in events:
        ics += "BEGIN:VEVENT\n"
        ics += f"SUMMARY:{ev['title']}\n"
        ics += f"DTSTART;VALUE=DATE:{ev['date']}\n"
        ics += f"DTEND;VALUE=DATE:{ev['date']}\n"
        ics += "BEGIN:VALARM\nTRIGGER:-P1D\nACTION:DISPLAY\nDESCRIPTION:Dividend Alert\nEND:VALARM\n"
        ics += "END:VEVENT\n"
    ics += "END:VCALENDAR\n"
    return ics

def fetch_events():
    events = []
    for t in tickers:
        data = yf.Ticker(t).dividends
        if not data.empty:
            last_date = data.index[-1].date()
            date_str = last_date.strftime("%Y%m%d")
            events.append({
                "title": f"{t} Ex-Dividend Date",
                "date": date_str
            })
    return events

if __name__ == "__main__":
    events = fetch_events()
    with open("public/xd_calendar.ics", "w") as f:
        f.write(ics_content)
    print("✅ ICS calendar generated: xd_calendar.ics")
