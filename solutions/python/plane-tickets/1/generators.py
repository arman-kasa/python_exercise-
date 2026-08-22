"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""

    letters = "ABCD"
    for index in range(number):
        yield letters[index % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats."""

    letters = generate_seat_letters(number)
    for index in range(number):
        row = index // 4 + 1
        if row >= 13:
            row += 1
        yield f"{row}{next(letters)}"


def assign_seats(passengers):
    """Assign seats to passengers."""

    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""

    for seat_number in seat_numbers:
        yield (seat_number + flight_id).ljust(12, "0")
