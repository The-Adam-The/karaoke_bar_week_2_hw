

class Room:

    def __init__(self, room_num, capacity, current_occupancy):
        self.room_num = room_num
        self.capacity = capacity
        self.current_occupancy = current_occupancy


    def check_room_availability(self):
        if self.current_occupancy:
            return f"Room {self.room_num} unavailable."
        return f"Room {self.room_num} available."

    def check_in_guest(self, *guests):
        if self.check_room_availability():
            for guest in guests:
                self.current_occupancy.append(guest)
    
    def check_out_guest(self, *guests):
        for guest in guests:
            self.current_occupancy.remove(guest)

    def check_out_all_guests(self):
        self.current_occupancy.clear()