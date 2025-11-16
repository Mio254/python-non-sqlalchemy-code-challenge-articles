class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = [article.magazine for article in self.articles()]
       
        return list(set(mags))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()]))


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name        
        self.category = category  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors))  

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        result = []
        for author in self.contributors():
            authored_articles = [a for a in self.articles() if a.author == author]
            if len(authored_articles) > 2:
                result.append(author)
        return result
