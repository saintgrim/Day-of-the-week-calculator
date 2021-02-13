
def algorithm_part_one():
    month_values = {
        '01': 1.0,
        '02': 4.0,
        '03': 4,
        '04': 0,
        '05': 2,
        '06': 5,
        '07': 0,
        '08': 3,
        '09': 6,
        '10': 1,
        '11': 4,
        '12': 6
    }
    century = {
        '17': 4,
        '18': 2,
        '19': 0,
        '20': 6
    }
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: "Saturday"
    }
    import datetime
    from datetime import date
    step_one = input('(MM/DD/YYYY or MMDDYYYY)\n'
                     'Date: ').replace(' ', '').replace('/', '')

    def algorithm_part_two():
        step_two = int(int(step_one[6:]) / 4)
        step_three = step_two + int(step_one[2:4].replace('0', ''))
        step_four = int(step_three + month_values[step_one[0:2]])
        #  step five done in below if statements.
        step_six = step_four + century[step_one[4:6]]
        #  step seven ignored unless finding a Julian date.
        step_eight = step_six + int(step_one[6:])
        step_nine = step_eight % 7
        chosen_date = datetime.date(int(step_one[4:]), int(step_one[0:2]), int(step_one[2:4]))
        if chosen_date > date.today():
            print(f'{step_one[0:2]}/{step_one[2:4]}/{step_one[4:]} will be a {days[step_nine]}.')
        elif chosen_date == date.today():
            print(f'Today is a {days[step_nine]}.')
        elif chosen_date < date.today():
            print(f'{step_one[0:2]}/{step_one[2:4]}/{step_one[4:]} was a {days[step_nine]}.')

    # if statements check for leap year and subtract 1 from value if the selected month is Feb. or Jan.
    if (int(step_one[4:]) % 4) == 0 and month_values[step_one[0:2]] == 1.0:
        if (int(step_one[4:]) % 100) == 0 and month_values[step_one[0:2]] == 1.0:
            if (int(step_one[4:]) % 400) == 0 and month_values[step_one[0:2]] == 1.0:
                month_values['1'] = 0
                algorithm_part_two()
            else:
                algorithm_part_two()
        else:
            algorithm_part_two()
    elif (int(step_one[4:]) % 4) == 0 and month_values[step_one[0:2]] == 4.0:
        if (int(step_one[4:]) % 100) == 0 and month_values[step_one[0:2]] == 4.0:
            if (int(step_one[4:]) % 400) == 0 and month_values[step_one[0:2]] == 4.0:
                month_values['2'] = 3
                algorithm_part_two()
            else:
                algorithm_part_two()
        else:
            algorithm_part_two()
    else:
        algorithm_part_two()


if __name__ == '__main__':
    algorithm_part_one()
