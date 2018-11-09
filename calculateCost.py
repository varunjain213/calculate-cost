cost = 0

def calculateCostMultiple(liters, perLtrCosts, costs):
   minPerLtrCost = perLtrCosts[0]
   minPerLtrCostIndex = 0
   for j in range(len(costs)):
      if perLtrCosts[j] < minPerLtrCost:
         minPerLtrCost = perLtrCosts[j]
         minPerLtrCostIndex = j
   unitsNeeded = liters / pow(2, minPerLtrCostIndex)
   return costs[minPerLtrCostIndex] * unitsNeeded

def calculateCostRecurse(liters, perLtrCosts, costs):
   global cost
   if (liters <= 0):
      return
   index = 0
   temp = liters
   while temp != 1:
      temp = temp / 2
      index += 1
   if index > (len(costs) - 1):
      index = len(costs) - 1
      units = liters / pow(2, index)
      cost += units * calculateCostMultiple(pow(2, index), perLtrCosts, costs)
      litersRem = liters - (units * pow(2, index))
      calculateCostRecurse(litersRem, perLtrCosts, costs)
      return
   litersThisIter = pow(2, index)
   minPerLtrCost = perLtrCosts[0]
   minPerLtrCostIndex = 0
   for j in range(index + 1):
      if perLtrCosts[j] < minPerLtrCost:
         minPerLtrCost = perLtrCosts[j]
         minPerLtrCostIndex = j
   unitsNeeded = litersThisIter / pow(2, minPerLtrCostIndex)
   costThisIter = costs[minPerLtrCostIndex] * unitsNeeded
   minCostPostIndex = pow(10, 40)
   if minPerLtrCostIndex < (len(costs) - 1):
      minCostPostIndex = costs[minPerLtrCostIndex + 1]
      for k in range(minPerLtrCostIndex + 1, len(costs)):
          if costs[k] <= minCostPostIndex:
             minCostPostIndex = costs[k]
   if minCostPostIndex <= costThisIter:
      cost += minCostPostIndex
      return
   cost += costThisIter
   litersRemaining = liters - litersThisIter
   calculateCostRecurse(litersRemaining, perLtrCosts, costs)
   return

if __name__ == "__main__":
    liters = 787787787
    costs = [123456789, 234567890, 345678901, 456789012, 987654321]
#    liters = 3
#    costs = [10, 100, 1000, 10000]
#    liters = 3
#    costs = [10000, 1000, 100, 10]
#    liters = 12
#    costs = [20, 30, 70, 90]
    perLtrCosts = []
    for i in range(len(costs)):
       perLtrCosts += [costs[i] / pow(2, i)]
    calculateCostRecurse(liters, perLtrCosts, costs)
    print 'cost is {}'.format(cost)
