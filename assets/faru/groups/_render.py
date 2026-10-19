"""Phone frames for the public FARU Groups pages (current copy, not DD)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 390, 844
BG = (20, 18, 24)
CARD = (32, 30, 38)
FG = (244, 246, 251)
MUTED = (139, 147, 167)
CYAN = (0, 229, 255)
GREEN = (110, 231, 160)
LINE = (40, 42, 52)
OUT = Path(__file__).resolve().parent


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for name in (
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded(draw: ImageDraw.ImageDraw, xy, r, fill, outline=None):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline)


def chip(draw, xy, text, fill=CYAN, fg=(7, 8, 12)):
    x1, y1, x2, y2 = xy
    rounded(draw, xy, 99, fill)
    f = font(13, True)
    tw = draw.textlength(text, font=f)
    draw.text(((x1 + x2 - tw) / 2, y1 + 6), text, fill=fg, font=f)


def status(draw):
    draw.text((20, 12), "9:41", fill=FG, font=font(13, True))
    draw.text((330, 12), "FARU", fill=CYAN, font=font(13, True))


def tabbar(draw, y=790):
    labels = ["Home", "Browse", "Clubs", "Inbox", "More"]
    for i, lab in enumerate(labels):
        x = 18 + i * 74
        col = CYAN if lab == "Clubs" else MUTED
        draw.text((x, y), lab, fill=col, font=font(12, lab == "Clubs"))


def save(im: Image.Image, name: str):
    path = OUT / name
    im.save(path, "PNG", optimize=True)
    print(f"  wrote {path.name}")


def hub():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Home game send-off", fill=FG, font=font(22, True))
    d.text((20, 76), "Outing Club  ·  JQH Arena", fill=MUTED, font=font(13))
    d.text((20, 100), "Arrive 6:30–7:15  ·  Leave 10:00–11:30", fill=CYAN, font=font(13, True))
    rounded(d, (16, 136, 374, 230), 16, CARD)
    d.text((32, 152), "Tonight for members", fill=MUTED, font=font(12))
    d.text((32, 172), "Need a ride or have seats?", fill=FG, font=font(16, True))
    d.text((32, 198), "Listings stay on this hub — club only.", fill=MUTED, font=font(12))
    chip(d, (20, 250, 186, 292), "I have seats")
    chip(d, (202, 250, 370, 292), "I need a ride", fill=(40, 42, 52), fg=FG)
    rounded(d, (16, 312, 374, 430), 16, CARD)
    d.text((32, 328), "Open seats", fill=MUTED, font=font(12))
    d.text((32, 350), "Maya  ·  3 seats  ·  PSU loop", fill=FG, font=font(15, True))
    d.text((32, 376), "Jordan  ·  2 seats  ·  after overtime", fill=FG, font=font(15, True))
    d.text((32, 402), "QR at the door so members can post fast.", fill=MUTED, font=font(12))
    rounded(d, (16, 450, 374, 560), 16, CARD)
    d.text((32, 466), "Ride needs", fill=MUTED, font=font(12))
    d.text((32, 488), "Sam  ·  dorm after the game", fill=FG, font=font(15, True))
    d.text((32, 514), "Riley  ·  walking is not an option tonight", fill=FG, font=font(15, True))
    d.text((32, 540), "Still-out counts need-a-ride only.", fill=MUTED, font=font(12))
    tabbar(d)
    save(im, "hub-home-game.png")


def command():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Command", fill=FG, font=font(22, True))
    d.text((20, 76), "Outing Club  ·  Groups Pro", fill=MUTED, font=font(13))
    rounded(d, (16, 108, 186, 188), 14, CARD)
    rounded(d, (202, 108, 374, 188), 14, CARD)
    d.text((28, 120), "Still out", fill=MUTED, font=font(12))
    d.text((28, 140), "4", fill=CYAN, font=font(28, True))
    d.text((28, 174), "need a ride", fill=MUTED, font=font(11))
    d.text((214, 120), "Drivers on duty", fill=MUTED, font=font(12))
    d.text((214, 140), "1 / 2", fill=GREEN, font=font(28, True))
    d.text((214, 174), "coverage short", fill=MUTED, font=font(11))
    rounded(d, (16, 204, 374, 318), 16, CARD)
    d.text((32, 218), "Tonight — Command board", fill=FG, font=font(15, True))
    d.text((32, 244), "Seats open  6   ·   Needs  5", fill=MUTED, font=font(13))
    d.text((32, 268), "Leave wave 2  10:45", fill=MUTED, font=font(13))
    d.text((32, 292), "Rain plan ready  ·  venue + ping", fill=CYAN, font=font(13))
    rounded(d, (16, 334, 374, 520), 16, CARD)
    d.text((32, 348), "Still out", fill=MUTED, font=font(12))
    for i, (name, note) in enumerate(
        (
            ("Sam", "Need a ride home"),
            ("Riley", "Need a ride home"),
            ("Chris", "Need a ride home"),
            ("Avery", "Need a ride home"),
        )
    ):
        y = 374 + i * 34
        d.text((32, y), name, fill=FG, font=font(14, True))
        d.text((130, y), note, fill=MUTED, font=font(12))
        d.text((300, y), "In", fill=CYAN, font=font(13, True))
    rounded(d, (16, 536, 374, 640), 16, CARD)
    d.text((32, 552), "Run this hub", fill=MUTED, font=font(12))
    d.text((32, 574), "Fill leftover seats  ·  Remind", fill=FG, font=font(14, True))
    d.text((32, 600), "Assign Driver on Duty  ·  QR", fill=FG, font=font(14, True))
    d.text((32, 624), "Officers expand this. Members do not.", fill=MUTED, font=font(12))
    tabbar(d)
    save(im, "command-board.png")


def checkin():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Check in", fill=FG, font=font(22, True))
    d.text((20, 76), "How are you leaving tonight?", fill=MUTED, font=font(14))
    options = (
        ("Need a ride home", "You stay on the still-out list"),
        ("Walking home", "Roster only — not still-out"),
        ("Driving alone", "Roster only — not still-out"),
        ("Driving · can take others", "Opens I have seats on this hub"),
    )
    for i, (title, sub) in enumerate(options):
        y = 120 + i * 110
        rounded(d, (16, y, 374, y + 98), 16, CARD, outline=CYAN if i == 0 else None)
        d.text((32, y + 18), title, fill=FG, font=font(16, True))
        d.text((32, y + 50), sub, fill=MUTED, font=font(13))
    tabbar(d)
    save(im, "checkin-leave.png")


def tonight():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Tonight", fill=FG, font=font(22, True))
    d.text((20, 76), "Your card — no officer gap numbers", fill=MUTED, font=font(13))
    rounded(d, (16, 116, 374, 360), 16, CARD)
    d.text((32, 136), "Home game send-off", fill=FG, font=font(18, True))
    d.text((32, 168), "JQH Arena", fill=MUTED, font=font(14))
    d.text((32, 200), "Arrive 6:30  ·  Leave 10:00", fill=CYAN, font=font(14, True))
    d.text((32, 232), "Show this QR at the door", fill=MUTED, font=font(13))
    rounded(d, (130, 258, 260, 338), 12, (10, 10, 14), outline=CYAN)
    d.text((156, 286), "QR", fill=CYAN, font=font(22, True))
    chip(d, (20, 380, 370, 426), "Check in")
    rounded(d, (16, 446, 374, 560), 16, CARD)
    d.text((32, 462), "Your seat", fill=MUTED, font=font(12))
    d.text((32, 484), "Maya’s car  ·  1 of 3 seats", fill=FG, font=font(16, True))
    d.text((32, 516), "Pickup PSU loop after the game", fill=MUTED, font=font(13))
    tabbar(d)
    save(im, "member-tonight.png")


def groups_plan():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "FARU Groups", fill=FG, font=font(22, True))
    d.text((20, 76), "$9.99/mo  ·  billed to the club", fill=MUTED, font=font(13))
    rounded(d, (16, 110, 374, 250), 16, CARD)
    d.text((32, 126), "What the club unlocks", fill=MUTED, font=font(12))
    d.text((32, 150), "Event ride hubs", fill=FG, font=font(15, True))
    d.text((32, 174), "Arrive and leave windows", fill=FG, font=font(15, True))
    d.text((32, 198), "QR page for seats or needs", fill=FG, font=font(15, True))
    d.text((32, 222), "Club-owned ride series", fill=FG, font=font(15, True))
    rounded(d, (16, 268, 374, 380), 16, CARD)
    d.text((32, 286), "Members still ride free", fill=FG, font=font(15, True))
    d.text((32, 316), "Post seats, request a ride, and", fill=MUTED, font=font(13))
    d.text((32, 338), "join a sober-ride network — no", fill=MUTED, font=font(13))
    d.text((32, 360), "student membership required.", fill=MUTED, font=font(13))
    chip(d, (20, 404, 370, 450), "Start FARU Groups  ·  $9.99/mo")
    chip(d, (20, 466, 370, 512), "See Groups Pro  ·  $24.99/mo", fill=(40, 42, 52), fg=FG)
    tabbar(d)
    save(im, "groups-plan.png")


def groups_pro_plan():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Groups Pro", fill=FG, font=font(22, True))
    d.text((20, 76), "$24.99/mo  ·  billed to the club", fill=MUTED, font=font(13))
    rounded(d, (16, 110, 186, 190), 14, CARD)
    rounded(d, (202, 110, 374, 190), 14, CARD)
    d.text((28, 122), "Hubs", fill=MUTED, font=font(12))
    d.text((28, 144), "3", fill=CYAN, font=font(26, True))
    d.text((214, 122), "Coverage", fill=MUTED, font=font(12))
    d.text((214, 144), "On", fill=GREEN, font=font(26, True))
    rounded(d, (16, 208, 374, 430), 16, CARD)
    d.text((32, 224), "Officer tools", fill=MUTED, font=font(12))
    for i, line in enumerate(
        (
            "Command board + still-out",
            "24h / 2h reminders",
            "Driver on Duty nights",
            "Waitlist, pin, leave waves",
            "Advisor digest + campus packet",
        )
    ):
        d.text((32, 250 + i * 32), line, fill=FG, font=font(15, True))
    chip(d, (20, 454, 370, 500), "Open Command")
    tabbar(d)
    save(im, "groups-pro-plan.png")


def series():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Ride series", fill=FG, font=font(22, True))
    d.text((20, 76), "Outing Club  ·  club-owned weekly", fill=MUTED, font=font(13))
    rounded(d, (16, 116, 374, 280), 16, CARD)
    d.text((32, 132), "Friday trailheads", fill=FG, font=font(18, True))
    d.text((32, 166), "Every Friday  ·  4:00 PM", fill=CYAN, font=font(14, True))
    d.text((32, 196), "Campus lot → Busiek trailhead", fill=MUTED, font=font(13))
    d.text((32, 224), "3 seats this week  ·  1 need", fill=FG, font=font(14, True))
    d.text((32, 250), "Members see it on Clubs and Browse.", fill=MUTED, font=font(12))
    rounded(d, (16, 300, 374, 440), 16, CARD)
    d.text((32, 316), "This week’s posts", fill=MUTED, font=font(12))
    d.text((32, 342), "Alex  ·  2 seats  ·  after lab", fill=FG, font=font(15, True))
    d.text((32, 372), "Priya  ·  needs a seat  ·  dorm", fill=FG, font=font(15, True))
    d.text((32, 402), "Series keeps the post — not a thread.", fill=MUTED, font=font(12))
    chip(d, (20, 464, 186, 510), "I have seats")
    chip(d, (202, 464, 370, 510), "I need a ride", fill=(40, 42, 52), fg=FG)
    tabbar(d)
    save(im, "ride-series.png")


def joint():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Homecoming send-off", fill=FG, font=font(22, True))
    d.text((20, 76), "Outing + Dance  ·  joint hub", fill=MUTED, font=font(13))
    rounded(d, (16, 116, 374, 250), 16, CARD)
    d.text((32, 132), "Both clubs open this hub", fill=FG, font=font(16, True))
    d.text((32, 166), "Arrive 7:00–7:45  ·  Leave 11:30", fill=CYAN, font=font(13, True))
    d.text((32, 196), "Seats stay on the posting club.", fill=MUTED, font=font(13))
    d.text((32, 220), "Dance members see Outing’s night.", fill=MUTED, font=font(13))
    rounded(d, (16, 270, 374, 430), 16, CARD)
    d.text((32, 286), "Open tonight", fill=MUTED, font=font(12))
    d.text((32, 312), "Outing  ·  4 seats toward downtown", fill=FG, font=font(14, True))
    d.text((32, 344), "Dance  ·  2 seats after last set", fill=FG, font=font(14, True))
    d.text((32, 376), "Joint night. Separate listings.", fill=MUTED, font=font(13))
    d.text((32, 404), "Officers still run their own roster.", fill=MUTED, font=font(12))
    chip(d, (20, 454, 370, 500), "Open hub")
    tabbar(d)
    save(im, "joint-hub.png")


def qr():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Hub QR", fill=FG, font=font(22, True))
    d.text((20, 76), "Tape this at the door or table", fill=MUTED, font=font(13))
    rounded(d, (70, 120, 320, 370), 18, (10, 10, 14), outline=CYAN)
    d.text((148, 220), "QR", fill=CYAN, font=font(42, True))
    d.text((112, 280), "Scan to post", fill=MUTED, font=font(14))
    rounded(d, (16, 396, 374, 560), 16, CARD)
    d.text((32, 416), "Members land on this hub", fill=FG, font=font(16, True))
    d.text((32, 452), "I have seats  ·  I need a ride", fill=CYAN, font=font(14, True))
    d.text((32, 486), "No GroupMe scavenger hunt.", fill=MUTED, font=font(13))
    d.text((32, 514), "Listings stay club-only.", fill=MUTED, font=font(13))
    tabbar(d)
    save(im, "hub-qr.png")


def waves():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Leave waves", fill=FG, font=font(22, True))
    d.text((20, 76), "Pin  ·  waitlist  ·  two leave times", fill=MUTED, font=font(13))
    rounded(d, (16, 116, 374, 250), 16, CARD)
    d.text((32, 132), "Pinned  ·  Home game send-off", fill=CYAN, font=font(13, True))
    d.text((32, 162), "Wave 1   10:00   ·   6 seats", fill=FG, font=font(15, True))
    d.text((32, 192), "Wave 2   10:45   ·   3 seats", fill=FG, font=font(15, True))
    d.text((32, 222), "Waitlist  4  ·  notify when a seat opens", fill=MUTED, font=font(12))
    rounded(d, (16, 270, 374, 430), 16, CARD)
    d.text((32, 286), "Waitlist", fill=MUTED, font=font(12))
    d.text((32, 314), "Sam  ·  dorm  ·  wave 2 preferred", fill=FG, font=font(14, True))
    d.text((32, 346), "Chris  ·  any wave after overtime", fill=FG, font=font(14, True))
    d.text((32, 378), "Avery  ·  if a Driver on Duty is free", fill=FG, font=font(14, True))
    d.text((32, 406), "Officers fill leftover seats in one tap.", fill=MUTED, font=font(12))
    chip(d, (20, 454, 370, 500), "Fill leftover seats")
    tabbar(d)
    save(im, "leave-waves.png")


def duty():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Driver on Duty", fill=FG, font=font(22, True))
    d.text((20, 76), "Duty nights  ·  not Profile Designated Drivers", fill=MUTED, font=font(12))
    rounded(d, (16, 112, 374, 230), 16, CARD)
    d.text((32, 128), "Tonight’s target", fill=MUTED, font=font(12))
    d.text((32, 152), "1 of 2 signed  ·  coverage short", fill=FG, font=font(16, True))
    d.text((32, 186), "Assign from Command. Target stays.", fill=MUTED, font=font(13))
    rounded(d, (16, 250, 374, 470), 16, CARD)
    d.text((32, 266), "This week", fill=MUTED, font=font(12))
    d.text((32, 294), "Fri  ·  Jordan  ·  signed", fill=GREEN, font=font(15, True))
    d.text((32, 326), "Sat  ·  open slot", fill=CYAN, font=font(15, True))
    d.text((32, 358), "Sun  ·  Maya  ·  signed", fill=GREEN, font=font(15, True))
    d.text((32, 396), "Optional: attach a sober-ride", fill=MUTED, font=font(13))
    d.text((32, 420), "network from Profile. Separate layer.", fill=MUTED, font=font(13))
    d.text((32, 444), "Duty is a roster slot for the night.", fill=MUTED, font=font(12))
    chip(d, (20, 494, 370, 540), "Sign up for Saturday")
    tabbar(d)
    save(im, "duty-nights.png")


def digest():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Advisor digest", fill=FG, font=font(22, True))
    d.text((20, 76), "Read-only  ·  sent in-app, not email blast", fill=MUTED, font=font(12))
    rounded(d, (16, 112, 374, 560), 16, CARD)
    d.text((32, 130), "Outing Club  ·  this week", fill=CYAN, font=font(13, True))
    d.text((32, 162), "3 hubs  ·  14 seats  ·  9 needs", fill=FG, font=font(16, True))
    d.text((32, 198), "Driver-on-duty hours  6", fill=FG, font=font(15, True))
    d.text((32, 232), "Still-out closed  ·  0 open needs", fill=GREEN, font=font(14, True))
    d.text((32, 274), "Nights", fill=MUTED, font=font(12))
    d.text((32, 300), "Fri  Home game  ·  covered", fill=FG, font=font(14, True))
    d.text((32, 332), "Sat  Trailheads  ·  1 gap filled", fill=FG, font=font(14, True))
    d.text((32, 372), "Advisor sees roster and windows.", fill=MUTED, font=font(13))
    d.text((32, 400), "No silent email to the university.", fill=MUTED, font=font(13))
    d.text((32, 436), "Campus packet is export-only until", fill=MUTED, font=font(13))
    d.text((32, 460), "an officer taps Send to Student Affairs.", fill=MUTED, font=font(13))
    tabbar(d)
    save(im, "advisor-digest.png")


def packet():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Campus packet", fill=FG, font=font(22, True))
    d.text((20, 76), "Export  ·  officer tap only", fill=MUTED, font=font(13))
    rounded(d, (16, 112, 374, 500), 16, CARD)
    d.text((32, 130), "Outing Club  ·  social packet", fill=CYAN, font=font(13, True))
    d.text((32, 164), "Roster  ·  42 members", fill=FG, font=font(16, True))
    d.text((32, 200), "Sober monitors  ·  2 on duty", fill=FG, font=font(16, True))
    d.text((32, 236), "Windows  ·  arrive / leave listed", fill=FG, font=font(16, True))
    d.text((32, 280), "Not filed with the school.", fill=MUTED, font=font(13))
    d.text((32, 308), "FARU does not auto-email campus.", fill=MUTED, font=font(13))
    d.text((32, 348), "If a campus license stores a", fill=MUTED, font=font(13))
    d.text((32, 372), "Student Affairs inbox, officers can", fill=MUTED, font=font(13))
    d.text((32, 396), "tap Send. Nothing goes out silently.", fill=MUTED, font=font(13))
    chip(d, (28, 436, 362, 478), "Export PDF")
    tabbar(d)
    save(im, "campus-packet.png")


def council():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Council", fill=FG, font=font(22, True))
    d.text((20, 76), "Multi-club roll-up  ·  Groups Pro", fill=MUTED, font=font(13))
    rounded(d, (16, 112, 374, 230), 16, CARD)
    d.text((32, 128), "Tonight across member clubs", fill=MUTED, font=font(12))
    d.text((32, 152), "2 hubs live  ·  1 coverage short", fill=FG, font=font(16, True))
    d.text((32, 188), "Outing + Dance on the same board.", fill=MUTED, font=font(13))
    rounded(d, (16, 250, 374, 500), 16, CARD)
    d.text((32, 266), "Member clubs", fill=MUTED, font=font(12))
    d.text((32, 294), "Outing  ·  Home game  ·  4 still-out", fill=FG, font=font(14, True))
    d.text((32, 326), "Dance  ·  Formal  ·  covered", fill=GREEN, font=font(14, True))
    d.text((32, 366), "Council sees the night. Each club", fill=MUTED, font=font(13))
    d.text((32, 390), "still runs its own seats and duty.", fill=MUTED, font=font(13))
    d.text((32, 426), "Glance tiles open the hub —", fill=MUTED, font=font(13))
    d.text((32, 450), "not a wall of unlabeled numbers.", fill=MUTED, font=font(13))
    tabbar(d)
    save(im, "council.png")


def transition():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Officer transition", fill=FG, font=font(22, True))
    d.text((20, 76), "Pass the gavel without a lost folder", fill=MUTED, font=font(13))
    rounded(d, (16, 112, 374, 500), 16, CARD)
    d.text((32, 130), "Season pack", fill=MUTED, font=font(12))
    d.text((32, 156), "Term history  ·  Fall 2026", fill=FG, font=font(16, True))
    d.text((32, 192), "12 hubs  ·  4 series  ·  duty nights", fill=FG, font=font(14, True))
    d.text((32, 228), "Snapshots stay with the club.", fill=MUTED, font=font(13))
    d.text((32, 268), "Transfer", fill=MUTED, font=font(12))
    d.text((32, 294), "President  ·  Jordan → Avery", fill=CYAN, font=font(14, True))
    d.text((32, 326), "Event chair  ·  stays Maya", fill=FG, font=font(14, True))
    d.text((32, 358), "Ride chair  ·  open", fill=FG, font=font(14, True))
    d.text((32, 398), "Advisor stays read-only.", fill=MUTED, font=font(13))
    d.text((32, 426), "New officers inherit Command,", fill=MUTED, font=font(13))
    d.text((32, 450), "not a spreadsheet in someone’s DMs.", fill=MUTED, font=font(13))
    tabbar(d)
    save(im, "officer-transition.png")


def rain():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    status(d)
    d.text((20, 44), "Rain plan", fill=FG, font=font(22, True))
    d.text((20, 76), "Venue + leave + ping  ·  Groups Pro", fill=MUTED, font=font(13))
    rounded(d, (16, 116, 374, 290), 16, CARD)
    d.text((32, 134), "Home game send-off", fill=FG, font=font(16, True))
    d.text((32, 168), "Move pickup to PSU covered loop", fill=CYAN, font=font(14, True))
    d.text((32, 200), "Leave wave still 10:00 / 10:45", fill=MUTED, font=font(13))
    d.text((32, 232), "Ping tagged members now", fill=FG, font=font(14, True))
    d.text((32, 260), "Officers set it. Members see the new spot.", fill=MUTED, font=font(12))
    rounded(d, (16, 310, 374, 470), 16, CARD)
    d.text((32, 326), "Night close", fill=MUTED, font=font(12))
    d.text((32, 352), "Expire leftover needs", fill=FG, font=font(15, True))
    d.text((32, 384), "Snapshot the roster", fill=FG, font=font(15, True))
    d.text((32, 416), "Draft advisor digest", fill=FG, font=font(15, True))
    d.text((32, 448), "No silent school email on close.", fill=MUTED, font=font(12))
    chip(d, (20, 494, 370, 540), "Close the night")
    tabbar(d)
    save(im, "rain-plan.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    hub()
    command()
    checkin()
    tonight()
    groups_plan()
    groups_pro_plan()
    series()
    joint()
    qr()
    waves()
    duty()
    digest()
    packet()
    council()
    transition()
    rain()


if __name__ == "__main__":
    main()
