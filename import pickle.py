import pickle

class Movie:
    def __init__(self, title, seats_available):
        self.title = title
        self.seats_available = seats_available

class Screen:
    def __init__(self, screen_number):
        self.screen_number = screen_number
        self.timeslots = {}

    def add_timeslot(self, timeslot, movie_title):
        self.timeslots[timeslot] = movie_title

class Booking:
    def __init__(self, user_name, movie_title, screen_number, timeslot, seats):
        self.user_name = user_name
        self.movie_title = movie_title
        self.screen_number = screen_number
        self.timeslot = timeslot
        self.seats = seats

class CinemaBookingSystem:
    def __init__(self):
        self.movies = {}
        self.screens = {}
        self.bookings = []
        self.current_user = None

    def add_movie(self, title, seats_available):
        self.movies[title] = Movie(title, seats_available)

    def add_screen(self, screen_number):
        self.screens[screen_number] = Screen(screen_number)

    def book_ticket(self, movie_title, screen_number, timeslot, seats):
        if movie_title not in self.movies or screen_number not in self.screens:
            print("Selected movie or screen is invalid.")
            return False

        movie = self.movies[movie_title]
        screen = self.screens[screen_number]

        if timeslot not in screen.timeslots or movie.title != screen.timeslots[timeslot]:
            print("The selected timeslot isn't available for the chosen movie on this screen.")
            return False

        if len(seats) > movie.available_seats:
            print("Not enough seats available.")
            return False

        booking = Booking(self.current_user, movie_title, screen_number, timeslot, seats)
        self.bookings.append(booking)
        movie.available_seats -= len(seats)
        print("Booking is successful!")
        return True

    def save_data(self):
        with open('cinema_data.pkl', 'wb') as f:
            pickle.dump((self.movies, self.screens, self.bookings), f)
        print("Data saved successfully.")

    def load_data(self):
        try:
            with open('cinema_data.pkl', 'rb') as f:
                self.movies, self.screens, self.bookings = pickle.load(f)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

def user_interaction(cinema_booking_system):
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Registration process...")
        # Logic for registration
    elif choice == "2":
        print("Login process...")
        user_name = input("Enter your username: ")
        cinema_booking_system.current_user = user_name
        movie_title = input("Enter movie title: ")
        screen_number = int(input("Enter screen number: "))
        timeslot = input("Enter timeslot: ")
        seats = input("Enter seats (comma-separated): ").split(",")
        success = cinema_booking_system.book_ticket(movie_title, screen_number, timeslot, seats)
        if success:
            print("Booking confirmed.")
    elif choice == "3":
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def main():
    cinema_booking_system = CinemaBookingSystem()

    # Load data if available
    cinema_booking_system.load_data()

    while True:
        if cinema_booking_system.current_user is None:
            user_logged_in = user_interaction(cinema_booking_system)
            if not user_logged_in:
                break
        else:
            print("\n1. Add Movie")
            print("2. Add Screen")
            print("3. Book Ticket")
            print("4. Save Data")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter movie title: ")
                seats_available = int(input("Enter available seats: "))
                cinema_booking_system.add_movie(title, seats_available)
            elif choice == "2":
                screen_number = int(input("Enter screen number: "))
                cinema_booking_system.add_screen(screen_number)
            elif choice == "3":
                movie_title = input("Enter movie title: ")
                screen_number = int(input("Enter screen number: "))
                timeslot = input("Enter timeslot: ")
                seats = input("Enter seats (comma-separated): ").split(",")
                success = cinema_booking_system.book_ticket(movie_title, screen_number, timeslot, seats)
                if success:
                    print("Booking confirmed.")
            elif choice == "4":
                cinema_booking_system.save_data()
            elif choice == "5":
                cinema_booking_system.current_user = None
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
