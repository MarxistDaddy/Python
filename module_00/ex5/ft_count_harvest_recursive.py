def ft_count_harvest_recursive():
	Days = int(input("Days until harvest: "))
	def count_harvest(days):
	  if (days > Days):
	    print("Harvest time!")
	    return
	  print("Day ", days)
	  count_harvest(days + 1)	     

	count_harvest(1)
