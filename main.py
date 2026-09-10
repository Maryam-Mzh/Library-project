# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:32:56 2026

@author: Maryam
"""

from mylibrary.library import Library

if __name__ == "__main__":
    library = Library()
    
    while True:
        print("\n1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Show books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            library.add_book(title, author)

        elif choice == "2":
            title = input("Enter title: ")
            library.remove_book(title)

        elif choice == "3":
            title = input("Enter title: ")
            result = library.search_book(title)

            if result:
                print(result)
            else:
                print("Book not found")

        elif choice == "4":
            library.show_books()

        elif choice == "5":
            break

        else:
            print("Invalid choice")
            
        

