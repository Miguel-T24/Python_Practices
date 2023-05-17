# 109. Write a python program that counts the number of leap ywars within the range of years. Range of years should be accepted as string

def test(r_years):
	start_year, end_year = map(int, r_years.split('-'))
	return sum(is_leap_year(year) for year in range(start_year, end_year+1))
def is_leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False

text ="1981-1991"
print("Range of years:", text)
print("Count  the number of leap years within the said range:")
print(test(text))
text ="2000-2020"
print("Range of years:", text)
print("Count  the number of leap years within the said range:")
print(test(text))