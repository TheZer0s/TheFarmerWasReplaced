while True:
	Main()

def Main():
	goal = 10000
	while True:
		till_All()
		if num_items(Items.Hay) < goal:
			Grass(goal)
		elif num_items(Items.Wood) < goal:
			Trees(goal)
		elif num_items(Items.Carrot) < goal:
			Carrots(goal)
		elif num_items(Items.Pumpkin) < goal:
			Pumpkin(goal)
		else:
			break

def till_All():
	area = get_world_size() * get_world_size()
	area_check = 0
	while True:
		for i in range(get_world_size()):
			for j in range(1):
				move(North)
				if can_harvest():
					harvest()
					if get_ground_type() == Grounds.Turf:
						till()
				if can_harvest() != True:
					area_check += 1
				
		move(East)
		if area_check >= area:
			break

def Grass(s_goal):	
		while num_items(Items.Hay) < s_goal:
			for i in range(get_world_size()):
				for j in range(1):
					move(North)
					if can_harvest():
						harvest()
						plant(Entities.Grass)
					else:
						plant(Entities.Grass)
			move(East)


def Trees(s_goal):	
	if num_items(Items.Water_Tank) < 100:
		Tank_Buffer()
	while num_items(Items.Wood) < s_goal:
		for x in range(get_world_size()):
			for j in range(1):
				move(North)
				if (get_pos_x() + get_pos_y()) % 2 == 0:
						harvest()
						if get_water() < 1:
							use_item(Items.Water_Tank)
							plant(Entities.Tree)
						
				else:
					if can_harvest():
						harvest()
					plant(Entities.Bush)
		move(East)	

def Carrots(s_goal):
	while num_items(Items.Carrot) < s_goal:
		world_Area = get_world_size() * get_world_size()
		if num_items(Items.Carrot_Seed) < world_Area:
			for i in range(world_Area):
				trade(Items.Carrot_Seed)
		for i in range(get_world_size()):
			for j in range(1):
				move(North)
				if get_ground_type() == Grounds.Turf:
					if can_harvest():
						harvest()
						till()
						plant(Entities.Carrots)
				else:
					if can_harvest():
						harvest()
					trade(Items.Carrot_Seed)
					plant(Entities.Carrots)
						
		move(East)


def Pumpkin(s_goal):
	pumpkins = 0
	while num_items(Items.Pumpkin) < s_goal:
		world_area = get_world_size() * get_world_size()
		if num_items(Items.Pumpkin_Seed) < world_area:
			for i in range(world_area * get_world_size()):
				trade(Items.Pumpkin_Seed)
		for i in range(get_world_size()):
			for j in range(1):
				move(North)
				if pumpkins < s_goal:
					if get_entity_type() != Entities.Pumpkin:
						harvest()
					else:
						plant(Entities.Pumpkin)
						pumpkins += 1
					plant(Entities.Pumpkin)
					pumpkins += 1 
					
				if( pumpkins >= world_area * 8 ):
					harvest()
					pumpkins = 0
		move(East)
		
# Would like to have a function in place to track if all plots are pumpkins or not
