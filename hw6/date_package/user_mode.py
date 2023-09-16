from date_check import make_date_list_from_string as ml, date_exists as de


def user_input():
    date = input('Type the date in this format YYYY.MM.DD\n'
                 'to separate year, day, month use one of symbols >>> .,/-:\\\n'
                 '>>>  ')

    if ml(date):

        print(f'Date year = {ml(date)[0]}, month = {ml(date)[1]}, day = {ml(date)[2]} '
              f'{"does not" * (not de(ml(date)))} exist{"s" * de(ml(date))}')
    else:
        print(f'Incorrect input')
