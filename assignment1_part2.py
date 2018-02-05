class Book:
    author = ''
    title = ''

    def __init__(self, title, author):
        self.author = author
        self.title = title

    def display(self):
        print(self.title + ', written by ' + self.author)


obj1 =  Book('Of Mice and Men', 'John Steinbeck')
obj2 =  Book('To Kill a Mockingbird', 'Harper Lee')
obj1.display()
obj2.display()


