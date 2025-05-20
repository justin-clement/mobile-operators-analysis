import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Colors to be used for visualizing the mobile networks.
green = '#28a745'
red = '#e40000'
yellow = '#ffcc01'
d_green = '#0f5132'


# Dataset of Glo plans.
glo = {
	'Daily & Weekly': {
	'plan': ['45MB Daily', '125MB Daily', '260MB 2-Day', 
			'1.5GB Weekly', '1.1GB 2-Week', '3.5GB Weekly', 
			'6GB Weekly', '8.5GB Weekly', '23GB Weekly'],
	'value_day': [0.039, 0.107, 0.215, 0.488, 1.1, 1.5, 4, 6, 20],
	'value_night': [0.0049, 0.0146, 0.0391, 1, 0, 2, 2, 2.5, 3],
	'cost': [50, 100, 200, 500, 750, 1000, 1500, 2000, 5000],
	'duration': [1, 1, 2, 7, 14, 7, 7, 7, 7]
	},

	'Monthly': {
	'plan': ['2.6GB Monthly', '5GB Monthly', '6.25GB Monthly', 
				'7.5GB Monthly', '11GB Monthly', '14GB Monthly', 
				'18GB Monthly', '22GB Monthly', '29GB Monthly', 
				'40GB Monthly', '69GB Monthly', '110GB Monthly'],
	'value_day': [1.1, 2, 3.25, 4.5, 8, 11, 14, 18, 25, 36, 65, 105],
	'value_night': [1.5, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5],
	'cost': [1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 8000, 
				10000, 15000, 20000],
	'duration': [30 for i in range(12)]
	},

	'Mega': {
	'plan': ['135GB Monthly Mega','165GB Monthly Mega', '220GB Monthly Mega', 
			'225GB Monthly Mega', '320GB 2-Month Mega', '380GB 3-Month Mega', 
			'475GB 3-Month Mega', '1TB Annual Mega'],
	'value': [135, 165, 220, 225, 320, 380, 475, 1024],
	'cost': [25000, 30000, 36000, 40000, 50000, 60000, 75000, 100000],
	'duration': [30, 30, 30, 30, 60, 90, 90, 365]
	},

	'Special': {
	'plan': ['2GB 2-Day Special', '6GB Weekly Special'],
	'value_day': [1, 4],
	'value_night': [1, 2],
	'cost': [500, 1500],
	'duration': [2, 7]
	},

	'G-cafe': {
	'plan': ['750MB Daily (G-cafe)', '1.5GB Daily (G-cafe)', 
			'2.5GB 2-Day (G-cafe)', '10GB Weekly (G-cafe)'],
	'value': [0.732, 1.5, 2.5, 10],
	'cost': [200, 300, 500, 2000],
	'duration': [1, 1, 2, 7]
	},

	'Campus Booster': {
	'plan': ['235MB Daily (CB)', '480MB 2-Day (CB)', '2GB Weekly (CB)', 
			'4.2GB Monthly (CB)'],
	'value_day': [220, 440, 1024, 2248],
	'value_night': [15, 40, 1024, 2048],
	'cost': [100, 200, 500, 1000],
	'duration': [1, 2, 7, 30]   
	}
}


