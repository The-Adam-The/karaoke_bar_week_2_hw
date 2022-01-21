

class Room:

    def __init__(self, room_num, capacity, current_occupancy, song_list):
        self.room_num = room_num
        self.capacity = capacity
        self.current_occupancy = current_occupancy
        self.song_list = song_list

    def check_room_availability(self):
        if self.current_occupancy:
            return f"Room {self.room_num} unavailable."
        return f"Room {self.room_num} available."

    def check_in_guest(self, *guests):
        room_availability = self.check_room_availability()
       
        if room_availability[-12:] == "unavailable":
          
            return room_availability
        if len(guests) > self.capacity:
            return "Only 8 people are able to use this room. Please choose a larger room."

        for guest in guests:
            self.current_occupancy.append(guest) 
        


    def check_out_guest(self, *guests):
        for guest in guests:
            self.current_occupancy.remove(guest)

    def check_out_all_guests(self):
        self.current_occupancy.clear()
    
