import tkinter as tk
from tkinter import messagebox

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management")

        # Contact List
        self.contacts = []

        # GUI Components
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.address_entry = tk.Entry(root, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.contact_listbox = tk.Listbox(root, width=40, height=10)
        self.contact_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)

        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.grid(row=7, column=1, padx=10, pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=9, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=10, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Warning", "Name and phone number are required.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def search_contact(self):
        query = self.search_entry.get().lower()
        search_results = [contact for contact in self.contacts
                          if query in contact['name'].lower() or query in contact['phone'].lower()]

        self.contact_listbox.delete(0, tk.END)
        for result in search_results:
            self.contact_listbox.insert(tk.END, f"{result['name']} - {result['phone']}")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if name and phone:
                self.contacts[selected_index[0]]["name"] = name
                self.contacts[selected_index[0]]["phone"] = phone
                self.contacts[selected_index[0]]["email"] = email
                self.contacts[selected_index[0]]["address"] = address
                self.clear_entries()
                self.view_contacts()
                messagebox.showinfo("Success", "Contact updated successfully.")
            else:
                messagebox.showwarning("Warning", "Name and phone number are required.")
        else:
            messagebox.showwarning("Warning", "Select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
