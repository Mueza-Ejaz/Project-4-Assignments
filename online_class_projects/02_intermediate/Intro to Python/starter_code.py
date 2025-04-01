# Planetary WeightsDownload Project:

# constant variable:
MARS_GRAVITY = 0.378 # Mars' gravity compared to Earth's gravity

def main():
    # user input
    earth_weight = float(input('Enter a weight on Earth: '))

    # calculate equivalent weight of mars:
    mars_weight = earth_weight * MARS_GRAVITY

    # rounded mars weight of two decimal places:
    rounded_mars_weight = round(mars_weight, 2)

    print(f"The equivalent weight on Mars: {rounded_mars_weight} \n") 

main()

# output:
# Enter a weight on Earth: 50
# The equivalent weight on Mars: 18.9 






