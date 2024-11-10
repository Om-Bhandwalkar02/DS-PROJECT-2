import tkinter as tk
from tkinter import messagebox

# Define queues for different services
queues = {
    "Account Services": [],
    "Loan Services": [],
    "General Inquiry": [],
    "Cash Deposit": [],
    "Foreign Exchange": []
}
selected_service = None


# Helper function to update queue display for the selected service
def update_queue_display():
    listbox_queue.delete(0, tk.END)
    for customer in queues[selected_service]:
        listbox_queue.insert(tk.END, f"{customer['name']}")


# Function to show the specific service page
def show_service_page(service):
    global selected_service
    selected_service = service

    for widget in specific_fields_frame.winfo_children():
        widget.destroy()

    label_service_title.config(text=f"{service} Queue Management")

    label_customer_name.grid(row=0, column=0)
    entry_customer_name.grid(row=0, column=1)

    if service == "Cash Deposit":
        label_amount = tk.Label(specific_fields_frame, text="Amount to Deposit:", font=('Arial', 12))
        label_amount.grid(row=1, column=0, pady=5)
        entry_amount = tk.Entry(specific_fields_frame, font=('Arial', 12))
        entry_amount.grid(row=1, column=1)
        specific_fields_frame.amount_field = entry_amount

    elif service == "Loan Services":
        label_loan_type = tk.Label(specific_fields_frame, text="Loan Type:", font=('Arial', 12))
        label_loan_type.grid(row=1, column=0, pady=5)
        loan_options = ["Home Loan", "Personal Loan", "Education Loan"]
        loan_type_var = tk.StringVar(value=loan_options[0])
        loan_type_dropdown = tk.OptionMenu(specific_fields_frame, loan_type_var, *loan_options)
        loan_type_dropdown.grid(row=1, column=1)
        specific_fields_frame.loan_type_field = loan_type_var

        label_loan_amount = tk.Label(specific_fields_frame, text="Loan Amount:", font=('Arial', 12))
        label_loan_amount.grid(row=2, column=0, pady=5)
        entry_loan_amount = tk.Entry(specific_fields_frame, font=('Arial', 12))
        entry_loan_amount.grid(row=2, column=1)
        specific_fields_frame.loan_amount_field = entry_loan_amount

    elif service == "Foreign Exchange":
        label_currency = tk.Label(specific_fields_frame, text="Currency Type:", font=('Arial', 12))
        label_currency.grid(row=1, column=0, pady=5)
        currency_options = ["USD", "EUR", "GBP", "JPY"]
        currency_var = tk.StringVar(value=currency_options[0])
        currency_dropdown = tk.OptionMenu(specific_fields_frame, currency_var, *currency_options)
        currency_dropdown.grid(row=1, column=1)
        specific_fields_frame.currency_field = currency_var

        label_exchange_amount = tk.Label(specific_fields_frame, text="Exchange Amount:", font=('Arial', 12))
        label_exchange_amount.grid(row=2, column=0, pady=5)
        entry_exchange_amount = tk.Entry(specific_fields_frame, font=('Arial', 12))
        entry_exchange_amount.grid(row=2, column=1)
        specific_fields_frame.exchange_amount_field = entry_exchange_amount

    update_queue_display()
    service_selection_frame.pack_forget()
    queue_management_frame.pack()


def back_to_services():
    queue_management_frame.pack_forget()
    service_selection_frame.pack()


def add_customer():
    customer_name = entry_customer_name.get().strip()
    if not customer_name:
        messagebox.showwarning("Input Error", "Please enter a customer name!")
        return

    customer_data = {"name": customer_name}

    if selected_service == "Cash Deposit":
        amount = specific_fields_frame.amount_field.get().strip()
        if not amount:
            messagebox.showwarning("Input Error", "Please enter the deposit amount!")
            return
        customer_data["amount"] = amount

    elif selected_service == "Loan Services":
        loan_type = specific_fields_frame.loan_type_field.get().strip()
        loan_amount = specific_fields_frame.loan_amount_field.get().strip()
        if not loan_type or not loan_amount:
            messagebox.showwarning("Input Error", "Please select a loan type and enter the loan amount!")
            return
        customer_data["loan_type"] = loan_type
        customer_data["loan_amount"] = loan_amount

    elif selected_service == "Foreign Exchange":
        currency = specific_fields_frame.currency_field.get().strip()
        exchange_amount = specific_fields_frame.exchange_amount_field.get().strip()
        if not currency or not exchange_amount:
            messagebox.showwarning("Input Error", "Please select a currency type and enter the exchange amount!")
            return
        customer_data["currency"] = currency
        customer_data["exchange_amount"] = exchange_amount

    queues[selected_service].append(customer_data)
    update_queue_display()
    entry_customer_name.delete(0, tk.END)

    if selected_service == "Cash Deposit":
        specific_fields_frame.amount_field.delete(0, tk.END)
    elif selected_service == "Loan Services":
        specific_fields_frame.loan_amount_field.delete(0, tk.END)
    elif selected_service == "Foreign Exchange":
        specific_fields_frame.exchange_amount_field.delete(0, tk.END)


