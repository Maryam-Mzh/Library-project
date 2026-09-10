# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:07:02 2026

@author: Maryam
"""

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {
            "title": title,
            "author": author
        }
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                return
        print("Book not found")

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return book
        return None

    def show_books(self):
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}")
        




























