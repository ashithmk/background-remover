from withoutbg import WithoutBG

img = WithoutBG.opensource()
result = img.remove_background("WhatsApp Image 2026-01-19 at 1.12.03 AM.jpeg")
result.save("photo_no_bg.png")
