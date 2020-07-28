year_str = input('あなたの生まれた年を西暦４桁で入力してください: ')
year = int(year_str)
number_of_eto = (year + 8) % 12
print('あなたの干支の順番は', number_of_eto, '番です。')
