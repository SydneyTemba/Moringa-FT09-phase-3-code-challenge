# tests/test_models.py
import unittest
from models.article import Article
from models.author import Author
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_article_creation(self):
        author = Author("Jane Smith")
        magazine = Magazine("Science Today", "Science")
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")

if __name__ == '__main__':
    unittest.main()
