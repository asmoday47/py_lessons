from lesson4_dop import sal_counter

def sal_counter (sal_val, sal_time,sal_prem):
    sal_sum = sal_val * sal_time + sal_prem
    return sal_sum

sval = float(input("Введите ставку сотрудника в час"))
stime = float(input("Введите количество отработанных часов"))
sprem = float(input("Введите сумму премии"))

print(sal_counter(sval,stime,sprem))
