import smtplib
# s = "wtfm962@gmail.com"


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('omiindustriesbot@gmail.com', 'e!9f^KGx5LQJhq8')
    server.sendmail('omiindustriesbot@gmail.com', to, content)
    server.close()


for i in range(900, 1000):
    x = f"wtfm{i}@gmail.com"
    try:
        sendEmail(x, "Mustakim is a bullshit Guy")
        print(f"Success Email Send to {x}")
    except Exception as e:
        print(e)
        print(f"Not Possible on {x}")

print("Program Ended......")
