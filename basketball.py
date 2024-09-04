import tkinter as tk

class BasketballCourtBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basketball Court Booking System")
        self.root.configure(bg="black")
        
        self.slots = [
            TimeSlot(6, 8, "AM"),
            TimeSlot(10, 12, "AM"),
            TimeSlot(2, 4, "PM"),
            TimeSlot(5, 7, "PM"),
            TimeSlot(8, 10, "PM")
        ]
        
        self.courts = [BasketballCourt(i + 1) for i in range(NUM_COURTS)]

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            self.root,
            text="Basketball Court Booking System",
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="black"
        )
        self.label.pack(pady=10)
        
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.pack(pady=10)

        self.choice_label = tk.Label(
            self.main_frame,
            text="Choose an option:",
            font=("Helvetica", 12, "bold"),
            fg="white",
            bg="black"
        )
        self.choice_label.pack()

        self.create_main_buttons()

        self.output_text = tk.Text(
            self.root,
            height=10,
            width=50,
            fg="white",
            bg="black"
        )
        self.output_text.pack()

    def create_main_buttons(self):
        self.create_button(
            self.main_frame,
            "Book a Court",
            self.show_book_court_frame
        )

        self.create_button(
            self.main_frame,
            "Cancel Booking",
            self.show_cancel_booking_frame
        )

        self.create_button(
            self.main_frame,
            "Calculate Air Pressure",
            self.show_air_pressure_frame
        )

        self.create_button(
            self.main_frame,
            "Show Bookings",
            self.show_bookings_frame
        )

        self.create_button(
            self.main_frame,
            "Exit",
            self.root.quit  # Function to quit the app
        )

    def create_button(self, frame, text, command):
        button = tk.Button(
            frame,
            text=text,
            command=command,
            bg="light blue"
        )
        button.pack(pady=5, padx=10, fill=tk.X)

    def show_book_court_frame(self):
        self.clear_messages()
        self.hide_main_frame()

        self.book_court_frame = tk.Frame(self.root, bg="black")
        self.book_court_frame.pack(pady=10)

        self.create_label(self.book_court_frame, "Book a Court", 14)

        self.create_label(self.book_court_frame, "Enter court number (1-5):")
        self.court_number_entry = self.create_entry(self.book_court_frame)
        
        self.create_label(self.book_court_frame, "Select a time slot:")
        self.slot_var = tk.StringVar()
        self.slot_var.set("6 AM - 8 AM")  # Default value
        self.slot_menu = tk.OptionMenu(self.book_court_frame, self.slot_var, *[
            f"{slot.startHour} {slot.am_pm} - {slot.endHour} {slot.am_pm}" for slot in self.slots
        ])
        self.slot_menu.pack()
        
        self.create_button(self.book_court_frame, "Book Slot", self.book_slot)
        self.create_button(self.book_court_frame, "Back", self.back_to_main_frame)

    def show_cancel_booking_frame(self):
        self.clear_messages()
        self.hide_main_frame()

        self.cancel_booking_frame = tk.Frame(self.root, bg="black")
        self.cancel_booking_frame.pack(pady=10)

        self.create_label(self.cancel_booking_frame, "Cancel Booking", 14)

        self.create_label(self.cancel_booking_frame, "Enter court number (1-5):")
        self.cancel_court_number_entry = self.create_entry(self.cancel_booking_frame)
        
        self.create_label(self.cancel_booking_frame, "Select a time slot:")
        self.cancel_slot_var = tk.StringVar()
        self.cancel_slot_var.set("6 AM - 8 AM")  # Default value
        self.cancel_slot_menu = tk.OptionMenu(self.cancel_booking_frame, self.cancel_slot_var, *[
            f"{slot.startHour} {slot.am_pm} - {slot.endHour} {slot.am_pm}" for slot in self.slots
        ])
        self.cancel_slot_menu.pack()
        
        self.create_button(self.cancel_booking_frame, "Cancel Slot", self.cancel_slot)
        self.create_button(self.cancel_booking_frame, "Back", self.back_to_main_frame)

    def show_air_pressure_frame(self):
        self.clear_messages()
        self.hide_main_frame()

        self.air_pressure_frame = tk.Frame(self.root, bg="black")
        self.air_pressure_frame.pack(pady=10)

        self.create_label(self.air_pressure_frame, "Calculate Air Pressure", 14)

        self.create_label(self.air_pressure_frame, "Enter basketball weight (in pounds):")
        self.ball_weight_entry = self.create_entry(self.air_pressure_frame)
        
        self.create_button(self.air_pressure_frame, "Calculate Pressure", self.calculate_pressure)
        self.create_button(self.air_pressure_frame, "Back", self.back_to_main_frame)

    def show_bookings_frame(self):
        self.clear_messages()
        self.hide_main_frame()

        self.bookings_frame = tk.Frame(self.root, bg="black")
        self.bookings_frame.pack(pady=10)

        self.create_label(self.bookings_frame, "Current Booking Status", 14)

        bookings_text = "Current Booking Status:\n\n"
        for court in self.courts:
            bookings_text += f"Court {court.courtNumber}:\n"
            for j, slot in enumerate(court.isBooked):
                slot_timing = f"{self.slots[j].startHour} {self.slots[j].am_pm} - {self.slots[j].endHour} {self.slots[j].am_pm}"
                bookings_text += f"Slot {slot_timing}: {'Booked' if slot else 'Available'}\n"
            bookings_text += "\n"
        
        self.bookings_display = tk.Text(
            self.bookings_frame,
            height=10,
            width=50,
            fg="white",
            bg="black"
        )
        self.bookings_display.insert(tk.END, bookings_text)
        self.bookings_display.pack()

        self.create_button(self.bookings_frame, "Back", self.back_to_main_frame)

    def clear_messages(self):
        self.output_text.delete(1.0, tk.END)

    def hide_main_frame(self):
        self.main_frame.pack_forget()

    def back_to_main_frame(self):
        self.clear_messages()
        if hasattr(self, "book_court_frame"):
            self.book_court_frame.pack_forget()
        if hasattr(self, "cancel_booking_frame"):
            self.cancel_booking_frame.pack_forget()
        if hasattr(self, "air_pressure_frame"):
            self.air_pressure_frame.pack_forget()
        if hasattr(self, "bookings_frame"):
            self.bookings_frame.pack_forget()
        self.main_frame.pack()

    def create_label(self, frame, text, font_size=12, justify="center"):
        label = tk.Label(
            frame,
            text=text,
            font=("Helvetica", font_size, "bold"),
            fg="white",
            bg="black",
            justify=justify
        )
        label.pack()
        return label

    def create_entry(self, frame):
        entry = tk.Entry(frame)
        entry.pack()
        return entry

    def book_slot(self):
        court_number = int(self.court_number_entry.get())
        selected_slot = self.slot_var.get()

        if court_number >= 1 and court_number <= NUM_COURTS:
            selected_slot_index = None
            for index, slot in enumerate(self.slots):
                if selected_slot == f"{slot.startHour} {slot.am_pm} - {slot.endHour} {slot.am_pm}":
                    selected_slot_index = index
                    break
            
            if selected_slot_index is not None:
                if self.courts[court_number - 1].isBooked[selected_slot_index]:
                    message = f"Slot {selected_slot} is already booked for Court {court_number}."
                else:
                    self.courts[court_number - 1].isBooked[selected_slot_index] = True
                    message = f"Court {court_number} has been booked for Slot {selected_slot}."
            else:
                message = "Invalid time slot."
        else:
            message = "Invalid court number."

        self.output_text.insert(tk.END, message + "\n\n")

    def cancel_slot(self):
        court_number = int(self.cancel_court_number_entry.get())
        selected_slot = self.cancel_slot_var.get()

        if court_number >= 1 and court_number <= NUM_COURTS:
            selected_slot_index = None
            for index, slot in enumerate(self.slots):
                if selected_slot == f"{slot.startHour} {slot.am_pm} - {slot.endHour} {slot.am_pm}":
                    selected_slot_index = index
                    break
            
            if selected_slot_index is not None:
                if not self.courts[court_number - 1].isBooked[selected_slot_index]:
                    message = f"Slot {selected_slot} is not booked for Court {court_number}."
                else:
                    self.courts[court_number - 1].isBooked[selected_slot_index] = False
                    message = f"Booking for Court {court_number}, Slot {selected_slot} has been canceled."
            else:
                message = "Invalid time slot."
        else:
            message = "Invalid court number."

        self.output_text.insert(tk.END, message + "\n\n")

    def calculate_pressure(self):
        try:
            ball_weight = float(self.ball_weight_entry.get())
            required_air_pressure = calculate_air_pressure(ball_weight)
            message = "Recommended air pressure for the basketball: {:.2f} PSI".format(required_air_pressure)
        except ValueError:
            message = "Invalid input. Please enter a valid weight."

        self.output_text.insert(tk.END, message + "\n\n")

class TimeSlot:
    def __init__(self, startHour, endHour, am_pm):
        self.startHour = startHour
        self.endHour = endHour
        self.am_pm = am_pm

class BasketballCourt:
    def __init__(self, courtNumber):
        self.courtNumber = courtNumber
        self.isBooked = [False] * NUM_SLOTS

NUM_COURTS = 5
NUM_SLOTS = 5

def calculate_air_pressure(ball_weight):
    return ball_weight * 0.1333

if __name__ == "__main__":
    root = tk.Tk()
    app = BasketballCourtBookingApp(root)
    root.mainloop()