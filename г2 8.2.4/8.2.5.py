class SMSender():
    def send_sms(self, message):
        print('Отправил сообщение через смс:', message)

class PushSender():
    def send_push(self, message):
        print('Отправим сообщение через пуш-уведомление' , message)


class MailSender():
    def send_mail(self, message):
        print('отправим сообщение через почту', message)

class SuperSender(SMSender, PushSender, MailSender):
    def send_all(self, message):
        self.send_sms(message)
        self.send_push(message)
        self.send_mail(message)

sender = SuperSender()
sender.send_all('text massage')