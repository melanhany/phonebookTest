from phonebook.phonebook import Phonebook
import phonebook.constants as c
import sys

def main():
    """
    The main function to run the phonebook application.
    """
    phonebook = Phonebook(c.FILENAME, c.entries_per_page)
    phonebook.load()
    
    while True:
        print("\nТелефонный справочник")
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")

        choice: str = input("Выберите действие: ")

        menu: dict = {
            '1': display,
            '2': add,
            '3': edit,
            '4': search,
            '5': exit_program,
        }

        action = menu.get(choice)
        if action:
            action(phonebook)
        else:
            print("Неверный выбор. Попробуйте снова.")

def display(phonebook: Phonebook) -> None:
    """
    Display a page of phonebook entries.

    Parameters:
    - phonebook (Phonebook): The phonebook instance to display entries from.
    """
    while True:
        print(f"Всего страниц: {phonebook.calculate_pages()}")
        page_input = input("Введите номер страницы или 'выйти' для выхода: ")
        if page_input.lower() == 'выйти':
            break
        try:
            page = int(page_input)
            phonebook.display_entries(page)
        except ValueError:
            print("Неверный выбор. Попробуйте снова.")

def add(phonebook: Phonebook) -> None:
    """
    Add a new entry to the phonebook.

    Parameters:
    - phonebook (Phonebook): The phonebook instance to add the entry to.
    """
    print("Добавление новой записи:")
    phonebook.add_entry()

def edit(phonebook: Phonebook) -> None:
    """
    Edit an existing phonebook entry.

    Parameters:
    - phonebook (Phonebook): The phonebook instance to edit the entry in.
    """
    print("Редактирование записи:")
    try:
        entry_id = int(input("Введите номер записи для редактирования: "))
        phonebook.edit_entry(entry_id)
    except ValueError:
            print("Неверный выбор.")

def search(phonebook: Phonebook) -> None:
    """
    Search for entries in the phonebook based on a query.

    Parameters:
    - phonebook (Phonebook): The phonebook instance to search entries in.
    """
    query = input("Введите строку для поиска: ")
    results = phonebook.search_entries(query)
    if results:
        print("Результаты поиска:")
        for idx, entry in enumerate(results, start=1):
            print(f"{idx}. {entry}")
    else:
        print("Ничего не найдено.")

def exit_program(phonebook: Phonebook) -> None:
    """
    Exit the phonebook application, saving any changes to the file.

    Parameters:
    - phonebook (Phonebook): The phonebook instance to save entries from.
    """
    phonebook.save_entries()
    print("До свидания!")
    sys.exit(0)

if __name__ == "__main__":
    main()