# Dataset of MTN plans.
mtn = {
	'Daily': {
	'plan': ['400MB Hourly', '75MB Daily', '120MB Daily',
			'250MB Daily', '500MB Daily', '1GB Daily',
			'1.5GB Daily','2.5GB Daily (App)'],
	'value': [400, 75, 120, 250, 500, 1024, 1536, 2560],
	'cost': [100, 75, 100, 200, 350, 350, 400, 750],
	'duration': [1 for i in range(8)]
	},

	'2-Day': {
	'plan': ['1GB 2-Day', '1.4GB 2-Day', '2GB 2-Day',
			'2.5GB 2-Day', '3.2GB 2-Day'],
	'value': [1, 1.4, 2, 2.5, 3.2],
	'cost': [500, 600, 750, 900, 1000],
	'duration': [2 for i in range(5)]
	},

	'Weekly': {
	'plan': ['500MB Weekly', '1GB Weekly', '1.5GB Weekly',
			'5GB Weekly', '7GB Weekly', '1.2GB Pulse Weekly'],
	'value': [0.488, 1, 1.5, 5, 7, 1.2],
	'cost': [500, 800, 1000, 1500, 3000, 700],
	'duration': [7 for i in range(6)]
	},

	'Monthly': {
	'plan': ['1.8GB Monthly', '2.7GB Monthly', '4.25GB Monthly',
			'5.5GB Monthly', '8GB Monthly', '11GB Monthly',
			'15GB Monthly', '20GB Monthly', '25GB Monthly',
			'32GB Monthly', '50GB Monthly', '75GB Monthly',
			'150GB Monthly', '250GB Monthly'],
	'value': [1.8, 2.7, 4.25, 5.55, 8, 11, 15, 20, 25, 32, 50, 
				75, 150, 250],
	'cost': [1500, 2000, 3000, 3500, 4500, 5000, 6500, 7500,
			9000, 11000, 16000, 20000, 35000, 55000],
	'duration': [30 for i in range(14)]
	},

	'Bi-Monthly to Quarterly': {
	'plan': ['90GB 2-Month', '150GB 2-Month', '200GB 2-Month',
			'480GB 3-Month'],
	'value': [90, 150, 200, 480],
	'cost': [25000, 40000, 50000, 120000],
	'duration': [60, 60, 60, 90]
	},
}


# Dataset of Airtel plans.
airtel = {
	'Daily': {
	'plan': ['75MB Daily', '100MB Daily', '200MB 2-Day',
			'300MB 2-Day'],
	'value': [40, 100, 200, 300],
	'cost': [75, 100, 200, 300],
	'duration': [1, 1, 2, 2]
	},

	'Daily (Opay-accessible)': {
	'plan': ['1GB Daily', '1.5GB 2-Day', '2GB 2-Day', 
			'3GB 2-Day', '5GB 2-Day'],
	'value': [1, 1.5, 2, 3, 5],
	'cost': [500, 600, 750, 1000, 1500],
	'duration': [1, 2, 2, 2, 2]
	},

	'Weekly': {
	'plan': ['500MB Weekly', '1GB Weekly', '1.5GB Weekly',
			'3.5GB Weekly', '6GB Weekly', '10GB Weekly', 
			'18GB Weekly'],
	'value': [0.488, 1, 1.5, 3.5, 6, 10, 18],
	'cost': [500, 800, 1000, 1500, 2500, 3000, 5000],
	'duration': [7 for i in range(7)]
	},

	'Monthly': {
	'plan': ['2GB Monthly', '3GB Monthly', '4GB Monthly',
			'8GB Monthly', '10GB Monthly', '13GB Monthly',
			'18GB Monthly', '25GB Monthly', '35GB Monthly',
			'60GB Monthly', '100GB Monthly', '160GB Monthly',
			'210GB Monthly'],
	'value': [2, 3, 4, 8, 10, 13, 18, 25, 35, 60, 100, 160, 210],
	'cost': [1500, 2000, 2500, 3000, 4000, 5000, 6000,
			8000, 10000, 15000, 20000, 30000, 40000],
	'duration': [30 for i in range(13)]
	},

	'Quarterly to Annual': {
	'plan': ['300GB 3-Month', '350GB 6-Month', '650GB Yearly'],
	'value': [300, 350, 650],
	'cost': [50000, 60000, 100000],
	'duration': [90, 120, 365]
	},

	'Everyday On': {
	'plan': ['500MB/day Monthly', '1.33GB/day Monthly'],
	'value': [15, 40],
	'cost': [3000, 7500],
	'duration': [30, 30]
	}
}


