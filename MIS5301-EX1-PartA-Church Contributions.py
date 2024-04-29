Total = 0
Average = 0
count = 0
gf = 0
MI = 0
bf = 0



print( '*' * 70)
print(f'{"Victorino Community Church - Contribution Management System":^70}')
print( '*' * 70,'\n')


print('='*40)
print(f'{"  MEMBER CONTRIBUTIONS DATA ENTRY":<30}')
print('='*40)

another_fund = 'y'
while another_fund.lower() == 'y':
    a = str(input('   Enter fund code: '))
    a = a.lower()
    b = float(input('   Enter Contribution amount: '))
    count +=1
    if a == 'gf':
        gf += b
        
    elif a == 'mi':
        MI += b
        
    elif a == 'bf':
        bf += b
        
    another_fund = input('      >>> Do you have any entry (y/n):')
        
Total = gf + MI + bf
Average = Total/count

balance = float(gf-11000)
OperatingExpense = float(0.2*balance)
ProgramExpense = float(0.8*balance)
Gtotal = float(MI + bf)

print()
print('='*40)
print('  FINANCIAL SUMMARY')
print('='*40, '\n')

print('   Contributions Summary')
print('  ','-'*33)

print(f'{"   General Fund         $":16s}' f'{gf:10,.2f}')
print(f'{"   Missions              ":16s}' f'{MI:10,.2f}')
print(f'{"   Building Fund         ":16s}' f'{bf:10,.2f}')

print('                         ','-'*10)

print(f'{"   Total                 ":16s}' f'{Total:>10,.2f}')
print(f'{"   Average               ":16s}' f'{Average:>10,.2f}')

print('\n')

print("   Planned Allocations")
print('  ','-'*33)
print(f'{"   General Fund":14s}')
Salaries = 9000.00
Averagee = 2000.00
print(f'{"      Salaries          $":14s}'  f'{Salaries:10,.2f}')
print(f'{"      Mortgage           ":14s}'  f'{Averagee:10,.2f}')
print(f'{"      Operating expenses ":14s}'  f'{OperatingExpense:10,.2f}')
print(f'{"      Program expenses   ":14s}'  f'{ProgramExpense:10,.2f}' f'{" <<< consider allocation":24s}')

print()

print("   Restricted Funds")
print(f'{"      Missions           ":<14}'  f'{MI:>10,.2f}')
print(f'{"      Building fund      ":<14}'  f'{bf:>10,.2f}')

print('                         ','-'*9)
print(f'{"   Total                 "}'  f'{Total:10,.2f}')
print()


AllocatePEF = input('>>> Would you like to allocate the Program Expense fund? ')
print()

Allocation1 = 0; Allocation2=0; Allocation3=0; alloc1=0; alloc2=0; alloc3=0
print('='*40)
print(f'{"   PROGRAM EXPENSE PLANNING":30s}')

print('='*40)
print()

print(f'{  "Funds available >>> $":20s}'f'{ProgramExpense:,.2f}')

print()


while AllocatePEF.lower() == 'y':
   programAllocation = int(input("Enter number of programs for allocation (max 3): "))
   if programAllocation == 1:
       print("   Program 1:")
       ProgramName1 = input("      Enter program name: ")
       Allocation1 = int(input("      Enter allocation %: "))
       alloc1 = (Allocation1/100)*ProgramExpense
       print(f'{"         >> Allocation amount: $":15s} ${alloc1:<8,.2f}')
       AllocatePEF = 'n'

   elif programAllocation == 2:
       print("   Program 1:")
       ProgramName1 = input("      Enter program name: ")
       Allocation1 = int(input("      Enter allocation %: "))
       alloc1 = (Allocation1/100)*ProgramExpense
       print(f'{"         >> Allocation amount: ":15s} ${alloc1:<8,.2f}')
       
       print("   Program 2:")
       ProgramName2 = input("      Enter program name: ")
       Allocation2 = int(input("      Enter allocation %: "))
       alloc2 = (Allocation2/100)*ProgramExpense
       print(f'{"         >> Allocation amount: ":15s} ${alloc2:<8,.2f}')
       AllocatePEF = 'n'
           
   elif programAllocation == 3:
       print("   Program 1:")
       ProgramName1 = input("      Enter program name: ")
       Allocation1 = int(input("      Enter allocation %: "))
       alloc1 = (Allocation1/100)*ProgramExpense
       print(f'{"         >> Allocation amount: ":15s} ${alloc1:<8,.2f}')
       
       print("   Program 2:")
       ProgramName2 = input("      Enter program name: ")
       Allocation2 = int(input("      Enter allocation %: "))
       alloc2 = (Allocation2/100)*ProgramExpense
       print(f'{"         >> Allocation amount:   ":15s} ${alloc2:<8,.2f}')
           
       print("   Program 3:")
       ProgramName3 = input("      Enter program name: ")
       Allocation3 = int(input("      Enter allocation %: "))
       alloc3 = (Allocation3/100) * ProgramExpense
       print(f'{"         >> Allocation amount:   ":15s} ${alloc3:<8,.2f}')
       AllocatePEF = 'n'

print('   Program Expense Allocations')
print('  ','-'*40)
T1 = alloc1 + alloc2 + alloc3
T2 = ProgramExpense - T1
Unallocated = 100 - (Allocation1 + Allocation2 + Allocation3)
if programAllocation == 1:
    print(f'{"   "}'f'{ProgramName1  :15s}      $ { alloc1:8,.2f} ({Allocation1}%)')
    print(f'{"   "}'f'{"Unallocated ":15s}          {T2:8,.2f} ({Unallocated}%)')
    Totall = Allocation1 + Unallocated
elif programAllocation == 2:
   print(f'{"   "}'f'{ProgramName1  :15s}       $ {alloc1:8,.2f} ({Allocation1}%)')
   print(f'{"   "}'f'{ProgramName2  :15s}       {alloc2:8,.2f} ({Allocation2}%)')
   print(f'{"   "}'f'{"Unallocated ":15s}           {T2:8,.2f} ({Unallocated}%)')
   Totall = Allocation1 + Allocation2 + Unallocated
elif programAllocation == 3:
   print(f'{"   "}'f'{ProgramName1  :15s}       $ {alloc1:8,.2f} ({Allocation1}%)')
   print(f'{"   "}'f'{ProgramName2  :15s}       {alloc2:8,.2f} ({Allocation2}%)')
   print(f'{"   "}'f'{ProgramName3  :15s}       {alloc3:8,.2f} ({Allocation3}%)')
   print(f'{"   "}'f'{"Unallocated ":15s}           {T2:8,.2f} ({Unallocated}%)') 
   
Totall = Allocation1 + Allocation2 + Allocation3 + Unallocated
print('                            ','-'*8)
print(f'{"   Total                     ":15s}' f'{ProgramExpense:8,.2f}' f' ({Totall}%)')

print()
print('Contribution Management System (c) 2023')