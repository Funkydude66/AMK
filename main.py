print ("LIQUIDITY CALCULATOR")

entrypoint = float (input('ENTRY POINT:'));
amount = float (input('AMOUNT:'));
totalprice = (entrypoint*amount);
print('TOTAL PRICE:',totalprice) 
accbal = float (input('ACCOUNT BAL:'))
loan = (totalprice/accbal)  
potion = (entrypoint/loan)
liquidation = (entrypoint-potion)
print('LIQUIDATION:',liquidation)
print('Calcualtor by creativespace')
 

