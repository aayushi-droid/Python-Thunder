def compound_interest(p, t, r, n):
	return round(p * (1 + (r / n))**(n * t), 2)