# Dataset of 9mobile plans.
mobile9 = {
	'Daily & Weekly': {
	'plan': ['50MB Daily', '100MB Daily', '300MB Daily',
			'650MB Daily', '1GB Daily', '2GB 3-Day',
			'7GB Weekly'],
	'value': [50, 100, 300, 650, 1024, 2048, 7168],
	'cost': [50, 100, 150, 200, 300, 500, 1500],
	'duration': [1, 1, 1, 1, 1, 3, 7]
	},

	'Monthly & Bi-Monthly': {
	'plan': ['4.2GB Monthly', '6.5GB Monthly', '9.5GB Monthly',
			'11GB Monthly', '12GB Monthly', '18.5GB Monthly',
			'225GB 2-Month'],
	'value_day': [2, 2.5, 5.5, 7, 12, 15, 225],
	'value_night': [2.2, 4, 4, 4, 0, 3.5, 0],
	'total_value': [4.2, 6.5, 9.5, 11, 12, 18.5, 225],
	'cost': [1000, 1200, 2000, 2500, 3000, 4000, 30000],
	'duration': [30, 30, 30, 30, 30, 30, 60]
	},

	'Quarterly to Annual': {
	'plan': ['75GB 3-Month', '425GB 3-Month', '165GB 6-Month', 
			'600GB 6-Month', '1TB Annual'],
	'value': [75, 425, 165, 600, 1024],
	'cost': [25000, 50000, 50000, 70000, 100000],
	'duration': [90, 90, 180, 180, 365]
	},

	'Opay-accessible': {
	'plan': ['22GB Monthly'],
	'value': [22],
	'cost': [5000],
	'duration': [30]
	}	
}


# Methods to visualize Glo plans.
class Glo:
	# global glo

	def bar_chart(plan_category: str):
		"""Visualize the value-cost of Glo data plans in a specific category. 
		Enter keys from the Glo dataset."""

		plans_df = pd.DataFrame(glo[plan_category])
		plans = np.array(plans_df['plan'])
		if 'value_day' in plans_df or 'value_night' in plans_df:
			day_data = np.array(plans_df['value_day'])
			night_data = np.array(plans_df['value_night'])
			total_data = day_data + night_data
		else:
			total_data = np.array(plans_df['value'])
		cost = np.array(plans_df['cost'])

		if 'value_day' in plans_df or 'value_night' in plans_df:
			vpc_day_array = day_data / cost
			vpc_array = total_data / cost
			plan_and_day_vpc = list(zip(plans, vpc_day_array))	
		else:
			vpc_array = total_data / cost
			
		plan_and_vpc = list(zip(plans, vpc_array))

		if 'value_day' in plans_df or 'value_night' in plans_df:
			day_vpc_values = []
			names = []
			for item in plan_and_day_vpc:
				day_vpc_values.append(item[1])
				names.append(item[0])

			for i in range(len(names)):
				plt.text(names[i], day_vpc_values[i]+0.00008, f"\u20A6{cost[i]}",
					ha='center', fontsize=12)

			plt.bar(names, day_vpc_values, color=green, width=0.5)
			plt.title(f'Glo {plan_category} Plans (daylight value)')
			plt.xticks(names, rotation=20)
			plt.yticks([])
			plt.show()
		
		vpc_values = []
		plan_names = []
		for item in plan_and_vpc:
			vpc_values.append(item[1])
			plan_names.append(item[0])

		for i in range(len(plan_names)):
			plt.text(plan_names[i], vpc_values[i]+0.00005, f"\u20A6{cost[i]}",
				ha='center', fontsize=12)

		plt.bar(plan_names, vpc_values, color=green, width=0.5)
		plt.title(f'Glo {plan_category} Plans (day + night value)')
		plt.xticks(plan_names, rotation=20)
		plt.yticks([])
		plt.show()

	def bestplans():
		"""Visualize the best Glo plans as bar charts."""

		bestplans = {
		'plan': ['6GB Weekly', '8.5GB Weekly', '23GB Weekly', '40GB Monthly', 
				'69GB Monthly', '110GB Monthly', '18GB Monthly', '22GB Monthly', 
				'29GB Monthly', '2GB 2-Day Special', '6GB Weekly Special', 
				'220GB Monthly Mega', '320GB 2-Month Mega', '1TB Annual Mega', 
				'1.5GB Daily (G-cafe)', '2.5GB Daily (G-cafe)', '10GB Weekly (G-cafe)', 
				'480MB 2-Day (CB)', '4.2GB Monthly (CB)'],
		'value': [4, 6, 20, 36, 65, 105, 14, 18, 25, 1, 4, 220, 320, 1024, 1.5, 2.5, 10, 0.43, 2.2],
		'cost': [1500, 2000, 5000, 10000, 15000, 20000, 5000, 6000, 
				8000, 500, 1500, 36000, 50000, 100000, 300, 500, 2000, 200, 1000]
		}

		best = pd.DataFrame(bestplans)
		names = best['plan']
		values = best['value']
		costs = best['cost']
		best['vpc'] = values / costs
		sorted_best = best.sort_values(by='vpc', ascending=True)

		for i in range(len(sorted_best['plan'])):
			plt.text(sorted_best['vpc'][i]+0.00002, sorted_best['plan'][i], 
				f"\u20A6{sorted_best['cost'][i]}", fontsize=9, va='center')

		plt.barh(sorted_best['plan'], sorted_best['vpc'], color=green)
		plt.title('Best Value Glo Plans')
		plt.yticks(names)
		plt.xticks([])
		plt.show()


