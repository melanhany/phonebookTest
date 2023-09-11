from typing import List
from .decorators import logger
import os


class Phonebook:
    def __init__(self, filename: str, entries_per_page: int):
        """
        Initialize a Phonebook instance.

        Parameters:
        - filename (str): The name of the file to read and save entries.
        - entries_per_page (int): Number of entries to display per page.
        """
        self.filename: str = filename
        self.entries: List[str] = []
        self.entries_per_page: int = entries_per_page
        self.id_counter: int = 1

    def load(self) -> None:
        """
        Load phonebook entries from a text file.

        This method reads the entries from the specified file and populates the phonebook.
        """
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as file:
            for line in file:
                parts: List[str] = line.strip().split("|")
                if len(parts) == 7:
                    (
                        entry,
                        last_name,
                        first_name,
                        middle_name,
                        organization,
                        work_phone,
                        personal_phone,
                    ) = parts
                    # Update the ID counter based on the loaded entries
                    entry_id: int = int(entry)
                    if entry_id >= self.id_counter:
                        self.id_counter = entry_id + 1
                    self.entries.append(line.strip())

    def calculate_pages(self) -> int:
        """
        Calculate the total number of pages needed to display all entries.

        Returns:
        - int: The total number of pages.
        """
        pages: int = len(self.entries) // self.entries_per_page
        if len(self.entries) % self.entries_per_page != 0:
            pages += 1

        return pages

    def save_entries(self) -> None:
        """
        Save phonebook entries to a text file.

        This method writes the phonebook entries to the specified file.
        """
        with open(self.filename, "w") as file:
            for entry in self.entries:
                file.write(entry + "\n")

    @logger
    def display_entries(self, page: int) -> None:
        """
        Display a page of phonebook entries.

        Parameters:
        - page (int): The page number to display.
        """
        start_idx = (page - 1) * self.entries_per_page
        end_idx = start_idx + self.entries_per_page
        for entry in self.entries[start_idx:end_idx]:
            print(entry)

    @logger
    def add_entry(self) -> None:
        """
        Add a new entry to the phonebook.

        This method prompts the user to enter details for a new entry and adds it to the phonebook.
        """
        entry_id: int = self.id_counter
        self.id_counter += 1
        last_name: str = input("Фамилия: ")
        first_name: str = input("Имя: ")
        middle_name: str = input("Отчество: ")
        organization: str = input("Организация: ")
        work_phone: str = input("Телефон рабочий: ")
        personal_phone: str = input("Телефон личный: ")
        new_entry: str = f"{entry_id}|{last_name}|{first_name}|{middle_name}|{organization}|{work_phone}|{personal_phone}"
        self.entries.append(new_entry)

    @logger
    def edit_entry(self, entry_id: int) -> None:
        """
        Edit an existing phonebook entry.

        Parameters:
        - entry_id (int): The unique ID of the entry to be edited.

        This method allows the user to edit an existing entry's information.
        """
        entry_index: int = -1
        for i, entry in enumerate(self.entries):
            parts: List[str] = entry.split("|")
            if parts and int(parts[0]) == entry_id:
                entry_index = i
                break

        if entry_index != -1:
            new_entry: str = input(
                "Введите новую информацию в формате 'Фамилия|Имя|Отчество|Организация|Телефон рабочий|Телефон личный': "
            )
            self.entries[entry_index] = f"{entry_id}|{new_entry}"
            self.save_entries()
            print("Запись успешно отредактирована.")
        else:
            print("Запись с указанным номером не найдена.")

    @logger
    def search_entries(self, query: str) -> List[str]:
        """
        Search for entries in the phonebook based on a query.

        Parameters:
        - query (str): The search query.

        Returns:
        - list: A list of matching entries.
        """
        results: List[str] = [
            entry for entry in self.entries if query.lower() in entry.lower()
        ]
        return results
