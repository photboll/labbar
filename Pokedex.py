class Pokemon:
    def __init__(self,attributes):
        self.name = str(attributes[2])
        self.type = str(attributes[2])
        self.hp = int(attributes[3])
        self.atk = int(attributes[4])
        self.defen = int(attributes[5])
        self.spa = int(attributes[6])
        self.spd = int(attributes[7])
        self.speed = int(attributes[8])
        self.mass = float(attributes[16][:-3])

    def __str__(self):
        return self.name

    def __lt__(self,other):
        if self.mass < other.mass :
            return True
        else:
            return False
    def change_name(self,new_name):
        self.name = new_name

    #ökar pokemonens hp, indata är hur mycket mer hp den får
    def increase_hp(self, extra_hp):
        self.hp = self.hp + extra_hp
    #returnerar summan av pokemonens stats
    def tot_stats(self):
        return int(self.hp + self.atk + self.defen + self.spa + self.spd + self.speed)

    def get_type(self):
        return self.type
class Gym:
    def __init__(self,gym_name,members):
        self.members = members
        self.name = gym_name

    def __str__(self):
        return self.name

    def add_member(self,member):
        if type(member) == Pokemon :
            self.members.append(member)
            print(str(member)+'lades till i gymmet')

    def remove_member(self,member):
        for i in self.members:
            if str(i) == member:
                self.members.remove(i)
                print(str(i)+'avlägsnades')

    def view_members(self):
        for member in self.members:
            print(str(member)+' of type '+str(member.get_type()))
    #tar emot en lista med namn och ser om de är medlem i gymmet, returnerar en
    # lista med medlammarna som efterfrågades
    def member_search(self,queries):
        matching_queries =[]
        for member in self.members :
            if str(member) in queries :
                matching_queries.append(member)
        return matching_queries

    #retrunerar den tyngsta medlemmen i gymmet
    def get_heaviest(self):
        heaviest_member = self.members[0]
        for member in self.members:
            if member > heaviest_member:
                heaviest_member = member
        return heaviest_member

    #retrunerar den lättaste medlemmen i gymmet
    def get_lightest(self):
        lightest_member = self.members[0]
        for member in self.members:
            if not lightest_member.__lt__(member):
                lightest_member = member
        return lightest_member

    #returnerar medlemen med största totala stats
    def get_strongest(self):
        strongest_member = self.members[0]
        for member in self.members:
            if member.tot_stats() > strongest_member.tot_stats():
                strongest_member = member
        return strongest_member


def hardcoded_poke():
    attributes1 = [1,1,'Bulbasaur',45,49,49,65,65,45,318,'Grass','Poison','NU','Overgrow',''
    ,'Chlorophyll','6.9 kG',20,'1 SpA',64,'Green',5120,'M (87.5%)','Monster','Grass',45,1059860,'',1,1,226,'','','','Bulbasaur']
    attributes2 = [4,4,'Charmander',39,52,43,60,50,65,309,'Fire','','NU','Blaze','','Solar Power',
    '8.5 kG',20,'1 Spe',65,'Red',5120,'M (87.5%)','Monster','Dragon',45,1059860,'',4,4,229,'','','','Charmander']
    Bulbasaur = Pokemon(attributes1)
    Charmander = Pokemon(attributes2)
    print (Bulbasaur)
    print (Charmander)

def create_pokedex(size):
    fil = open('Excel Pkdx V5.14 - Pokedex.csv','r')
    fil.readline()
    pokedex =[]
    for i in range(size) :
        attributes = fil.readline().rstrip('').split(',')
        poke = Pokemon(attributes)
        #print(poke)
        pokedex.append(poke)
    return pokedex

def gym_test(n):
    members = create_pokedex(n)
    first_gym = Gym('The first gym',members)
    queries = ['bulbasaur','hejsvejs','Charmander','Caterpie']
    matching_queries = first_gym.member_search(queries)
    for match in matching_queries:
        print (match)
    print(first_gym.get_heaviest())
    print(first_gym.get_lightest())
    print(first_gym.get_strongest())
    print('_______')
    attributes1 = [1,1,'Bulbasaur',45,49,49,65,65,45,318,'Grass','Poison','NU','Overgrow',''
    ,'Chlorophyll','6.9 kG',20,'1 SpA',64,'Green',5120,'M (87.5%)','Monster','Grass',45,1059860,'',1,1,226,'','','','Bulbasaur']
    Bulbasaur = Pokemon(attributes1)
    Bulbasaur.change_name('BILLBAU')
    first_gym.add_member(Bulbasaur)
    first_gym.add_member('asdasda')
    first_gym.view_members()
    print('________')
    first_gym.remove_member('BILLBAU')
    first_gym.view_members()
    print(first_gym.get_heaviest())
gym_test(5)