# Methods to visualize MTN plans.
class Mtn:

	def bar_chart(plan_category: str):
		"""Visualize the value-cost of MTN data plans in a specific category. 
		Enter keys from the MTN dataset."""

		plans_df = pd.DataFrame(mtn[plan_category])
		plans = np.array(plans_df['plan'])
		total_data = np.array(plans_df['value'])
		cost = np.array(plans_df['cost'])

		vpc_array = total_data / cost	
		plan_and_vpc = list(zip(plans, vpc_array))
		
		vpc_values = []
		plan_names = []
		for item in plan_and_vpc:
			vpc_values.append(item[1])
			plan_names.append(item[0])

		for i in range(len(plan_names)):
			plt.text(plan_names[i], vpc_values[i]+0.00005, f"\u20A6{cost[i]}",
				ha='center', fontsize=12)


		plt.bar(plan_names, vpc_values, color=yellow, width=0.5)
		plt.title(f'MTN {plan_category} Plans')
		plt.xticks(plan_names, rotation=20)
		plt.yticks([])
		plt.show()

	def bestplans():
		"""Visualize the best MTN plans as bar charts."""

		bestplans = {
		'plan': ['3.2GB 2-Day', '2.5GB 2-Day', '2GB 2-Day', 
				'480GB 3-Month', '200GB 2-Month', '150GB 2-Month', 
				'2.5GB Daily (App)', '1.5GB Daily', '1GB Daily',
				'250GB Monthly', '150GB Monthly', '75GB Monthly',
				'1.2GB Pulse Weekly', '7GB Weekly', '5GB Weekly'],
		'value': [3.2, 2.5, 2, 480, 200, 150, 2.5, 
					1.5, 1, 250, 150, 75, 1.2, 7, 5],
		'cost': [1000, 900, 750, 120000, 50000, 40000, 750, 
				400, 300, 55000, 35000, 20000, 700, 3000, 1500]
		}

		best = pd.DataFrame(bestplans)
		names = best['plan']
		values = best['value']
		costs = best['cost']
		best['vpc'] = values / costs
		sorted_best = best.sort_values(by='vpc', ascending=True)

		for i in range(len(sorted_best['plan'])):
			plt.text(sorted_best['vpc'][i]+0.00002, sorted_best['plan'][i], 
				f"\u20A6{sorted_best['cost'][i]}", fontsize=9, va='center')

		plt.barh(sorted_best['plan'], sorted_best['vpc'], color=yellow)
		plt.title('Best Value MTN Plans')
		plt.yticks(names)
		plt.xticks([])
		plt.show()


