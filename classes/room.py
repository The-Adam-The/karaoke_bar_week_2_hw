class Room:

    def __init__(self, room_num, capacity, current_occupancy, song_list):
        self.room_num = room_num
        self.capacity = capacity
        self.current_occupancy = current_occupancy
        self.song_list = song_list
        self.entry_fee = 500

    def check_room_availability(self):
        if self.current_occupancy:
            return f"Room {self.room_num} unavailable."
        return f"Room {self.room_num} available."

    def customer_has_sufficient_funds(self, guest_money):
        if guest_money >= self.entry_fee:
            return True
        return False

    def pay_entry_fee(self, guest):
        guest.money -= self.entry_fee

    def favorite_song_react(self, guest, song):
        print(f"{guest}: かこい! {song}! この曲が大好きだ! 歌いたい!")
       

        
    def check_in_guest(self, *guests):
        denied_entry_list = []
        room_availability = self.check_room_availability()
       
        if room_availability[-12:] == "unavailable":
          
            return room_availability
        if len(guests) > self.capacity:
            return "Only 8 people are able to use this room. Please choose a larger room."

        for guest in guests:
            if guest.money >= self.entry_fee:
                self.pay_entry_fee(guest)
                self.current_occupancy.append(guest)
                for song in self.song_list:
                    
                    if guest.favorite_song == song.title:
                        self.favorite_song_react(guest.name, song.title)
            else:
                denied_entry_list.append(guest.name)

        if denied_entry_list:
            out_string = " ".join([str(name) for name in denied_entry_list])
            return f"The following guests have insufficient funds: {out_string}"
        

    def check_out_guest(self, *guests):
        for guest in guests:
            self.current_occupancy.remove(guest)

    def check_out_all_guests(self):
        self.current_occupancy.clear()
    
