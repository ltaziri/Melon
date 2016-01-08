


def report_revenue(orders_by_type):
    """"reports how much revenue was generated per melon type"""
    
    melon_log = open(orders_by_type)
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    for line in melon_log:  #counts how many of each melon were sold
        melon_data = line.split("|")
        melon_type = melon_data[1]
        melon_count = int(melon_data[2])
        melon_tallies[melon_type] += melon_count

    melon_log.close()

    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

    total_revenue = 0
    for melon_type in melon_tallies: #calculates revenue per melon type
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold {} {} melons at ${:.2f} each for a total of ${:,.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)


def report_salesperson_revenue(salestype_log):
    """reports salesperson revenue and online revenue"""

    sales_log = open(salestype_log)
    salesperson_revenue = 0
    online_revenue = 0
    for line in sales_log:
        sales_data = line.split("|")
        if sales_data[1] == "0":
            salesperson_revenue += float(sales_data[3])
        else:
            online_revenue += float(sales_data[3])
    print "Salespeople generated ${:,.2f} in revenue.".format(salesperson_revenue)
    print "Internet sales generated ${:,.2f} in revenue.".format(online_revenue)
    if salesperson_revenue > online_revenue:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"
    print "*" * 80

    sales_log.close()


print "*" * 80

report_revenue("orders-by-type.txt")

print "*" * 80

report_salesperson_revenue("orders-with-sales.txt")
