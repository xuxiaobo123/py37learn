"""Test user's favourite Integrated Circuit."""
#3.7新特性，断点调试，只需异常语句处输入breakpoints(),然后执行在控制台（Pdb）输入locals()即可比较结果

def test_ic(favourite_ic):
    user_guess = input("Try to guess our favourite IC >>> ")
    #breakpoint()

    if user_guess == favourite_ic:
        return "Yup, that's our favourite!"
    else:
        return "Sorry, that's not our favourite IC"


if __name__ == '__main__':
    favourite_ic = 555
    print(test_ic(favourite_ic))