# Methods to visualize Airtel plans.
class Airtel:

	def bar_chart(plan_category: str):
		"""Visualize the value-cost of Airtel data plans in a specific category. 
		Enter keys from the Airtel dataset."""
		plans_df = pd.DataFrame(airtel[plan_category])
		plans = np.array(plans_df['plan'])
		total_data = np.array(plans_df['value'])
		cost = np.array(plans_df['cost'])

		vpc_array = total_data / cost	
		plan_and_vpc = list(zip(plans, vpc_array))
		
		vpc_values = []
		plan_names = []
		for item in plan_and_vpc:
			vpc_values.append(item[1])
			plan_names.append(item[0])

		for i in range(len(plan_names)):
			plt.text(plan_names[i], vpc_values[i]+0.00005, f"\u20A6{cost[i]}",
				ha='center', fontsize=12)

		plt.bar(plan_names, vpc_values, color=red, width=0.5)
		plt.title(f'Airtel {plan_category} Plans')
		plt.xticks(plan_names, rotation=20)
		plt.yticks([])
		plt.show()

	def bestplans():
		"""Visualize the best Airtel plans as bar charts."""
		
		bestplans = {
		'plan': ['300MB 2-Day', '200MB 2-Day', '210GB Monthly', 
				'160GB Monthly', '100GB Monthly', '8GB Monthly', 
				'650GB Yearly', '300GB 3-Month', '350GB 6-Month', 
				'18GB Weekly', '10GB Weekly', '6GB Weekly', 
				'5GB 2-Day (Opay)', '3GB 2-Day (Opay)', '2GB 2-Day (Opay)'],
		'value': [0.29, 0.20, 210, 160, 100, 8, 650, 300, 350, 
					18, 10, 6, 5, 3, 2],
		'cost': [300, 200, 40000, 30000, 20000, 3000, 100000, 
				50000, 60000, 5000, 3000, 2500, 1500, 1000, 750]
		}

		best = pd.DataFrame(bestplans)
		names = best['plan']
		values = best['value']
		costs = best['cost']
		best['vpc'] = values / costs
		vpc = best['vpc']
		sorted_best = best.sort_values(by='vpc', ascending=True)

		for i in range(len(sorted_best['plan'])):
			plt.text(sorted_best['vpc'][i]+0.00002, sorted_best['plan'][i], 
				f"\u20A6{sorted_best['cost'][i]}", fontsize=9, va='center')

		plt.barh(sorted_best['plan'], sorted_best['vpc'], color=red)
		plt.title('Best Value Airtel Plans')
		plt.yticks(names)
		plt.xticks([])
		plt.show()


