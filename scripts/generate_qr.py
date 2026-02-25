import qrcode
import os
from urllib.parse import quote

OUTPUT_DIR = "/Users/sunnyhaladker/repos/House of lani/assets/images/qr-codes"
UPI_ID = "8790935353-4@ybl"
PAYEE_NAME = "House of Lani"

plans = [
    # Pilates
    ("pilates-single-session", "Pilates Single Session", 1500),
    ("pilates-monthly", "Pilates Monthly Session", 11200),
    ("pilates-monthly-plus", "Pilates Monthly Plan Plus", 15600),
    ("pilates-extended", "Pilates Extended Plan", 26400),
    # Yoga
    ("yoga-single-session", "Yoga Single Session", 800),
    ("yoga-monthly", "Yoga Monthly Plan", 8400),
    ("yoga-monthly-plus", "Yoga Monthly Plan Plus", 13000),
    # Combos
    ("combo-1-month", "Combo 1 Month Plan", 22800),
    ("combo-3-month", "Combo 3 Month Plan", 63600),
    ("combo-6-month", "Combo 6 Month Plan", 100800),
    # Red Light Therapy
    ("rlt-single", "Red Light Therapy Single Session", 1100),
    ("rlt-5-sessions", "Red Light Therapy 5 Sessions", 4995),
    ("rlt-10-sessions", "Red Light Therapy 10 Sessions", 8990),
    # Compression Therapy
    ("compression-single", "Compression Therapy Single Session", 1400),
    ("compression-6-sessions", "Compression Therapy 6 Sessions", 7195),
    ("compression-12-sessions", "Compression Therapy 12 Sessions", 11999),
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename, description, amount in plans:
    upi_uri = (
        f"upi://pay?"
        f"pa={UPI_ID}"
        f"&pn={quote(PAYEE_NAME)}"
        f"&am={amount}"
        f"&cu=INR"
        f"&tn={quote(description)}"
    )

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filepath = os.path.join(OUTPUT_DIR, f"{filename}.png")
    img.save(filepath)
    print(f"✅ Generated: {filepath}")

print(f"\nDone! Generated {len(plans)} QR codes.")
