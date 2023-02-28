#Подсчет количества символов
class Article():
    def __init__(self, content):
        self.content = content

class ArticleExtended(Article):
    def count_symbols(self):
        return len(self.content)
    def count_words(self):
        words = self.content.split()

        return len(words)

article = ArticleExtended(
    '''
    Ваш баланс составляет $ - 100.000
    Номер заблокирован.
    Вас ожидает 10 лет рабства на урановых рудниках.
    Одна СМСка. Чертов роуминг в Сибири. (с) Иванов Иван - Баланс   
    '''
)

print(article.count_symbols())
print(article.count_words())
