def main():
    time_input = input("What time is it? ")
    time_float = convert(time_input)

    if 7.0 <= time_float <= 8.0:
        print("Breakfast Time")
    elif 12.0 <= time_float <= 13.0:
        print("Lunch Time")
    elif 18.0 <= time_float <= 19.0:
        print("Dinner Time")
    else:
        print("Have some patience! It's not meal time yet...")

def convert(time_value):
    
    # Convert string to float, leading zeroes are ignored due to conversion
    hour, minute = map(float, time_value.split(":"))
    return hour + minute / 60

if __name__ == "__main__":
    main()