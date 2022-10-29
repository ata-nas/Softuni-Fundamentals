class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_list = []

while True:
    user_input = input()
    if user_input == "Stop":
        break

    command = user_input.split(sep=" ")

    email = Email(command[0], command[1], command[2])

    emails_list.append(email)

sent_indices = [int(index) for index in input().split(sep=", ")]

for index in sent_indices:
    emails_list[index].send()

for item in emails_list:
    print(item.get_info())