# Methods to visualize 9mobile plans.
class Mobile_9:

	def bar_chart(plan_category: str):
		"""Visualize the value-cost of 9mobile data plans in a specific category. 
		Enter keys from the 9mobile dataset."""

		plans_df = pd.DataFrame(mobile9[plan_category])
		plans = np.array(plans_df['plan'])
		if 'value_day' in plans_df or 'value_night' in plans_df:
			day_data = np.array(plans_df['value_day'])
			night_data = np.array(plans_df['value_night'])
			total_data = day_data + night_data
		else:
			total_data = np.array(plans_df['value'])
		cost = np.array(plans_df['cost'])

		if 'value_day' in plans_df or 'value_night' in plans_df:
			vpc_day_array = day_data / cost
			vpc_array = total_data / cost
			plan_and_day_vpc = list(zip(plans, vpc_day_array))	
		else:
			vpc_array = total_data / cost
			
		plan_and_vpc = list(zip(plans, vpc_array))

		if 'value_day' in plans_df or 'value_night' in plans_df:
			day_vpc_values = []
			names = []
			for item in plan_and_day_vpc:
				day_vpc_values.append(item[1])
				names.append(item[0])

			for i in range(len(names)):
				plt.text(names[i], day_vpc_values[i]+0.0001, f"\u20A6{cost[i]}",
					ha='center', fontsize=12)

			plt.bar(names, day_vpc_values, color=d_green, width=0.5)
			plt.title(f'9mobile {plan_category} Plans (daylight value)')
			plt.xticks(names, rotation=20)
			plt.yticks([])
			
			plt.show()
		
		vpc_values = []
		plan_names = []
		for item in plan_and_vpc:
			vpc_values.append(item[1])
			plan_names.append(item[0])

		for i in range(len(plan_names)):
			plt.text(plan_names[i], vpc_values[i]+0.06, f"\u20A6{cost[i]}",
				ha='center', fontsize=12)

		plt.bar(plan_names, vpc_values, color=d_green, width=0.5)
		plt.title(f'9mobile {plan_category} Plans')
		plt.xticks(plan_names, rotation=20)
		plt.yticks([])
		plt.show()

	def bestplans():
		"""Visualize the best 9mobile plans as bar charts."""

		bestplans = {
		'plan': ['7GB Weekly', '2GB 3-Day', '1GB Daily', 
				'225GB 2-Month', '12GB Monthly', '18.5GB Monthly', 
				'425GB 3-Month', '600GB 6-Month', '1TB Annual'],
		'value': [7, 2, 1, 225, 12, 15, 425, 600, 1024],
		'cost': [1500, 500, 300, 30000, 3000, 4000, 50000, 70000, 
				100000]
		}

		best = pd.DataFrame(bestplans)
		names = best['plan']
		values = best['value']
		costs = best['cost']
		best['vpc'] = values / costs
		vpc = best['vpc']
		sorted_best = best.sort_values(by='vpc', ascending=True)

		for i in range(len(sorted_best['plan'])):
			plt.text(sorted_best['vpc'][i]+0.00002, sorted_best['plan'][i], 
				f"\u20A6{sorted_best['cost'][i]}", fontsize=9, va='center')

		plt.barh(sorted_best['plan'], sorted_best['vpc'], color=d_green)
		plt.title('Best Value 9mobile Plans')
		plt.yticks(names)
		plt.xticks([])
		plt.show()