def serve_customer():
    if queues[selected_service]:
        served_customer = queues[selected_service].pop(0)
        update_queue_display()
        messagebox.showinfo("Served", f"{selected_service} - '{served_customer['name']}' has been served!")
    else:
        messagebox.showinfo("Empty Queue", f"No customers in the {selected_service} queue to serve!")


def clear_queue():
    queues[selected_service] = []
    update_queue_display()


# Main window setup
root = tk.Tk()
root.title("Professional Bank Queue System")
root.geometry("500x650")
root.config(bg='#f8f9fa')

# Colors and Fonts
primary_bg = '#ffffff'
primary_fg = '#2e2e2e'
highlight_bg = '#007bff'
button_bg = '#6c757d'
button_fg = '#ffffff'
title_font = ('Helvetica', 18, 'bold')
label_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')

# Service Selection Page
service_selection_frame = tk.Frame(root, bg=primary_bg)
label_title = tk.Label(service_selection_frame, text="Bank Service System", font=title_font, bg=primary_bg,
                       fg=highlight_bg)
label_title.pack(pady=20)

label_select_service = tk.Label(service_selection_frame, text="Select a Service", font=('Arial', 14), bg=primary_bg,
                                fg=primary_fg)
label_select_service.pack(pady=10)

for service in queues.keys():
    button_service = tk.Button(service_selection_frame, text=service, font=button_font, bg=highlight_bg, fg=button_fg,
                               width=20, command=lambda s=service: show_service_page(s))
    button_service.pack(pady=5)

# Add author label at the bottom of the selection page
label_author_main = tk.Label(service_selection_frame, text="Created by: Om Bhandwalkar\nSRN: 31231851",
                             font=('Arial', 10), bg=primary_bg, fg='#6c757d')
label_author_main.pack(side=tk.BOTTOM, pady=10)
service_selection_frame.pack()

# Queue Management Page with customer input and queue list
queue_management_frame = tk.Frame(root, bg=primary_bg)
label_service_title = tk.Label(queue_management_frame, text="Bank Service Queue", font=title_font, bg=primary_bg,
                               fg=highlight_bg)
label_service_title.pack(pady=20)

label_customer_prompt = tk.Label(queue_management_frame, text="Enter Customer Name:", font=label_font, bg=primary_bg,
                                 fg=primary_fg)
label_customer_prompt.pack(pady=5)

frame_add_customer = tk.Frame(queue_management_frame, bg=primary_bg)
frame_add_customer.pack(pady=10)

label_customer_name = tk.Label(frame_add_customer, text="Customer Name:", font=label_font, bg=primary_bg, fg=primary_fg)
label_customer_name.grid(row=0, column=0, pady=5)
entry_customer_name = tk.Entry(frame_add_customer, font=label_font, width=25)
entry_customer_name.grid(row=0, column=1)

specific_fields_frame = tk.Frame(queue_management_frame, bg=primary_bg)
specific_fields_frame.pack(pady=10)

button_add = tk.Button(queue_management_frame, text="Add to Queue", font=button_font, bg=highlight_bg, fg=button_fg,
                       command=add_customer)
button_add.pack(pady=5)

label_queue = tk.Label(queue_management_frame, text="Current Queue:", font=button_font, bg=primary_bg, fg=primary_fg)
label_queue.pack(pady=10)

listbox_queue = tk.Listbox(queue_management_frame, font=label_font, height=10, width=40, bg='#e9ecef', relief=tk.SUNKEN)
listbox_queue.pack(pady=5)

frame_controls = tk.Frame(queue_management_frame, bg=primary_bg)
frame_controls.pack(pady=15)

button_serve = tk.Button(frame_controls, text="Serve Next Customer", font=button_font, bg=highlight_bg, fg=button_fg,
                         command=serve_customer)
button_serve.grid(row=0, column=0, padx=10)
button_clear = tk.Button(frame_controls, text="Clear Queue", font=button_font, bg='#dc3545', fg=button_fg,
                         command=clear_queue)
button_clear.grid(row=0, column=1, padx=10)
button_back = tk.Button(frame_controls, text="Back to Services", font=button_font, bg=button_bg, fg=button_fg,
                        command=back_to_services)
button_back.grid(row=0, column=2, padx=10)

# Add author label at the bottom of the queue management page
label_author_queue = tk.Label(queue_management_frame, text="Created by: Om Bhandwalkar\nSRN: 31231851",
                              font=('Arial', 10), bg=primary_bg, fg='#6c757d')
label_author_queue.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
