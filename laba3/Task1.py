"""Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four types
of tickets: regular ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased fewer
than 10 days before the event) and student ticket.
Additional information:
-advance ticket - discount 40% of the regular ticket price;
-student ticket - discount 50% of the regular ticket price;
-late ticket - additional 10% to the reguler ticket price.
All tickets must have the following properties:
-the ability to construct a ticket by number;
-the ability to ask for a ticket’s price;
-the ability to print a ticket as a String."""
import datetime


class Ticket:
    def __init__(self, event_name, date, now, ticket_type, price, number):
        self.__event_name = event_name
        self.__date = date
        self.__now = now
        self.__ticket_type = ticket_type
        self.__price = price
        self.__number = number

    @property
    def printer(self):
        return 'Event: ' + self.event_name + '\nDate of event: ' + str(self.date) + '\nTicket bought: ' + str(self.now) \
               + '\nType: ' + self.ticket_type + '\nPrice: ' + str(self.price) + '\nNumber: ' + str(self.number) + '\n'

    @property
    def event_name(self):
        return self.__event_name

    @property
    def date(self):
        return self.__date

    @property
    def now(self):
        return self.__now

    @property
    def ticket_type(self):
        return self.__ticket_type

    @property
    def price(self):
        return self.__price

    @property
    def number(self):
        return self.__number

    @event_name.setter
    def event_name(self, event_name):
        self.__event_name = event_name

    @date.setter
    def date(self, date):
        self.__date = date

    @now.setter
    def now(self, now):
        self.__now = now

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        self.__ticket_type = ticket_type

    @price.setter
    def price(self, price):
        self.__price = price

    @number.setter
    def number(self, number):
        self.__number = number


class Event:
    tickets = []

    def __init__(self, event_name, date, ticket_circulation, price):
        delta = date - datetime.datetime.now()
        if not isinstance(event_name, str):
            raise TypeError("The event name is a string")
        elif not isinstance(date, datetime.datetime):
            raise TypeError("The date is a datetime.datetime value")
        elif not isinstance(ticket_circulation, int):
            raise TypeError("Ticket circulation is a int value")
        elif not isinstance(price, int):
            raise TypeError("Price is a int value")
        elif delta.days < 0:
            raise ValueError("This date is from the past")
        elif ticket_circulation <= 0:
            raise ValueError("The number of tickets is positive")
        elif price < 0:
            raise ValueError("Price is not negative")
        self.__event_name = event_name
        self.__date = date
        self.__ticket_circulation = ticket_circulation
        self.__price = price

    def buying(self, student):
        if len(self.tickets) >= self.ticket_circulation:
            raise Warning('Sold out')
        ticket_type = 'regular'
        price = self.price
        now = datetime.datetime.now()
        delta = self.date - now
        if student:
            price = 0.5 * self.price
            ticket_type = 'student'
        elif delta.days >= 60:
            price = 0.6 * self.price
            ticket_type = 'advance'
        elif 0 < delta.days < 10:
            price = 1.1 * self.price
            ticket_type = 'late'
        elif delta.days < 0:
            raise ValueError("The event has already taken place")
        new_ticket = Ticket(self.event_name, self.date, now, ticket_type, price, len(self.tickets))
        self.tickets.append(new_ticket)
        return new_ticket

    def ask(self, student_card):
        price = self.price
        now = datetime.datetime.now()
        delta = self.date - now
        if student_card:
            price = 0.5 * self.price
        elif delta.days >= 60:
            price = 0.6 * self.price
        elif 0 < delta.days < 10:
            price = 1.1 * self.price
        return 'Ticket price: ' + str(price) + '\n'

    def search(self, number):
        if not isinstance(number, int) and not number >= 0:
            raise TypeError("The ticket number is an integer positive value")
        if number < len(self.tickets):
            return 'We found your ticket: \n' + self.tickets[number].printer
        elif len(self.tickets) <= number < self.ticket_circulation:
            return "A ticket with this number has not been sold yet"
        else:
            return "There is no ticket with such a number"

    @property
    def event_name(self):
        return self.__event_name

    @property
    def date(self):
        return self.__date

    @property
    def ticket_circulation(self):
        return self.__ticket_circulation

    @property
    def price(self):
        return self.__price

    @event_name.setter
    def event_name(self, event_name):
        if not isinstance(event_name, str):
            raise TypeError("The event name is a string")
        else:
            self.__event_name = event_name

    @date.setter
    def date(self, date):
        delta = date - datetime.datetime.now()
        if not isinstance(date, datetime.datetime):
            raise TypeError("The date is a datetime.datetime value")
        elif delta.days < 0:
            raise ValueError("This date is from the past")
        else:
            self.__date = date

    @ticket_circulation.setter
    def now(self, ticket_circulation):
        if ticket_circulation <= 0:
            raise ValueError("The number of tickets is positive")
        elif ticket_circulation <= 0:
            raise ValueError("The number of tickets is positive")
        else:
            self.__ticket_circulation = ticket_circulation

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError("Price is a int value")
        elif price < 0:
            raise ValueError("Price is not negative")
        else:
            self.__price = price

if __name__ == "__main__":
    Big_money = Event("Big_money", datetime.datetime(2022, 2, 26), 5000, 500)
    your_ticket1 = Big_money.buying("№999999")
    your_ticket2 = Big_money.buying(None)
    print(your_ticket1.printer)
    print(your_ticket2.printer)
    your_ticket3 = Big_money.ask("№88")
    print(your_ticket3)
    your_ticket4 = Big_money.search(1)
    print(your_ticket4)
