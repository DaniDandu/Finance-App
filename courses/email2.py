import smtplib


server = smtplib.SMTP(host="localhost", port=7777)

message = """
a

message

on multiple lines!
"""

server.sendmail(
    from_addr="danidandu@localhost.com",
    to_addrs=["danidandu19gmail.com", "dnd.dannyz@gmail.com"],
    msg=message,
)
