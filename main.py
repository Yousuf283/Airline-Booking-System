import os
import random
import data
import encrypt as e
import login

states = ['start', 'login', 'menu', 'book_seat', 'cancel_seat', 'upgrade']
state = 'start'

customers = ['A','B','C','D','E','F','G']
seating_area = [["FC", "|||", "FC"],
                ["FC", "|||", "FC"],
                ["ER", "ER", "|||", "ER", "ER"],
                ["SD", "SD", "|||", "SD", "SD"],
                ["ER", "IF", "|||", "IF", "ER"],
                ["SD", "SD", "|||", "SD", "SD"],
                ["SD", "SD", "|||", "SD", "SD"],
                ["ER", "ER", "|||", "ER", "ER"],
                ["ER", "IF", "|||", "IF", "ER"]
]

def display_seats(seating_area):
    for i in range(len(seating_area)):
        temp = ''
        for j in range(len(seating_area[i])):
            temp += seating_area[i][j] + ' '
        print(temp)

def book_seat(state, seating_area):
    data = get_input(state, seating_area)
    if data[0] == 'A' and data[1] == '0' and data[2] == '0':
        seating_area[0][0] += '@{0}'.format(data[0])
    elif data[0] != -1 and data[1] != -1 and data[2] != -1:
        customer = data[0]
        row = data[1]
        seat = data[2]
        seating_area[row-1][seat-1] += '@{0}'.format(customer)

def release_seat(state, seating_area):
    data = get_input(state, seating_area)

    if '@' in seating_area[data[0]-1][data[1]-1]:
        seating_area[data[0]-1][data[1]-1] = seating_area[data[0]-1][data[1]-1][:-2]

def remaining_seats(seating_area):
    count = 0
    for i in range(len(seating_area)):
        for j in range(len(seating_area[i])):
            if '@' not in seating_area[i][j]:
                count += 1
    count - 9
    print(count, 'Seats Available')

def get_revenue(seating_area):
    SD = 70
    total = 0
    for i in range(len(seating_area)):
        for j in range(len(seating_area[i])):
            if 'SD@' in seating_area[i][j]:
                total += SD
            if 'FC@' in seating_area[i][j]:
                total += SD*10
            if 'ER@' in seating_area[i][j]:
                total += SD*1.1
            if 'IF@' in seating_area[i][j]:
                total += SD*0.1
    print("Total revenue = £", total)

def get_average(seating_area):
    SD = 70
    total = 0
    count = 0
    for i in range(len(seating_area)):
        for j in range(len(seating_area[i])):
            if 'SD@' in seating_area[i][j]:
                total += SD
                count += 1
            if 'FC@' in seating_area[i][j]:
                total += SD*10
                count += 1
            if 'ER@' in seating_area[i][j]:
                total += SD*1.1
                count += 1
            if 'IF@' in seating_area[i][j]:
                total += SD*0.1
                count += 1
    print("Average ticket price = £", (total/count))

def give_upgrade(state, seating_area):
    taken = 0
    available = []
    if ('@' in seating_area[0][0]):
        taken += 1
    else:
        available.append([0,0])
    if ('@' in seating_area[0][2]):
        taken += 1
    else:
        available.append([0,2])
    if ('@' in seating_area[1][0]):
        taken += 1
    else:
        available.append([1,0])
    if ('@' in seating_area[1][2]):
        taken += 1
    else:
        available.append([1,2])

    if taken != 4:
        pos_1, pos_2 = get_input(state, seating_area)
        ref = seating_area[pos_1][pos_2].replace(seating_area[pos_1][pos_2][:-2],'')
        seating_area[pos_1][pos_2] = seating_area[pos_1][pos_2][:-2]

        random_number = random.randint(0,len(available)-1)
        seating_area[available[random_number][0]][available[random_number][1]] += ref

        display_seats(seating_area)

    else:
        print('Upgrade Not Available\n')

def get_highest(seating_area):
    temp_list = []
    SD = 70
    for i in range(len(seating_area)):
        for j in range(len(seating_area[i])):
            if 'SD@' in seating_area[i][j]:
                temp_list.append(SD)
            if 'FC@' in seating_area[i][j]:
                temp_list.append(SD*10)
            if 'ER@' in seating_area[i][j]:
                temp_list.append(SD*1.1)
            if 'IF@' in seating_area[i][j]:
                temp_list.append(SD*0.1)
    print("Highest total spent by a customer = £", max(temp_list))

