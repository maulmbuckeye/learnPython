def main():

    number = 0
    total = 0.0
    highest = 0
    lowest = 9999.999

    try:
        in_file = open("donations.txt", "r")

        for line in in_file:

            donation = float(line.split(",")[1])
            if donation > highest:
                highest = donation

            if donation < lowest:
                lowest = donation

            number += 1
            total += donation

            average = total / number

        in_file.close()

        print ("The highest amount is $%.2f" %highest)
        print ("The lowest amount is $%.2f" %lowest)
        print ("The total donation is $%.2f" %total)
        print ("The average is $%.2f" %average)

    except IOError:
        print ("No such file")

    except ValueError:
        print ("Non-numeric data found in the file.")


main()