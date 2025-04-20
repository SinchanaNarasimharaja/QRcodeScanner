import qrcode
features = qrcode.QRCode(version=1, box_size=40, border=3)
features.add_data("https://www.linkedin.com/in/sinchana-n-936a8b22b/")
features.make(fit=True)
generate_image = features.make_image(fill_color="blue", back_color="white")
generate_image.save('image3.png')