def main(state,seating_area):
    if state == 'start':
        choice = get_input(state, seating_area)
        if choice == '1':
            state = 'login'
        elif choice == '2':
            u = login.gen_user()
            p = login.gen_pass()
            data.write(u, e.encrypt(p))
            print('Your Username is', u)
            print('Your Password is', p)
            input('click enter to continue')
            state = 'start'
        else:
            quit()
    if state == 'login':
        choice = get_input(state, seating_area)
        if login.validate(*choice):
            state = 'menu'
        else:
            state = 'start'
            main(state,seating_area)
    if state == 'menu':
        choice = get_input(state, seating_area)
        if choice == '1':
            state = 'book_seat'
        elif choice == '2':
            state = 'cancel_seat'
        elif choice == '3':
            remaining_seats(seating_area)
            display_seats(seating_area)
            input('press any key to continue')
            state = 'menu'
        elif choice == '4':
            get_revenue(seating_area)
            input('press any key to continue')
            state = 'menu'
        elif choice == '5':
            get_average(seating_area)
            input('press any key to continue')
            state = 'menu'
        elif choice == '6':
            state = 'upgrade'
        elif choice == '7':
            get_highest(seating_area)
            input('press any key to continue')
            state = 'menu'
        elif choice == '8':
            quit()
    if state == 'book_seat':
        book_seat(state,seating_area)
        display_seats(seating_area)
        input('press any key to continue')
        state = 'menu'
    if state == 'cancel_seat':
        release_seat(state, seating_area)
        display_seats(seating_area)
        input('press any key to continue')
        state = 'menu'
    if state == 'upgrade':
        give_upgrade(state, seating_area)
        input('press any key to continue')
        state = 'menu'

    return state

def get_input(state, seating_area):
    os.system('cls')
    if state == 'start':
        message = 'Select 1 to login\nSelect 2 to create an account\nSelect 3 to quit'
        print(message)
        choice = input('\nSelect [1, 2 or 3] : ')
        if (choice == '1') or (choice == '2') or (choice == '3'):
            return choice
        else:
            get_input(state, seating_area)
    elif state == 'login':
        username = input('Enter your username : ')
        password = input('Enter your password : ')
        return [username, password]
    elif state == 'menu':
        message = "1 - Book A Ticket \n2 - Cancel A Reservation \n3 - Check Remaining Seats \n4 - Calculate Flight's Revenue \n5 - Calculate Average Ticket Price \n6 - Award A Free Upgrade \n7 - List The Highest Total \n8 - Exit The System\n"
        choice  = input(message)
        if (choice == '1') or (choice == '2') or (choice == '3') or (choice == '4') or (choice == '5') or (choice == '6') or (choice == '7') or (choice == '8'):
            return choice
        else:
            get_input(state, seating_area)
    elif state == 'book_seat':
        display_seats(seating_area)
        customer = input('Which customer are you? : \n')
        if (customer == 'A') or (customer == 'B') or (customer == 'C') or (customer == 'D') or (customer == 'E') or (customer == 'F') or (customer == 'G'):
            row = input('Which row would you like? : \n')
            if (row == '0') or (row == '1') or (row == '2') or (row == '3') or (row == '4') or (row == '5') or (row == '6') or (row == '7') or (row == '8') or (row == '9'):
                if (row == '0') or (row == '1') or (row == '2'):
                    seat = input('Pick a seat 1 or 2: \n')
                    if (seat == '0') or (seat == '1') or (seat == '2'):
                        pass
                    else:
                        get_input(state, seating_area)
                elif (row == '3') or (row == '4') or (row == '5') or (row == '6') or (row == '7') or (row == '8') or (row == '9'):
                    seat = input('Pick seat 1, 2, 3 or 4 : \n')
                    if (seat == '1') or (seat == '2') or (seat == '3') or (seat == '4'):
                        pass
                    else:
                        get_input(state, seating_area)
            else:
                get_input(state, seating_area)
        else:
            get_input(state, seating_area)
        input('press any key to continue')

        if row != '0' and seat != '0':
            row = int(row)
            seat = int(seat)

            if row <= 2:
                if seat == 2:
                    seat = 3
            elif row > 2:
                if seat >= 3:
                    seat += 1

            if '@' in seating_area[row-1][seat-1]:
                print('Cannot Book This Seat, Choose Another')
                input('press any key to continue')
                state = 'menu'
                return [-1,-1,-1]
            else:
                return [customer, row, seat]
        else:
            return [customer, row, seat]
    elif state == 'cancel_seat':
        display_seats(seating_area)
        row = input('Which seat would you like to release? : \n')
        if (row == '1') or (row == '2'):
            seat = input('Pick a seat 1 or 2: \n')
            if (seat == '1') or (seat == '2'):
                pass
            else:
                get_input(state, seating_area)
        elif (row == '3') or (row == '4') or (row == '5') or (row == '6') or (row == '7') or (row == '8') or (row == '9'):
            seat = input('Pick seat 1, 2, 3 or 4 : \n')
            if (seat == '1') or (seat == '2') or (seat == '3') or (seat == '4'):
                pass
            else:
                get_input(state, seating_area)
        else:
            get_input(state, seating_area)

        row = int(row)
        seat = int(seat)

        if row <= 2:
            if seat == 2:
                seat = 3
        elif row > 2:
            if seat >= 3:
                seat += 1

        return [row, seat]
    elif state == 'upgrade':
        booked = []

        for i in range(2, len(seating_area)):
            for j in range(len(seating_area[i])):
                if '@' in seating_area[i][j]:
                    booked.append([i,j])
                    print('1',seating_area[i][j], 'Has been booked')

        victim = input('who would you like to upgrade? : \n')
        return booked[int(victim)-1][0],booked[int(victim)-1][1]


while True:
    state = main(state, seating_area)
