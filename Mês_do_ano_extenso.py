def get_month_name(month):
    
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    return months.get(month, "Mês Inválido")

user_input = int(input("Digite o número do mês "))

month_name = get_month_name(user_input)

print(month_name)
