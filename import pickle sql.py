+-------------------+               +-------------------+             +---------------------+
|     Movie         |               |     Screen        |             |      Booking        |
+-------------------+               +-------------------+             +---------------------+
| - title: str      |               | - screen_number:  |             | - user_name: str    |
| - seats_available:|               |     int           |             | - movie_title: str  |
|      int          |               | - timeslots: dict |             | - screen_number: int|
+-------------------+               +-------------------+             | - timeslot: str     |
       |                               |                               | - seats: list[str]  |
       |                               |                               +---------------------+
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       +--------------------------------
       |
       |
+---------------------+
|  CinemaBookingSystem|
+---------------------+
| - movies: dict      |
| - screens: dict     |
| - bookings: list    |
| - current_user: str |
+---------------------+
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       +--------------+
