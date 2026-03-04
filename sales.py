while True:
    try:
        n = int(input("Enter number of days: "))
        
        if n <= 0:
            print("Number of days must be positive. Try again.")
            continue
        
        break  
    except ValueError:
        print("Invalid input. Please enter an integer.")
sales = []
days = []
c = 1
while c <= n:
         try:
             a = int(input(f'Enter the sales for day {c}: '))
             if a >= 0:
               sales.append(a)
               days.append(f'Day {c}')
               c += 1 
             else:
                print("Invalid input! Sales cannot be negative. Try again.")
        
         except ValueError:
             print("Invalid input! Please enter a number.")
  


    print('Highest sales: ',max(sales))
    print('Day of highest sales: Day ', sales.index(max(sales))+1)
    print('Lowest sales: ',min(sales))
    print('Day of lowest sales: Day ', sales.index(min(sales))+1)
    print('Average sales: ', sum(sales)/len(sales))

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 2, figsize=(14, 4))  
    ax[0].plot(days, sales, marker='o', color='red', label='Sales per day')
    ax[0].set_title('Line Graph')
    ax[0].set_xlabel('Days')
    ax[0].set_ylabel('Sales (units)')
    ax[0].grid(True)
    ax[0].legend()


    ax[1].bar(days, sales, color='skyblue', label='Sales per day')
    ax[1].set_title('Bar Graph')
    ax[1].set_xlabel('Days')
    ax[1].set_ylabel('Sales (units)')
    ax[1].grid(axis='y', linestyle='--', alpha=0.2)
    ax[1].legend()

    for i, v in enumerate(sales):
        ax[1].text(i, v + 0.5, str(v), ha='center')
  
    plt.tight_layout()
    plt.show()

   