# Dataset of all networks' best plans.
best_plans_all = {
	'Daily to Weekly': {
	'plan': ['9mobile 1GB Daily', '9mobile 2GB 3-Day', '9mobile 7GB Weekly',

			'Airtel 200MB 2-Day', 'Airtel 6GB Weekly', 'Airtel 10GB Weekly', 
			'Airtel 18GB Weekly', 

			'Glo 1.5GB Daily (G-cafe)', 'Glo 2.5GB 2-Day (G-cafe)', 'Glo 10GB Weekly (G-cafe)', 
			'Glo 2GB 2-Day Special', 'Glo 6GB Weekly Special', 'Glo 480MB 2-Day (CB)',

			'MTN 1.2GB Pulse Weekly', 'MTN 7GB Weekly', 'MTN 2GB 2-Day', 
			'MTN 2.5GB 2-Day', 'MTN 3.2GB 2-Day', 'MTN 2.5GB Daily (App)', 
			'MTN 1GB Daily', 'MTN 5GB Weekly', 'MTN 1.5GB Daily'],
	'value': [1, 2, 7, 0.2, 6, 10, 18, 1.5, 2.5, 10, 1, 4, 0.43,
				1.2, 7, 2, 2.5, 3.2, 2.5, 1, 5, 1.5],
	'cost': [300, 500, 1500, 200, 2500, 3000, 5000, 
			300, 500, 2000, 500, 1500, 200,
			700, 3000, 750, 900, 1000, 750, 350, 1500, 400],
	'color': [d_green, d_green, d_green, 
			red, red, red, red, 
			green, green, green, green, green, green, 
			yellow, yellow, yellow, yellow, yellow, yellow, 
			yellow, yellow, yellow]
	},

	'Monthly': {
	'plan': ['9mobile 18.5GB Monthly', '9mobile 12GB Monthly', 

			'Airtel 8GB Monthly', 'Airtel 100GB Monthly', 
			'Airtel 210GB Monthly', 'Airtel 160GB Monthly', 

			'Glo 220GB Monthly Mega', 'Glo 110GB Monthly', 'Glo 69GB Monthly', 
			'Glo 40GB Monthly',

			'MTN 75GB Monthly', 'MTN 150GB Monthly', 'MTN 250GB Monthly'],
	'value': [15, 12, 8, 100, 210, 160, 220, 105, 65, 36,  
				75, 150, 250],
	'cost': [4000, 3000, 3000, 20000, 40000, 30000, 36000, 20000, 15000, 
			10000, 20000, 35000, 55000],
	'color': [d_green, d_green, red, red, red, red, green, 
				green, green, green, yellow, yellow, yellow]
	},

	'Mid-range Monthly': {
	'plan': ['MTN 4.25GB Monthly', 'MTN 5.5GB Monthly', 'MTN 8GB Monthly', 
			'MTN 11GB Monthly', 'MTN 15GB Monthly', 'MTN 20GB Monthly',

			'Glo 29GB Monthly', 'Glo 22GB Monthly', 'Glo 18GB Monthly', 
			'Glo 4.2GB Monthly (CB)',

			'Airtel 8GB Monthly', 'Airtel 10GB Monthly', 'Airtel 13GB Monthly', 
			'Airtel 18GB Monthly', 'Airtel 25GB Monthly', 

			'9mobile 9.5GB Monthly', '9mobile 11GB Monthly', '9mobile 12GB Monthly', 
			'9mobile 18.5GB Monthly'],
	'value': [4.25, 5.5, 8, 11, 15, 20, 25, 18, 14, 2.2, 
				8, 10, 13, 18, 25, 5.5, 7, 12, 15],
	'cost': [3000, 3500, 4500, 5000, 6500, 7500, 
			8000, 6000, 5000, 1000, 
			3000, 4000, 5000, 6000, 8000, 
			2000, 2500, 3000, 4000],
	'color': [yellow, yellow, yellow, yellow, yellow, yellow, 
				green, green, green, green, red, red, red, red, red, 
				d_green, d_green, d_green, d_green]
	},

	'Bi-Monthly to Quarterly': {
	'plan': ['9mobile 225GB 2-Month', '9mobile 425GB 3-Month', 

			'Airtel 300GB 3-Month', 'Glo 320GB 2-Month Mega', 
			'Glo 380GB 3-Month Mega', 'Glo 475GB 3-Month Mega', 

			'MTN 90GB 2-Month', 'MTN 150GB 2-Month', 
			'MTN 200GB 2-Month', 'MTN 480GB 3-Month'],
	'value': [225, 425, 300, 320, 380, 475, 90, 150, 200, 480],
	'cost': [30000, 50000, 50000, 50000, 60000, 75000, 25000, 40000, 
			50000, 120000],
	'color': [d_green, d_green, red, green, green, green, yellow, 
				yellow, yellow, yellow]
	},

	'Bi-Annual to Annual': {
	'plan': ['9mobile 600GB 6-Month', '9mobile 1TB Annual', 

			'Glo 1TB Annual Mega', 'Airtel 300GB 3-Month', 
			'Airtel 350GB 6-Month', 'Airtel 650GB Yearly'],
	'value': [600, 1024, 1024, 300, 350, 650],
	'cost': [70000, 100000, 100000, 50000, 60000, 100000],
	'color': [d_green, d_green, green, red, red, red]
	}
}

def best(category: str):
	"""Display the best value plans across all networks."""

	category_df = pd.DataFrame(best_plans_all[category])
	plans = category_df['plan']
	values = np.array(category_df['value'])
	costs = np.array(category_df['cost'])
	colors = category_df['color']
	category_df['vpc'] = values / costs
	sorted_category_df = category_df.sort_values(by='vpc', ascending=True)
	colors = sorted_category_df['color']

	for i in range(len(sorted_category_df['plan'])):
		plt.text(sorted_category_df['vpc'][i]+0.00002, sorted_category_df['plan'][i], 
			f"\u20A6{sorted_category_df['cost'][i]}", fontsize=9, va='center')

	plt.barh(sorted_category_df['plan'], sorted_category_df['vpc'], color=colors)
	plt.title(f'Best Value {category} Plans (All Networks)')
	plt.yticks(plans)
	plt.xticks([])
	plt.show()
